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

class LokiTests(unittest.TestCase):
    """
    Test application of Loki patterns
    """
    def test_token_lemma_exact(self):
        pattern = '[lemma=mistake]'
        compiled_pattern = LokiCompiler.compile(pattern)
        "{} should compile and match correctly".format(pattern)
        self.assertTrue(compiled_pattern.match(sentence, range(len(sentence.words))) == [4], "{} starting from any token should only be valid at position 4.".format(pattern))
        self.assertTrue(compiled_pattern.match(sentence, [10]) == [], "{} starting from position 10 should not be valid.".format(pattern))
        self.assertTrue(compiled_pattern.match(sentence, [100]) == [], "{} starting from position 100 should not be valid.".format(pattern))

    def test_token_lemma_regex(self):
        pattern = '[lemma=/ake$/]'
        compiled_pattern = LokiCompiler.compile(pattern)
        "{} should compile and match correctly".format(pattern)
        self.assertTrue(compiled_pattern.match(sentence, range(len(sentence.words))) == [3,4], "{} starting from any token should only be valid at positions 3 and 4.".format(pattern))
        self.assertTrue(compiled_pattern.match(sentence, [10]) == [], "{} starting from position 10 should not be valid.".format(pattern))
        self.assertTrue(compiled_pattern.match(sentence, [100]) == [], "{} starting from position 100 should not be valid.".format(pattern))

    def test_token_lemma_negated_exact(self):
        pattern = '[!lemma=mistake]'
        compiled_pattern = LokiCompiler.compile(pattern)
        "{} should compile and match correctly".format(pattern)
        self.assertTrue(compiled_pattern.match(sentence, range(len(sentence.words))) == [0,1,2,3,5,6,7,8,9,10], "{} starting from any token should not be valid at position 4.".format(pattern))
        self.assertTrue(compiled_pattern.match(sentence, [10]) == [10], "{} starting from position 10 should be valid at position 10.".format(pattern))
        self.assertTrue(compiled_pattern.match(sentence, [100]) == [], "{} starting from position 100 should not be valid.".format(pattern))

    def test_multi_token_pattern(self):
        pattern = '[lemma=make] [lemma=mistake]'
        compiled_pattern = LokiCompiler.compile(pattern)
        "{} should compile and match correctly".format(pattern)
        self.assertTrue(compiled_pattern.match(sentence, [3]) == [4], "{} starting from position 3 should lead to position 4.".format(pattern))
        self.assertTrue(compiled_pattern.match(sentence,  range(len(sentence.words))) == [4], "{} starting from any position should only lead to position 4.".format(pattern))
        self.assertTrue(compiled_pattern.match(sentence, [1]) == [], "{} starting from position 1 should not be valid.".format(pattern))

    def test_outgoing_wildcard(self):
        pattern = '>>'
        compiled_pattern = LokiCompiler.compile(pattern)
        "{} should compile and match correctly".format(pattern)
        # advmod
        self.assertTrue(compiled_pattern.match(sentence, [7]) == [6], "{} starting from position 7 should lead to position 6 by advmod.".format(pattern))
        # 3 is the sentential root
        self.assertTrue(compiled_pattern.match(sentence,  [3]) == [0, 1, 2, 4, 5, 9, 10], "{} starting from the sentential root (position 3) should only lead to positions [0, 1, 2, 4, 5, 9, 10].".format(pattern))

    def test_incoming_wildcard(self):
        pattern = '<<'
        compiled_pattern = LokiCompiler.compile(pattern)
        "{} should compile and match correctly".format(pattern)
        # advmod
        self.assertTrue(compiled_pattern.match(sentence, [6]) == [7], "{} starting from position 6 should lead to position 7 by advmod.".format(pattern))
        # 3 is the sentential root
        self.assertTrue(compiled_pattern.match(sentence,  [0, 1, 2, 4, 5, 9, 10]) == [3], "{} starting from positions [0, 1, 2, 4, 5, 9, 10] should only lead to the sentential root (position 3).".format(pattern))

    def test_outgoing_exact(self):
        pattern = '>dobj'
        compiled_pattern = LokiCompiler.compile(pattern)
        "{} should compile and match correctly".format(pattern)
        # advmod
        self.assertTrue(compiled_pattern.match(sentence, [3]) == [4], "{} starting from position 3 should lead to position 4.".format(pattern))
        # 3 is the sentential root
        self.assertTrue(compiled_pattern.match(sentence,  [2]) == [], "{} starting from position 2 should not lead anywhere.".format(pattern))

    def test_incoming_exact(self):
        pattern = '>/bj$/'
        compiled_pattern = LokiCompiler.compile(pattern)
        "{} should compile and match correctly".format(pattern)
        # advmod
        self.assertTrue(compiled_pattern.match(sentence, [3]) == [0, 4], "{} starting from position 3 should lead to positions 0 and 4.".format(pattern))
        # 3 is the sentential root
        self.assertTrue(compiled_pattern.match(sentence,  [2]) == [], "{} starting from position 2 should not lead anywhere.".format(pattern))

    def test_multihop_exact(self):
        pattern = '<dobj [lemma="make"]'
        compiled_pattern = LokiCompiler.compile(pattern)
        "{} should compile and match correctly".format(pattern)
        self.assertTrue(compiled_pattern.match(sentence, [4]) == [3], "{} starting from position 4 should lead to position 3.".format(pattern))
        self.assertTrue(compiled_pattern.match(sentence, range(len(sentence.words))) == [3], "{} starting from any position should only lead to position 3.".format(pattern))

    def test_multihop_exact(self):
        pattern = '<dobj [lemma=make]'
        compiled_pattern = LokiCompiler.compile(pattern)
        "{} should compile and match correctly".format(pattern)
        self.assertTrue(compiled_pattern.match(sentence, [4]) == [3], "{} starting from position 4 should lead to position 3.".format(pattern))
        self.assertTrue(compiled_pattern.match(sentence, range(len(sentence.words))) == [3], "{} starting from any position should only lead to position 3.".format(pattern))

if __name__ == "__main__":
    unittest.main()
