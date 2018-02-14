# Generated from Loki.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LokiParser import LokiParser
else:
    from LokiParser import LokiParser

# This class defines a complete listener for a parse tree produced by LokiParser.
class LokiListener(ParseTreeListener):

    # Enter a parse tree produced by LokiParser#loki_pattern.
    def enterLoki_pattern(self, ctx:LokiParser.Loki_patternContext):
        pass

    # Exit a parse tree produced by LokiParser#loki_pattern.
    def exitLoki_pattern(self, ctx:LokiParser.Loki_patternContext):
        pass


    # Enter a parse tree produced by LokiParser#graph_traversal.
    def enterGraph_traversal(self, ctx:LokiParser.Graph_traversalContext):
        pass

    # Exit a parse tree produced by LokiParser#graph_traversal.
    def exitGraph_traversal(self, ctx:LokiParser.Graph_traversalContext):
        pass


    # Enter a parse tree produced by LokiParser#incoming_wildcard.
    def enterIncoming_wildcard(self, ctx:LokiParser.Incoming_wildcardContext):
        pass

    # Exit a parse tree produced by LokiParser#incoming_wildcard.
    def exitIncoming_wildcard(self, ctx:LokiParser.Incoming_wildcardContext):
        pass


    # Enter a parse tree produced by LokiParser#outgoing_wildcard.
    def enterOutgoing_wildcard(self, ctx:LokiParser.Outgoing_wildcardContext):
        pass

    # Exit a parse tree produced by LokiParser#outgoing_wildcard.
    def exitOutgoing_wildcard(self, ctx:LokiParser.Outgoing_wildcardContext):
        pass


    # Enter a parse tree produced by LokiParser#incoming_traversal.
    def enterIncoming_traversal(self, ctx:LokiParser.Incoming_traversalContext):
        pass

    # Exit a parse tree produced by LokiParser#incoming_traversal.
    def exitIncoming_traversal(self, ctx:LokiParser.Incoming_traversalContext):
        pass


    # Enter a parse tree produced by LokiParser#outgoing_traversal.
    def enterOutgoing_traversal(self, ctx:LokiParser.Outgoing_traversalContext):
        pass

    # Exit a parse tree produced by LokiParser#outgoing_traversal.
    def exitOutgoing_traversal(self, ctx:LokiParser.Outgoing_traversalContext):
        pass


    # Enter a parse tree produced by LokiParser#token_constraint.
    def enterToken_constraint(self, ctx:LokiParser.Token_constraintContext):
        pass

    # Exit a parse tree produced by LokiParser#token_constraint.
    def exitToken_constraint(self, ctx:LokiParser.Token_constraintContext):
        pass


    # Enter a parse tree produced by LokiParser#negated_attribute_constraint.
    def enterNegated_attribute_constraint(self, ctx:LokiParser.Negated_attribute_constraintContext):
        pass

    # Exit a parse tree produced by LokiParser#negated_attribute_constraint.
    def exitNegated_attribute_constraint(self, ctx:LokiParser.Negated_attribute_constraintContext):
        pass


    # Enter a parse tree produced by LokiParser#attribute_constraint.
    def enterAttribute_constraint(self, ctx:LokiParser.Attribute_constraintContext):
        pass

    # Exit a parse tree produced by LokiParser#attribute_constraint.
    def exitAttribute_constraint(self, ctx:LokiParser.Attribute_constraintContext):
        pass


    # Enter a parse tree produced by LokiParser#pattern.
    def enterPattern(self, ctx:LokiParser.PatternContext):
        pass

    # Exit a parse tree produced by LokiParser#pattern.
    def exitPattern(self, ctx:LokiParser.PatternContext):
        pass


    # Enter a parse tree produced by LokiParser#pattern_regex.
    def enterPattern_regex(self, ctx:LokiParser.Pattern_regexContext):
        pass

    # Exit a parse tree produced by LokiParser#pattern_regex.
    def exitPattern_regex(self, ctx:LokiParser.Pattern_regexContext):
        pass


    # Enter a parse tree produced by LokiParser#pattern_literal.
    def enterPattern_literal(self, ctx:LokiParser.Pattern_literalContext):
        pass

    # Exit a parse tree produced by LokiParser#pattern_literal.
    def exitPattern_literal(self, ctx:LokiParser.Pattern_literalContext):
        pass


    # Enter a parse tree produced by LokiParser#inner_pattern.
    def enterInner_pattern(self, ctx:LokiParser.Inner_patternContext):
        pass

    # Exit a parse tree produced by LokiParser#inner_pattern.
    def exitInner_pattern(self, ctx:LokiParser.Inner_patternContext):
        pass


    # Enter a parse tree produced by LokiParser#regex.
    def enterRegex(self, ctx:LokiParser.RegexContext):
        pass

    # Exit a parse tree produced by LokiParser#regex.
    def exitRegex(self, ctx:LokiParser.RegexContext):
        pass


    # Enter a parse tree produced by LokiParser#literal.
    def enterLiteral(self, ctx:LokiParser.LiteralContext):
        pass

    # Exit a parse tree produced by LokiParser#literal.
    def exitLiteral(self, ctx:LokiParser.LiteralContext):
        pass


    # Enter a parse tree produced by LokiParser#token_attribute.
    def enterToken_attribute(self, ctx:LokiParser.Token_attributeContext):
        pass

    # Exit a parse tree produced by LokiParser#token_attribute.
    def exitToken_attribute(self, ctx:LokiParser.Token_attributeContext):
        pass


