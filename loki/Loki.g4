grammar Loki;

/*
 * loki parser Rules
 */
loki_pattern
  : (surface_pattern | graph_traversal)+ ;

/*
 * graph-based traversal patterns
 */
graph_traversal
  : incoming_traversal | outgoing_traversal | incoming_wildcard | outgoing_wildcard ;

incoming_wildcard
  : '<<' ;

outgoing_wildcard
  : '>>' ;

incoming_traversal
  : '<' pattern ;

outgoing_traversal
  : '>' pattern ;

/*
 * token constraints
 */

surface_pattern
  : token_wildcard | token_constraint ;

token_wildcard
  : '[' WHITESPACE? ']' ;

token_constraint
  : '[' (attribute_constraint | negated_attribute_constraint) ']' ;

negated_attribute_constraint
  : NEGATED attribute_constraint ;

attribute_constraint
  : token_attribute EQUAL pattern ;

pattern
  : pattern_regex | pattern_literal ;

pattern_regex
  : SLASH regex SLASH ;

pattern_literal
  : (QUOTE literal QUOTE) | literal ;

inner_pattern
  : literal | regex ;

regex
  : (PUNCT | LETTER | DIGIT)+ ;

literal
  : LETTER (DIGIT | PUNCT)* LETTER ;

token_attribute
  : (WORD | LEMMA | TAG | CHUNK | ENTITY | MENTION | INCOMING | OUTGOING) ;

/*
 * loki lexer rules
 */

OPEN_TC
  : '[' ;
CLOSE_TC
  : ']' ;

NEGATED
  : '!' ;

SLASH
  : '/' ;

EQUAL
  : '=' ;

QUOTE
  : '"' ;

INCOMING_DEP
  : '<' ;
OUTGOING_DEP
  : '>' ;

WORD
  : 'word' ;
LEMMA
  : 'lemma' ;
TAG
  : 'tag' ;
CHUNK
  : 'chunk' ;
ENTITY
  : 'entity' ;
MENTION
  : 'mention' ;
INCOMING
  : 'incoming' ;
OUTGOING
  : 'outgoing' ;

LETTER
  : [a-zA-Z]+ ;

DIGIT
  : [0-9]+ ;

PUNCT
  : '.'|','|':'|'_'|';'|'?'|NEGATED|'-'|'^'|'$'|'*'|'+'|OPEN_TC|CLOSE_TC|'('|')'|'%'|'"'+ ;

WHITESPACE
  : [ \t\r\n]+ -> skip ;
