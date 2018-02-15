import sys
import re
from antlr4 import *
from .LokiLexer import LokiLexer
from .LokiParser import LokiParser
from .LokiListener import LokiListener


class LokiPattern(object):
    """
    Houses a sequence of pattern fragments
    """
    def __init__(self, fragments):
        self.fragments = fragments

    def match(self, sentence, start_indices):
        num_fragments = len(self.fragments)
        indices = start_indices
        for i, frag in enumerate(self.fragments):
            passed = frag.match(sentence, indices)
            # if this isn't the final pattern fragment, we need to advance one token iff the next frag is also a TokenPattern
            # ex. "<dobj [lemma="make"] [] >dep", but not "<dobj [lemma="make"] >dep"
            if isinstance(frag, TokenPattern) and i + 1 < num_fragments and isinstance(self.fragments[i + 1], TokenPattern):
                indices = [idx + 1 for idx in passed if idx + 1 < len(sentence.words)]
            # this covers both TraversalPatterns as well as fragment-final TokenPatterns
            else:
                indices = list(passed)
            if not indices:
                return []
        return indices

class TraversalPattern(object):
    """
    Base class for graph-based traversal patterns
    """
    def __init__(self, is_regex=False, pattern=None):
        self.is_regex = is_regex
        self.pattern = pattern

    def compile(self):
        """
        compiles a traversal pattern
        """
        if self.is_regex and not isinstance(self.pattern, re._pattern_type):
            self.pattern = re.compile(self.pattern)

    def match_token(self, candidate):
        """
        Checks token against regex or literal pattern
        """
        # re.search isn't anchored (cf re.match)
        return self.pattern.search(candidate) != None if self.is_regex else self.pattern == candidate


class IncomingTraversal(TraversalPattern):
    """
    """
    def __init__(self, is_regex=False, pattern=None):
        super(IncomingTraversal, self).__init__(is_regex, pattern)

    def match(self, sentence, start_indices):
        # check if compiled
        self.compile()
        destinations = set()
        for start in start_indices:
            for (dest, rel) in sentence.dependencies.incoming[start]:
                if self.match_token(rel):
                    destinations.add(dest)
        return destinations


class OutgoingTraversal(TraversalPattern):
    """
    """
    def __init__(self, is_regex=False, pattern=None):
        super(OutgoingTraversal, self).__init__(is_regex, pattern)

    def match(self, sentence, start_indices):
        # check if compiled
        self.compile()
        destinations = set()
        for start in start_indices:
            for (dest, rel) in sentence.dependencies.outgoing[start]:
                if self.match_token(rel):
                    destinations.add(dest)
        return destinations


class IncomingWildcard(TraversalPattern):
    """
    """
    def __init__(self):
        super().__init__()

    def match(self, sentence, start_indices):
        destinations = set()
        for start in start_indices:
            for (dest, _) in sentence.dependencies.incoming[start]:
                destinations.add(dest)
        return destinations


class OutgoingWildcard(TraversalPattern):
    """
    """
    def __init__(self):
        super().__init__()

    def match(self, sentence, start_indices):
        destinations = set()
        for start in start_indices:
            for (dest, _) in sentence.dependencies.outgoing[start]:
                destinations.add(dest)
        return destinations

##############################
# Token patterns
##############################

class TokenPattern(object):
    """
    """
    def match(self, sentence, start_indices):
        pass

class TokenWildcard(TokenPattern):
    """
    """
    def __init__(self):
        super().__init__()

    # FIXME: write this
    def match(self, sentence, start_indices):
        pass

class TokenConstraint(TokenPattern):
    """
    """
    def __init__(self):
        super().__init__()
        # ex. lemma=cat
        self.attribute_constraints = []
    # TODO: test me
    def match(self, sentence, start_indices):
        indices = start_indices
        for ac in self.attribute_constraints:
            indices = ac.match(sentence, indices)
            if not indices:
                return []
        return indices

class AttributeConstraint(object):
    """
    """
    def __init__(self, token_attribute=None, negated=False, is_regex=False, pattern=None):
        self.token_attribute = token_attribute
        self.negated = negated
        self.is_regex = is_regex
        self.pattern = pattern

    def to_loki_pattern(self):
        self.compile()
        neg_repr = "" if not self.negated else "!"
        # pattern.pattern assumes re.compile()
        pattern_repr = "/{}/".format(self.pattern.pattern) \
        if self.is_regex and isinstance(self.pattern, re._pattern_type) else self.pattern
        return "{neg}{tok_attr}={patt}".format(
                neg=neg_repr,
                tok_attr=self.token_attribute,
                patt=pattern_repr
        )

    def compile(self):
        """
        compiles Attribute Constraint
        """
        if self.is_regex and not isinstance(self.pattern, re._pattern_type):
            self.pattern = re.compile(self.pattern)

    def match(self, sentence, start_indices):

        self.compile()

        def match_token(candidate):
            """
            Checks token against regex or literal pattern
            """
            # NOTE: re.search isn't anchored (cf re.match)
            matched = self.pattern.search(candidate) != None if self.is_regex else self.pattern == candidate
            #print("matched '{}'? {}".format(candidate, matched))
            # ex. negated == False and match == True  +> False != True -> True
            # ex. negated == True and match == True  +> True != True -> False
            return self.negated != matched

        def match_tokens(tokens):
            """
            """
            return [i for i in start_indices if i < len(tokens) and match_token(tokens[i])]

        def match_deps(deps):
            """
            """
            indices = []
            for i in start_indices:
                for (_, rel) in deps[i]:
                    if match_token(rel):
                        indices.append(i)
            return indices

        if self.token_attribute == "word":
            toks = sentence.words
            return match_tokens(toks)
        if self.token_attribute == "tag":
            toks = sentence.words
            return match_tokens(toks)
        if self.token_attribute == "lemma":
            toks = sentence.lemmas
            return match_tokens(toks)
        if self.token_attribute == "chunk":
            toks = sentence.chunks
            return match_tokens(toks)
        if self.token_attribute == "incoming":
            deps = sentence.dependencies.incoming
            return match_deps(deps)
        if self.token_attribute == "outgoing":
            deps = sentence.dependencies.outgoing
            return match_deps(deps)

class LokiPatternListener(LokiListener):
    """
    """
    def __init__(self):
        self.fragments = []
        self.graph_traversal_fragment = None
        self.token_constraint_fragment = None
        self.attribute_constraint_fragment = None

    def enterGraph_traversal(self, ctx):
        # print("entering graph traversal pattern...")
        assert(self.graph_traversal_fragment is None)

    def exitGraph_traversal(self, ctx):
        # print("exiting graph traversal pattern...")
        assert(self.graph_traversal_fragment is not None)
        frag = self.graph_traversal_fragment
        frag.compile()
        self.fragments.append(frag)
        self.graph_traversal_fragment = None

    def enterIncoming_wildcard(self, ctx):
        # print("entering incoming wildcard...")
        assert(self.graph_traversal_fragment is None)

    def exitIncoming_wildcard(self, ctx):
        # print("leaving incoming wildcard...")
        self.graph_traversal_fragment = IncomingWildcard()

    def enterOutgoing_wildcard(self, ctx):
        # print("entering outgoing wildcard...")
        assert(self.graph_traversal_fragment is None)

    def exitOutgoing_wildcard(self, ctx):
        # print("leaving outgoing wildcard...")
        self.graph_traversal_fragment = OutgoingWildcard()

    def enterIncoming_traversal(self, ctx):
        # print("entering incoming traversal...")
        assert(self.graph_traversal_fragment is None)
        self.graph_traversal_fragment = IncomingTraversal()

    def enterOutgoing_traversal(self, ctx):
        # print("entering outgoing traversal...")
        assert(self.graph_traversal_fragment is None)
        self.graph_traversal_fragment = OutgoingTraversal()

    def enterToken_constraint(self, ctx):
        # print("Constructing token constraint...")
        assert(self.token_constraint_fragment == None)
        # start building a token constraint
        self.token_constraint_fragment = TokenConstraint()

    def exitToken_constraint(self, ctx):
        # print("Analyzing completed token constraint...")
        frag = self.token_constraint_fragment
        assert(frag != None)
        # no attribute constraints means this is a wildcard
        if len(frag.attribute_constraints) == 0:
            self.fragments.append(TokenWildcard())
        else:
            #frag.compile()
            self.fragments.append(frag)
        # reset token constraint fragment
        self.token_constraint_fragment = None

    def enterToken_attribute(self, ctx):
        # print("Analyzing token attribute type...")
        assert(self.attribute_constraint_fragment != None)
        #print(ctx.__dict__)
        token_attribute = ctx.getText()
        # print("token attribute: {}".format(token_attribute))
        self.attribute_constraint_fragment.token_attribute = token_attribute

    def exitToken_attribute(self, ctx):
        # print("validating token attribute...")
        assert(self.attribute_constraint_fragment.token_attribute != None)

    def enterAttribute_constraint(self, ctx):
        # print("Beginning attribute constraint...")
        # NOTE: because negatedAttributeConstraint occurs higher in the tree,
        # attribute_constraint_fragment may not be none
        #assert(self.attribute_constraint_fragment == None)
        if not self.attribute_constraint_fragment:
            self.attribute_constraint_fragment = AttributeConstraint()

    def exitAttribute_constraint(self, ctx):
        # print("Exiting attribute constraint...")
        assert(self.attribute_constraint_fragment != None)
        assert(self.token_constraint_fragment != None)
        frag = self.attribute_constraint_fragment
        # print("is_regex? {}".format(self.attribute_constraint_fragment.is_regex))
        # print("frag.negated? {}".format(frag.negated))
        # print("Compiling attribute constraint...")
        frag.compile()
        # print("is_regex (after compilation)? {}".format(frag.is_regex))
        self.token_constraint_fragment.attribute_constraints.append(frag)
        self.attribute_constraint_fragment = None

    def enterNegated_attribute_constraint(self, ctx):
        # print("Detected negated token attribute contraint...")
        # NOTE: negated_attribute_constraint occurs higher in the tree than attribute_constraint
        assert(self.attribute_constraint_fragment == None)
        self.attribute_constraint_fragment = AttributeConstraint()
        self.attribute_constraint_fragment.negated = True
        # print("negated? {}".format(self.attribute_constraint_fragment.negated))
        # NOTE: though lower in the tree, we'll let exitAttribute_constraint handle appending

    def enterLiteral(self, ctx):
        # print("Detected literal...")
        pattern = ctx.getText()
        # print("Literal: {}".format(pattern))
        self.store_pattern(pattern, is_regex=False)

    def enterRegex(self, ctx):
        # print("Detected regex...")
        pattern = ctx.getText()
        # print("Regex: {}".format(pattern))
        self.store_pattern(pattern, is_regex=True)

    def store_pattern(self, pattern, is_regex=False):
        # check if this belongs to an attribute constraint for a token
        if self.attribute_constraint_fragment != None and self.graph_traversal_fragment == None:
            self.attribute_constraint_fragment.pattern = pattern
            self.attribute_constraint_fragment.is_regex = is_regex
        # check if this belongs to a graph traversal fragment
        elif self.attribute_constraint_fragment == None and self.graph_traversal_fragment != None:
            self.graph_traversal_fragment.pattern = pattern
            self.graph_traversal_fragment.is_regex = is_regex
        # if neither, throw an exception
        else:
            raise Exception("Regex or literal belongs to neither an attribute_constraint nor a graph_traversal")


class LokiCompiler(object):
    """
    """
    @staticmethod
    def compile(pattern):
        input_stream = InputStream(pattern)
        lexer = LokiLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = LokiParser(stream)
        loki_tree = parser.loki_pattern()
        listener = LokiPatternListener()
        walker = ParseTreeWalker()
        walker.walk(listener, loki_tree)
        frags = listener.fragments
        return LokiPattern(frags)
        #return loki_tree

if __name__ == '__main__':
    main(sys.argv)
