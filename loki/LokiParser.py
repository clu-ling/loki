# Generated from Loki.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\30")
        buf.write("l\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\6\2%\n\2\r\2")
        buf.write("\16\2&\3\3\3\3\3\3\3\3\5\3-\n\3\3\4\3\4\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\7\5\7\67\n\7\3\7\3\7\3\b\3\b\3\b\5\b>\n\b\3\b")
        buf.write("\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\5\13K\n\13")
        buf.write("\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\5\rV\n\r\3\16\3\16")
        buf.write("\5\16Z\n\16\3\17\6\17]\n\17\r\17\16\17^\3\20\3\20\7\20")
        buf.write("c\n\20\f\20\16\20f\13\20\3\20\3\20\3\21\3\21\3\21\2\2")
        buf.write("\22\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \2\5\3\2\25")
        buf.write("\27\3\2\26\27\3\2\r\24\2g\2$\3\2\2\2\4,\3\2\2\2\6.\3\2")
        buf.write("\2\2\b\60\3\2\2\2\n\62\3\2\2\2\f\66\3\2\2\2\16:\3\2\2")
        buf.write("\2\20A\3\2\2\2\22D\3\2\2\2\24J\3\2\2\2\26L\3\2\2\2\30")
        buf.write("U\3\2\2\2\32Y\3\2\2\2\34\\\3\2\2\2\36`\3\2\2\2 i\3\2\2")
        buf.write("\2\"%\5\16\b\2#%\5\4\3\2$\"\3\2\2\2$#\3\2\2\2%&\3\2\2")
        buf.write("\2&$\3\2\2\2&\'\3\2\2\2\'\3\3\2\2\2(-\5\n\6\2)-\5\f\7")
        buf.write("\2*-\5\6\4\2+-\5\b\5\2,(\3\2\2\2,)\3\2\2\2,*\3\2\2\2,")
        buf.write("+\3\2\2\2-\5\3\2\2\2./\7\3\2\2/\7\3\2\2\2\60\61\7\4\2")
        buf.write("\2\61\t\3\2\2\2\62\63\7\13\2\2\63\64\5\24\13\2\64\13\3")
        buf.write("\2\2\2\65\67\7\f\2\2\66\65\3\2\2\2\66\67\3\2\2\2\678\3")
        buf.write("\2\2\289\5\24\13\29\r\3\2\2\2:=\7\5\2\2;>\5\22\n\2<>\5")
        buf.write("\20\t\2=;\3\2\2\2=<\3\2\2\2>?\3\2\2\2?@\7\6\2\2@\17\3")
        buf.write("\2\2\2AB\7\7\2\2BC\5\22\n\2C\21\3\2\2\2DE\5 \21\2EF\7")
        buf.write("\t\2\2FG\5\24\13\2G\23\3\2\2\2HK\5\26\f\2IK\5\30\r\2J")
        buf.write("H\3\2\2\2JI\3\2\2\2K\25\3\2\2\2LM\7\b\2\2MN\5\34\17\2")
        buf.write("NO\7\b\2\2O\27\3\2\2\2PQ\7\n\2\2QR\5\36\20\2RS\7\n\2\2")
        buf.write("SV\3\2\2\2TV\5\36\20\2UP\3\2\2\2UT\3\2\2\2V\31\3\2\2\2")
        buf.write("WZ\5\36\20\2XZ\5\34\17\2YW\3\2\2\2YX\3\2\2\2Z\33\3\2\2")
        buf.write("\2[]\t\2\2\2\\[\3\2\2\2]^\3\2\2\2^\\\3\2\2\2^_\3\2\2\2")
        buf.write("_\35\3\2\2\2`d\7\25\2\2ac\t\3\2\2ba\3\2\2\2cf\3\2\2\2")
        buf.write("db\3\2\2\2de\3\2\2\2eg\3\2\2\2fd\3\2\2\2gh\7\25\2\2h\37")
        buf.write("\3\2\2\2ij\t\4\2\2j!\3\2\2\2\f$&,\66=JUY^d")
        return buf.getvalue()


class LokiParser ( Parser ):

    grammarFileName = "Loki.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<<'", "'>>'", "'['", "']'", "'!'", "'/'", 
                     "'='", "'\"'", "'<'", "'>'", "'word'", "'lemma'", "'tag'", 
                     "'chunk'", "'entity'", "'mention'", "'incoming'", "'outgoing'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "OPEN_TC", 
                      "CLOSE_TC", "NEGATED", "SLASH", "EQUAL", "QUOTE", 
                      "INCOMING_DEP", "OUTGOING_DEP", "WORD", "LEMMA", "TAG", 
                      "CHUNK", "ENTITY", "MENTION", "INCOMING", "OUTGOING", 
                      "LETTER", "DIGIT", "PUNCT", "WHITESPACE" ]

    RULE_loki_pattern = 0
    RULE_graph_traversal = 1
    RULE_incoming_wildcard = 2
    RULE_outgoing_wildcard = 3
    RULE_incoming_traversal = 4
    RULE_outgoing_traversal = 5
    RULE_token_constraint = 6
    RULE_negated_attribute_constraint = 7
    RULE_attribute_constraint = 8
    RULE_pattern = 9
    RULE_pattern_regex = 10
    RULE_pattern_literal = 11
    RULE_inner_pattern = 12
    RULE_regex = 13
    RULE_literal = 14
    RULE_token_attribute = 15

    ruleNames =  [ "loki_pattern", "graph_traversal", "incoming_wildcard", 
                   "outgoing_wildcard", "incoming_traversal", "outgoing_traversal", 
                   "token_constraint", "negated_attribute_constraint", "attribute_constraint", 
                   "pattern", "pattern_regex", "pattern_literal", "inner_pattern", 
                   "regex", "literal", "token_attribute" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    OPEN_TC=3
    CLOSE_TC=4
    NEGATED=5
    SLASH=6
    EQUAL=7
    QUOTE=8
    INCOMING_DEP=9
    OUTGOING_DEP=10
    WORD=11
    LEMMA=12
    TAG=13
    CHUNK=14
    ENTITY=15
    MENTION=16
    INCOMING=17
    OUTGOING=18
    LETTER=19
    DIGIT=20
    PUNCT=21
    WHITESPACE=22

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class Loki_patternContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def token_constraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LokiParser.Token_constraintContext)
            else:
                return self.getTypedRuleContext(LokiParser.Token_constraintContext,i)


        def graph_traversal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LokiParser.Graph_traversalContext)
            else:
                return self.getTypedRuleContext(LokiParser.Graph_traversalContext,i)


        def getRuleIndex(self):
            return LokiParser.RULE_loki_pattern

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoki_pattern" ):
                listener.enterLoki_pattern(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoki_pattern" ):
                listener.exitLoki_pattern(self)




    def loki_pattern(self):

        localctx = LokiParser.Loki_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_loki_pattern)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 34
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [LokiParser.OPEN_TC]:
                    self.state = 32
                    self.token_constraint()
                    pass
                elif token in [LokiParser.T__0, LokiParser.T__1, LokiParser.SLASH, LokiParser.QUOTE, LokiParser.INCOMING_DEP, LokiParser.OUTGOING_DEP, LokiParser.LETTER]:
                    self.state = 33
                    self.graph_traversal()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 36 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LokiParser.T__0) | (1 << LokiParser.T__1) | (1 << LokiParser.OPEN_TC) | (1 << LokiParser.SLASH) | (1 << LokiParser.QUOTE) | (1 << LokiParser.INCOMING_DEP) | (1 << LokiParser.OUTGOING_DEP) | (1 << LokiParser.LETTER))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Graph_traversalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def incoming_traversal(self):
            return self.getTypedRuleContext(LokiParser.Incoming_traversalContext,0)


        def outgoing_traversal(self):
            return self.getTypedRuleContext(LokiParser.Outgoing_traversalContext,0)


        def incoming_wildcard(self):
            return self.getTypedRuleContext(LokiParser.Incoming_wildcardContext,0)


        def outgoing_wildcard(self):
            return self.getTypedRuleContext(LokiParser.Outgoing_wildcardContext,0)


        def getRuleIndex(self):
            return LokiParser.RULE_graph_traversal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGraph_traversal" ):
                listener.enterGraph_traversal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGraph_traversal" ):
                listener.exitGraph_traversal(self)




    def graph_traversal(self):

        localctx = LokiParser.Graph_traversalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_graph_traversal)
        try:
            self.state = 42
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LokiParser.INCOMING_DEP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.incoming_traversal()
                pass
            elif token in [LokiParser.SLASH, LokiParser.QUOTE, LokiParser.OUTGOING_DEP, LokiParser.LETTER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.outgoing_traversal()
                pass
            elif token in [LokiParser.T__0]:
                self.enterOuterAlt(localctx, 3)
                self.state = 40
                self.incoming_wildcard()
                pass
            elif token in [LokiParser.T__1]:
                self.enterOuterAlt(localctx, 4)
                self.state = 41
                self.outgoing_wildcard()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Incoming_wildcardContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LokiParser.RULE_incoming_wildcard

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIncoming_wildcard" ):
                listener.enterIncoming_wildcard(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIncoming_wildcard" ):
                listener.exitIncoming_wildcard(self)




    def incoming_wildcard(self):

        localctx = LokiParser.Incoming_wildcardContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_incoming_wildcard)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(LokiParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Outgoing_wildcardContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LokiParser.RULE_outgoing_wildcard

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOutgoing_wildcard" ):
                listener.enterOutgoing_wildcard(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOutgoing_wildcard" ):
                listener.exitOutgoing_wildcard(self)




    def outgoing_wildcard(self):

        localctx = LokiParser.Outgoing_wildcardContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_outgoing_wildcard)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(LokiParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Incoming_traversalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pattern(self):
            return self.getTypedRuleContext(LokiParser.PatternContext,0)


        def getRuleIndex(self):
            return LokiParser.RULE_incoming_traversal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIncoming_traversal" ):
                listener.enterIncoming_traversal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIncoming_traversal" ):
                listener.exitIncoming_traversal(self)




    def incoming_traversal(self):

        localctx = LokiParser.Incoming_traversalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_incoming_traversal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(LokiParser.INCOMING_DEP)
            self.state = 49
            self.pattern()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Outgoing_traversalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pattern(self):
            return self.getTypedRuleContext(LokiParser.PatternContext,0)


        def getRuleIndex(self):
            return LokiParser.RULE_outgoing_traversal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOutgoing_traversal" ):
                listener.enterOutgoing_traversal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOutgoing_traversal" ):
                listener.exitOutgoing_traversal(self)




    def outgoing_traversal(self):

        localctx = LokiParser.Outgoing_traversalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_outgoing_traversal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LokiParser.OUTGOING_DEP:
                self.state = 51
                self.match(LokiParser.OUTGOING_DEP)


            self.state = 54
            self.pattern()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Token_constraintContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_constraint(self):
            return self.getTypedRuleContext(LokiParser.Attribute_constraintContext,0)


        def negated_attribute_constraint(self):
            return self.getTypedRuleContext(LokiParser.Negated_attribute_constraintContext,0)


        def getRuleIndex(self):
            return LokiParser.RULE_token_constraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToken_constraint" ):
                listener.enterToken_constraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToken_constraint" ):
                listener.exitToken_constraint(self)




    def token_constraint(self):

        localctx = LokiParser.Token_constraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_token_constraint)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(LokiParser.OPEN_TC)
            self.state = 59
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LokiParser.WORD, LokiParser.LEMMA, LokiParser.TAG, LokiParser.CHUNK, LokiParser.ENTITY, LokiParser.MENTION, LokiParser.INCOMING, LokiParser.OUTGOING]:
                self.state = 57
                self.attribute_constraint()
                pass
            elif token in [LokiParser.NEGATED]:
                self.state = 58
                self.negated_attribute_constraint()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 61
            self.match(LokiParser.CLOSE_TC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Negated_attribute_constraintContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEGATED(self):
            return self.getToken(LokiParser.NEGATED, 0)

        def attribute_constraint(self):
            return self.getTypedRuleContext(LokiParser.Attribute_constraintContext,0)


        def getRuleIndex(self):
            return LokiParser.RULE_negated_attribute_constraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegated_attribute_constraint" ):
                listener.enterNegated_attribute_constraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegated_attribute_constraint" ):
                listener.exitNegated_attribute_constraint(self)




    def negated_attribute_constraint(self):

        localctx = LokiParser.Negated_attribute_constraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_negated_attribute_constraint)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(LokiParser.NEGATED)
            self.state = 64
            self.attribute_constraint()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Attribute_constraintContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def token_attribute(self):
            return self.getTypedRuleContext(LokiParser.Token_attributeContext,0)


        def EQUAL(self):
            return self.getToken(LokiParser.EQUAL, 0)

        def pattern(self):
            return self.getTypedRuleContext(LokiParser.PatternContext,0)


        def getRuleIndex(self):
            return LokiParser.RULE_attribute_constraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute_constraint" ):
                listener.enterAttribute_constraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute_constraint" ):
                listener.exitAttribute_constraint(self)




    def attribute_constraint(self):

        localctx = LokiParser.Attribute_constraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_attribute_constraint)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.token_attribute()
            self.state = 67
            self.match(LokiParser.EQUAL)
            self.state = 68
            self.pattern()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PatternContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pattern_regex(self):
            return self.getTypedRuleContext(LokiParser.Pattern_regexContext,0)


        def pattern_literal(self):
            return self.getTypedRuleContext(LokiParser.Pattern_literalContext,0)


        def getRuleIndex(self):
            return LokiParser.RULE_pattern

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPattern" ):
                listener.enterPattern(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPattern" ):
                listener.exitPattern(self)




    def pattern(self):

        localctx = LokiParser.PatternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_pattern)
        try:
            self.state = 72
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LokiParser.SLASH]:
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.pattern_regex()
                pass
            elif token in [LokiParser.QUOTE, LokiParser.LETTER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                self.pattern_literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Pattern_regexContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SLASH(self, i:int=None):
            if i is None:
                return self.getTokens(LokiParser.SLASH)
            else:
                return self.getToken(LokiParser.SLASH, i)

        def regex(self):
            return self.getTypedRuleContext(LokiParser.RegexContext,0)


        def getRuleIndex(self):
            return LokiParser.RULE_pattern_regex

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPattern_regex" ):
                listener.enterPattern_regex(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPattern_regex" ):
                listener.exitPattern_regex(self)




    def pattern_regex(self):

        localctx = LokiParser.Pattern_regexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_pattern_regex)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(LokiParser.SLASH)
            self.state = 75
            self.regex()
            self.state = 76
            self.match(LokiParser.SLASH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Pattern_literalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(LokiParser.QUOTE)
            else:
                return self.getToken(LokiParser.QUOTE, i)

        def literal(self):
            return self.getTypedRuleContext(LokiParser.LiteralContext,0)


        def getRuleIndex(self):
            return LokiParser.RULE_pattern_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPattern_literal" ):
                listener.enterPattern_literal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPattern_literal" ):
                listener.exitPattern_literal(self)




    def pattern_literal(self):

        localctx = LokiParser.Pattern_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_pattern_literal)
        try:
            self.state = 83
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LokiParser.QUOTE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.match(LokiParser.QUOTE)
                self.state = 79
                self.literal()
                self.state = 80
                self.match(LokiParser.QUOTE)
                pass
            elif token in [LokiParser.LETTER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 82
                self.literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Inner_patternContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(LokiParser.LiteralContext,0)


        def regex(self):
            return self.getTypedRuleContext(LokiParser.RegexContext,0)


        def getRuleIndex(self):
            return LokiParser.RULE_inner_pattern

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInner_pattern" ):
                listener.enterInner_pattern(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInner_pattern" ):
                listener.exitInner_pattern(self)




    def inner_pattern(self):

        localctx = LokiParser.Inner_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_inner_pattern)
        try:
            self.state = 87
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.regex()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RegexContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PUNCT(self, i:int=None):
            if i is None:
                return self.getTokens(LokiParser.PUNCT)
            else:
                return self.getToken(LokiParser.PUNCT, i)

        def LETTER(self, i:int=None):
            if i is None:
                return self.getTokens(LokiParser.LETTER)
            else:
                return self.getToken(LokiParser.LETTER, i)

        def DIGIT(self, i:int=None):
            if i is None:
                return self.getTokens(LokiParser.DIGIT)
            else:
                return self.getToken(LokiParser.DIGIT, i)

        def getRuleIndex(self):
            return LokiParser.RULE_regex

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRegex" ):
                listener.enterRegex(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRegex" ):
                listener.exitRegex(self)




    def regex(self):

        localctx = LokiParser.RegexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_regex)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 89
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LokiParser.LETTER) | (1 << LokiParser.DIGIT) | (1 << LokiParser.PUNCT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 92 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LokiParser.LETTER) | (1 << LokiParser.DIGIT) | (1 << LokiParser.PUNCT))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LETTER(self, i:int=None):
            if i is None:
                return self.getTokens(LokiParser.LETTER)
            else:
                return self.getToken(LokiParser.LETTER, i)

        def DIGIT(self, i:int=None):
            if i is None:
                return self.getTokens(LokiParser.DIGIT)
            else:
                return self.getToken(LokiParser.DIGIT, i)

        def PUNCT(self, i:int=None):
            if i is None:
                return self.getTokens(LokiParser.PUNCT)
            else:
                return self.getToken(LokiParser.PUNCT, i)

        def getRuleIndex(self):
            return LokiParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = LokiParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(LokiParser.LETTER)
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LokiParser.DIGIT or _la==LokiParser.PUNCT:
                self.state = 95
                _la = self._input.LA(1)
                if not(_la==LokiParser.DIGIT or _la==LokiParser.PUNCT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 101
            self.match(LokiParser.LETTER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Token_attributeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(LokiParser.WORD, 0)

        def LEMMA(self):
            return self.getToken(LokiParser.LEMMA, 0)

        def TAG(self):
            return self.getToken(LokiParser.TAG, 0)

        def CHUNK(self):
            return self.getToken(LokiParser.CHUNK, 0)

        def ENTITY(self):
            return self.getToken(LokiParser.ENTITY, 0)

        def MENTION(self):
            return self.getToken(LokiParser.MENTION, 0)

        def INCOMING(self):
            return self.getToken(LokiParser.INCOMING, 0)

        def OUTGOING(self):
            return self.getToken(LokiParser.OUTGOING, 0)

        def getRuleIndex(self):
            return LokiParser.RULE_token_attribute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToken_attribute" ):
                listener.enterToken_attribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToken_attribute" ):
                listener.exitToken_attribute(self)




    def token_attribute(self):

        localctx = LokiParser.Token_attributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_token_attribute)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LokiParser.WORD) | (1 << LokiParser.LEMMA) | (1 << LokiParser.TAG) | (1 << LokiParser.CHUNK) | (1 << LokiParser.ENTITY) | (1 << LokiParser.MENTION) | (1 << LokiParser.INCOMING) | (1 << LokiParser.OUTGOING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





