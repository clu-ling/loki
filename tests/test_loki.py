#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import json
import os
from processors import Sentence
from loki import *

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

json_file = os.path.join(__location__, "sentence.json")
with open(json_file, "r") as jf:
    sentence = Sentence.load_from_JSON(json.load(jf))

json_file = os.path.join(__location__, "sentence2.json")
with open(json_file, "r") as jf:
    sentence2 = Sentence.load_from_JSON(json.load(jf))

class LokiTests(unittest.TestCase):
    """
    Test application of Loki patterns
    """
    def test_token_wildcard(self):
        pattern = '[]'
        compiled_pattern = LokiCompiler.compile(pattern)
        "{} should compile and match correctly".format(pattern)
        res = compiled_pattern.match(sentence, range(len(sentence.words)))
        self.assertTrue(res == list(range(len(sentence.words))), "{} starting from any token should be valid at all positions. Actual position: {}".format(pattern, res))
        res = compiled_pattern.match(sentence, [10])
        self.assertTrue(res == [10], "{} starting from position 10 should be valid. Actual position: {}".format(pattern, res))
        res = compiled_pattern.match(sentence, [100])
        self.assertTrue(res == [], "{} starting from position 100 should not be valid. Actual position: {}".format(pattern, res))

    def test_token_lemma_exact(self):
        pattern = '[lemma=mistake]'
        compiled_pattern = LokiCompiler.compile(pattern)
        "{} should compile and match correctly".format(pattern)
        res = compiled_pattern.match(sentence, range(len(sentence.words)))
        self.assertTrue(res == [4], "{} starting from any token should only be valid at position 4. Actual position: {}".format(pattern, res))
        res = compiled_pattern.match(sentence, [10])
        self.assertTrue(res == [], "{} starting from position 10 should not be valid. Actual position: {}".format(pattern, res))
        res = compiled_pattern.match(sentence, [100])
        self.assertTrue(res == [], "{} starting from position 100 should not be valid. Actual position: {}".format(pattern, res))

    def test_token_lemma_regex(self):
        pattern = '[lemma=/ake$/]'
        compiled_pattern = LokiCompiler.compile(pattern)
        "{} should compile and match correctly".format(pattern)
        res = compiled_pattern.match(sentence, range(len(sentence.words)))
        self.assertTrue(res == [3,4], "{} starting from any token should only be valid at positions 3 and 4. Actual position: {}".format(pattern, res))
        res = compiled_pattern.match(sentence, [10])
        self.assertTrue(res == [], "{} starting from position 10 should not be valid. Actual position: {}".format(pattern, res))
        res = compiled_pattern.match(sentence, [100])
        self.assertTrue(res == [], "{} starting from position 100 should not be valid. Actual position: {}".format(pattern, res))

    def test_token_lemma_negated_exact(self):
        pattern = '[!lemma=mistake]'
        compiled_pattern = LokiCompiler.compile(pattern)
        "{} should compile and match correctly".format(pattern)
        res = compiled_pattern.match(sentence, range(len(sentence.words)))
        self.assertTrue(res == [0,1,2,3,5,6,7,8,9,10], "{} starting from any token should not be valid at position 4. Actual position: {}".format(pattern, res))
        res = compiled_pattern.match(sentence, [10])
        self.assertTrue(res == [10], "{} starting from position 10 should be valid at position 10. Actual position: {}".format(pattern, res))
        res = compiled_pattern.match(sentence, [100])
        self.assertTrue(res == [], "{} starting from position 100 should not be valid. Actual position: {}".format(pattern, res))

    def test_token_tag_exact(self):
        pattern = '[tag=NNS]'
        compiled_pattern = LokiCompiler.compile(pattern)
        "{} should compile and match correctly".format(pattern)
        res = compiled_pattern.match(sentence, range(len(sentence.words)))
        self.assertTrue(res == [4,9], "{} starting from any token should only be valid at positions 4 and 9. Actual position: {}".format(pattern, res))
        res = compiled_pattern.match(sentence, [10])
        self.assertTrue(res == [], "{} starting from position 10 should not be valid. Actual position: {}".format(pattern, res))
        res = compiled_pattern.match(sentence, [100])
        self.assertTrue(res == [], "{} starting from position 100 should not be valid. Actual position: {}".format(pattern, res))

    def test_token_tag_regex(self):
        pattern = '[tag=/^NN/]'
        compiled_pattern = LokiCompiler.compile(pattern)
        "{} should compile and match correctly".format(pattern)
        res = compiled_pattern.match(sentence, range(len(sentence.words)))
        self.assertTrue(res == [4,9], "{} starting from any token should only be valid at positions 4 and 9. Actual position: {}".format(pattern, res))
        res = compiled_pattern.match(sentence, [10])
        self.assertTrue(res == [], "{} starting from position 10 should not be valid. Actual position: {}".format(pattern, res))
        res = compiled_pattern.match(sentence, [100])
        self.assertTrue(res == [], "{} starting from position 100 should not be valid. Actual position: {}".format(pattern, res))

    def test_token_tag_negated_exact(self):
        pattern = '[!tag=NNS]'
        compiled_pattern = LokiCompiler.compile(pattern)
        "{} should compile and match correctly".format(pattern)
        res = compiled_pattern.match(sentence, range(len(sentence.words)))
        self.assertTrue(res == [0,1,2,3,5,6,7,8,10], "{} starting from any token should not be valid at positions 4 or 9. Actual position: {}".format(pattern, res))
        res = compiled_pattern.match(sentence, [10])
        self.assertTrue(res == [10], "{} starting from position 10 should be valid at position 10. Actual position: {}".format(pattern, res))
        res = compiled_pattern.match(sentence, [100])
        self.assertTrue(res == [], "{} starting from position 100 should not be valid. Actual position: {}".format(pattern, res))

    def test_multi_token_pattern(self):
        pattern = '[lemma=make] [lemma=mistake]'
        compiled_pattern = LokiCompiler.compile(pattern)
        "{} should compile and match correctly".format(pattern)
        res = compiled_pattern.match(sentence, [3])
        self.assertTrue(res == [4], "{} starting from position 3 should lead to position 4. Actual position: {}".format(pattern, res))
        res = compiled_pattern.match(sentence,  range(len(sentence.words)))
        self.assertTrue(res == [4], "{} starting from any position should only lead to position 4. Actual position: {}".format(pattern, res))
        res = compiled_pattern.match(sentence, [1])
        self.assertTrue(res == [], "{} starting from position 1 should not be valid. Actual position: {}".format(pattern, res))

    def test_outgoing_wildcard(self):
        pattern = '>>'
        compiled_pattern = LokiCompiler.compile(pattern)
        "{} should compile and match correctly".format(pattern)
        # advmod
        res = compiled_pattern.match(sentence, [7])
        self.assertTrue(res == [6], "{} starting from position 7 should lead to position 6 by advmod. Actual position: {}".format(pattern, res))
        # 3 is the sentential root
        res = compiled_pattern.match(sentence,  [3])
        self.assertTrue(res == [0, 1, 2, 4, 5, 9, 10], "{} starting from the sentential root (position 3) should only lead to positions [0, 1, 2, 4, 5, 9, 10]. Actual position: {}".format(pattern, res))

    def test_incoming_wildcard(self):
        pattern = '<<'
        compiled_pattern = LokiCompiler.compile(pattern)
        "{} should compile and match correctly".format(pattern)
        # advmod
        res = compiled_pattern.match(sentence, [6])
        self.assertTrue(res == [7], "{} starting from position 6 should lead to position 7 by advmod. Actual position: {}".format(pattern, res))
        # 3 is the sentential root
        res = compiled_pattern.match(sentence, [0, 1, 2, 4, 5, 9, 10])
        self.assertTrue(res == [3], "{} starting from positions [0, 1, 2, 4, 5, 9, 10] should only lead to the sentential root (position 3). Actual position: {}".format(pattern, res))

    def test_outgoing_exact(self):
        pattern = '>dobj'
        compiled_pattern = LokiCompiler.compile(pattern)
        "{} should compile and match correctly".format(pattern)
        # advmod
        res = compiled_pattern.match(sentence, [3])
        self.assertTrue(res == [4], "{} starting from position 3 should lead to position 4. Actual position: {}".format(pattern, res))
        # 3 is the sentential root
        res = compiled_pattern.match(sentence, [2])
        self.assertTrue(res == [], "{} starting from position 2 should not lead anywhere. Actual position: {}".format(pattern, res))

    def test_incoming_exact(self):
        pattern = '>/bj$/'
        compiled_pattern = LokiCompiler.compile(pattern)
        "{} should compile and match correctly".format(pattern)
        # advmod
        res = compiled_pattern.match(sentence, [3])
        self.assertTrue(res == [0, 4], "{} starting from position 3 should lead to positions 0 and 4. Actual position: {}".format(pattern, res))
        # 3 is the sentential root
        res = compiled_pattern.match(sentence, [2])
        self.assertTrue(res == [], "{} starting from position 2 should not lead anywhere. Actual position: {}".format(pattern, res))

    def test_multihop_graph_traversal(self):
        pattern = "<< >dep >dep"
        compiled_pattern = LokiCompiler.compile(pattern)
        "{} should compile and match correctly".format(pattern)
        self.assertTrue(len(compiled_pattern.fragments) == 3, "{} should produce 3 fragments, but {} generated".format(pattern, len(compiled_pattern.fragments)))
        res = compiled_pattern.match(sentence2, [43])
        self.assertTrue(res == [72], "{} starting from position 43 should lead to position 72. Actual position: {}".format(pattern, res))

    def test_multihop_exact(self):
        pattern = '<dobj [lemma="make"]'
        compiled_pattern = LokiCompiler.compile(pattern)
        "{} should compile and match correctly".format(pattern)
        res = compiled_pattern.match(sentence, [4])
        self.assertTrue(res == [3], "{} starting from position 4 should lead to position 3. Actual position: {}".format(pattern, res))
        res = compiled_pattern.match(sentence, range(len(sentence.words)))
        self.assertTrue(res == [3], "{} starting from any position should only lead to position 3. Actual position: {}".format(pattern, res))

    def test_multihop_exact2(self):
        pattern = '<dobj [lemma=make]'
        compiled_pattern = LokiCompiler.compile(pattern)
        "{} should compile and match correctly".format(pattern)
        res = compiled_pattern.match(sentence, [4])
        self.assertTrue(res == [3], "{} starting from position 4 should lead to position 3. Actual position: {}".format(pattern, res))
        res = compiled_pattern.match(sentence, range(len(sentence.words)))
        self.assertTrue(res == [3], "{} starting from any position should only lead to position 3. Actual position: {}".format(pattern, res))

    def test_multihop_exact3(self):
        pattern = '<dobj [lemma="make"] >dep'
        compiled_pattern = LokiCompiler.compile(pattern)
        "{} should compile and match correctly".format(pattern)
        res = compiled_pattern.match(sentence, [4])
        self.assertTrue(res == [9], "{} starting from position 4 should lead to position 9. Actual position: {}".format(pattern, res))
        res = compiled_pattern.match(sentence, range(len(sentence.words)))
        self.assertTrue(res == [9], "{} starting from any position should only lead to position 9. Actual position: {}".format(pattern, res))

if __name__ == "__main__":
    unittest.main()
