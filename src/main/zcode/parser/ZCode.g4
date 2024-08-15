grammar ZCode;

@lexer::header {
from lexererr import *
# ID: 2112897
}

options {
	language=Python3;
}

//2. Program structure
program: optional_newline program_line optional_newline EOF;
program_line: decl_list | stmt_list;
compulsory_newline: NEWLINE optional_newline | NEWLINE;
optional_newline: NEWLINE optional_newline | ;
decl_list: decl decl_list | decl;
//6. Variables and Function (Declarations)
decl: decl_type optional_newline;
decl_type: var_decl | func_decl;
///6.1 Variables
var_decl: explicit_decl | implicit_decl | array_decl;
explicit_decl: primitive_type IDENTIFIER (ASSIGN expr)?;
primitive_type: NUMBER | BOOL | STRING;
implicit_decl: implicit_var | implicit_dynamic;
implicit_var: VAR IDENTIFIER ASSIGN expr;
implicit_dynamic: DYNAMIC IDENTIFIER (ASSIGN expr)?;
array_decl: primitive_type IDENTIFIER size_decl (ASSIGN expr)?;
size_decl: LB size_list RB;
size_list: NUM_LIT tail_size | NUM_LIT;
tail_size: COMMA NUM_LIT tail_size | ;
///6.2 Function
func_decl: FUNC IDENTIFIER passed_para optional_newline body_func;
passed_para: LP para_list RP;
para_list: parameter tail_para | ;
tail_para: COMMA parameter tail_para | ;
parameter: primitive_type IDENTIFIER | primitive_type IDENTIFIER size_decl;
body_func: return_stmt | block_stmt | ;
//7. Statements
stmt_list: statement stmt_list | statement;
statement: stmt_type optional_newline;
stmt_type: var_decl | assign_stmt | if_stmt | for_stmt | return_stmt | func_call_stmt | block_stmt | break_stmt | continue_stmt;
///7.2 Assign statement
assign_stmt: lhs ASSIGN expr compulsory_newline;
lhs: IDENTIFIER | expr index_expr;
///7.3 If statement
//////////// Consider newline list between if, elif, else and expr, statement
// if_stmt: IF LP expr RP optional_newline stmt_type optional_newline else_part;
// else_part: elif_list | else_stmt | elif_list else_stmt | ;
// elif_list: elif_stmt elif_list | ;
// elif_stmt: ELIF LP expr RP optional_newline statement;
// else_stmt: ELSE optional_newline statement;
if_stmt: IF LP expr RP optional_newline stmt_type optional_newline elif_list else_stmt;
elif_list: elif_stmt elif_list | ;
elif_stmt: ELIF LP expr RP optional_newline statement;
else_stmt: ELSE optional_newline statement | ;
///7.4 For statement
//////////// Consider each expr
for_stmt: FOR IDENTIFIER UNTIL expr BY expr optional_newline statement;
///7.5 Break statement
break_stmt: BREAK compulsory_newline;
///7.6 Continue statement
continue_stmt: CONTINUE compulsory_newline;
///7.7 Return statement
return_stmt: RETURN expr | RETURN compulsory_newline;
///7.8 Function call statement
func_call_stmt: IDENTIFIER LP expr_list RP;
expr_list: expr tail_expr | ;
tail_expr: COMMA expr tail_expr | ;
///7.9 Block statement
block_stmt: BEGIN compulsory_newline body_block END compulsory_newline;
body_block: block_stmt_list | ;
block_stmt_list: statement block_stmt_list | statement;
//5. Expressions
///5.7 Operator precedence and associativity
expr: expr1 SPREAD_OP expr1 | expr1;
expr1: expr2 relational_op expr2 | expr2;
expr2: expr2 and_or expr3 | expr3;
expr3: expr3 add_subtr expr4 | expr4;
expr4: expr4 mul_div_rem expr5 | expr5;
expr5: NOT expr5 | expr6;
expr6: SUBTR_OP expr6 | expr7;
expr7: expr7 index_expr | expr8;
expr8: LP expr RP | operand;
operand: IDENTIFIER | literal | func_call_expr;
func_call_expr: IDENTIFIER LP expr_list RP;
///Literal
literal: NUM_LIT | TRUE | FALSE | STRING_LIT | array_lit;
array_lit: LB comp_expr_list RB;
comp_expr_list: expr tail_expr | expr;
///5.5 Index operator
index_expr: LB index_operator RB;
index_operator: expr | expr COMMA index_operator;
///Sign negation (5.1 Arithmetic operators)
///Negation (5.2 Logic operators)
///Multiplying (5.1 Arithmetic operators)
mul_div_rem: MUL_OP | DIV_OP | REMAINDER_OP;
///Adding (5.1 Arithmetic operators)
add_subtr: ADD_OP | SUBTR_OP;
///Conjunction & Disjunction (5.2 Logic operators)
and_or: AND | OR;
///5.4 Relational operators
relational_op: EQUAL | EQUAL_STR | NOT_EQUAL | SMALLER | GREATER | SMALLER_OR_EQUAL | GREATER_OR_EQUAL;

//3.1 Character set
WS : [ \t\b\f]+ -> skip ; // skip spaces, tab, form feed
NEWLINE: '\n' | '\r\n' {self.text = '\n';}; //also 3.6
//3.2 Program comment
COMMENT: '##' ~[\n]*-> skip;
//3.4 Keywords
TRUE: 'true';
FALSE: 'false';
NUMBER: 'number';
BOOL: 'bool';
STRING: 'string';
RETURN: 'return';
VAR: 'var';
DYNAMIC: 'dynamic';
FUNC: 'func';
FOR: 'for';
UNTIL: 'until';
BY: 'by';
BREAK: 'break';
CONTINUE: 'continue';
IF: 'if';
ELSE: 'else';
ELIF: 'elif';
BEGIN: 'begin';
END: 'end';
NOT: 'not'; // also 3.5
AND: 'and'; // also 3.5
OR: 'or'; // also 3.5
//3.5 Operators
ADD_OP: '+';
SUBTR_OP: '-';
MUL_OP: '*';
DIV_OP: '/';
REMAINDER_OP: '%';
EQUAL: '=';
ASSIGN: '<-';
NOT_EQUAL: '!=';
SMALLER: '<';
SMALLER_OR_EQUAL: '<=';
GREATER: '>';
GREATER_OR_EQUAL: '>=';
SPREAD_OP: '...';
EQUAL_STR: '==';
//3.6 Separators
LP: '(';
RP: ')';
LB: '[';
RB: ']';
COMMA: ',';
//3.7 Literals
///3.7.1 Number
fragment INT: [0-9]+;
fragment DEC: [.][0-9]*;
fragment EXP: [eE][+-]?[0-9]+;
NUM_LIT: INT DEC? EXP?;
///3.7.2 Boolean
BOOL_LIT: TRUE | FALSE;
///3.7.3 String
fragment DOUBLE_QUOTE: '"';
// fragment ESCAPE_SEQ: '\\' [bfrnt'\\];
// fragment QUOTE_STR: [']["];
// fragment CHAR: ~["\b\f\r\n\t\\]; 

fragment ESCAPE_SEQ: '\\' [bfrnt\\'];
fragment QUOTE_STR: [']["];
fragment CHAR: ~["\b\f\r\n\t\\];
//~[DOUBLE_QUOTE ESCAPE_SEQ QUOTE_STR];

STRING_LIT: DOUBLE_QUOTE (ESCAPE_SEQ | QUOTE_STR | CHAR)* DOUBLE_QUOTE {self.text = self.text[1:-1];};

////////////////////
///Lexical error///
//////////////////
// UNCLOSE_STRING: (DOUBLE_QUOTE (ESCAPE_SEQ | QUOTE_STR | CHAR)* NEWLINE* (ESCAPE_SEQ | QUOTE_STR | CHAR)* DOUBLE_QUOTE?)
UNCLOSE_STRING: (DOUBLE_QUOTE (ESCAPE_SEQ | QUOTE_STR | CHAR | NEWLINE)* DOUBLE_QUOTE?)
{
	if self.text.find('\n') != -1:
		print("newline error")
		raise UncloseString(self.text[1:(self.text.find('\n') - 1)])
	if self.text[-1] != '"':
		print(self.text[-1])
		print("double quote error")
		raise UncloseString(self.text[1:])
};
fragment ILLEGAL: '\\' ~[bfrnt\\'];
ILLEGAL_ESCAPE: DOUBLE_QUOTE (ESCAPE_SEQ | QUOTE_STR | CHAR | ILLEGAL)* DOUBLE_QUOTE{
	illegal = '\\'
	index = self.text.find(illegal)
	start = 0
	while (start < len(self.text) - 1) and (index != -1) and (index + 1 < len(self.text) - 1):
		if (self.text[index + 1] != 'b') and (self.text[index + 1] != 'f') and (self.text[index + 1] != 'r') and (self.text[index + 1] != 'n') and (self.text[index + 1] != 't') and (self.text[index + 1] != '\\') and (self.text[index + 1] != '\''): 
			index += 2
			break
		start = index + 1
		index = self.text.find(illegal, start)
	raise IllegalEscape(self.text[1:index])
};

//3.3 Identifiers
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;

ERROR_CHAR: . {raise ErrorToken(self.text)};
