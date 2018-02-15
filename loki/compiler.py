from antlr4 import *
from .LokiLexer import LokiLexer
from .LokiParser import LokiParser
from .LokiListener import LokiListener
from .patterns import *


class LokiPatternListener(LokiListener):
    """
    Custom listener for compilation of Loki patterns
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

    def enterToken_wildcard(self, ctx):
        # print("entering token wildcard...")
        assert(self.token_constraint_fragment == None)
        self.fragments.append(TokenWildcard())

    def enterToken_constraint(self, ctx):
        # print("Constructing token constraint...")
        assert(self.token_constraint_fragment == None)
        # start building a token constraint
        self.token_constraint_fragment = TokenConstraint()

    def exitToken_constraint(self, ctx):
        # print("Analyzing completed token constraint...")
        frag = self.token_constraint_fragment
        assert(frag != None)
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
