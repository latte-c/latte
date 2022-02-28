grammar Latte;

WHITESPACE: [ \r\t\n]+ -> skip;
COMMENT: '//' ~[\r\n]* -> skip;

IMPORT: 'import';
PROCEDURE: 'procedure';
EXPORT: 'export';
ARRAY: 'array';
INT: 'int';
REAL: 'real';
IF: 'if';
ELSE: 'else';
LOOP: 'loop';
BREAK: 'break';
CONTINUE: 'continue';
RETURN: 'return';

fragment DEC_CONST: [1-9][0-9]* | '0';
fragment OCT_CONST: ('0o' | '0O') [0-7]+;
fragment HEX_CONST: ('0x' | '0X') [0-9a-fA-F]+;

INT_CONST: DEC_CONST | OCT_CONST | HEX_CONST;

REAL_CONST:
	[0-9]+ '.' [0-9]+ (('e' | 'E') ('+' | '-')? DEC_CONST)?;

IDENTIFIER: [_a-zA-Z][_a-zA-Z0-9]*;

fragment ESC_SEQUENCE:
	'\\' (
		'\\'
		| '"'
		| '?'
		| '\''
		| 'a'
		| 'b'
		| 'f'
		| 'n'
		| 'r'
		| 't'
		| 'v'
	);

fragment CCHAR: ~['\\\r\n] | ESC_SEQUENCE;

CHAR_CONST: '\'' CCHAR '\'';
STRING_CONST: '"' CCHAR* '"';

compilationUnit: importDeclaration* topDeclaration* EOF;

importDeclaration: IMPORT IDENTIFIER ('.' IDENTIFIER)* ';';

topDeclaration: varDeclaration | procedureDeclaration;

varDeclaration: EXPORT? latteType IDENTIFIER ('=' expression)?;

procedureDeclaration:
	EXPORT? PROCEDURE latteType IDENTIFIER '(' (
		procedureArgument (',' procedureArgument)*
	)? ')' '{' statement* '}';

procedureArgument: latteType IDENTIFIER;

statement:
	blockStatement
	| ifStatement
	| loopStatement
	| breakStatement
	| continueStatement
	| returnStatement
	| expressionStatement
	| assignStatement
	| returnStatement
	| varStatement;

blockStatement: '{' statement* '}';

ifStatement: IF '(' expression ')' statement (ELSE statement)?;

loopStatement: (IDENTIFIER ':')? LOOP statement;

breakStatement: BREAK IDENTIFIER? ';';

continueStatement: CONTINUE IDENTIFIER? ';';

returnStatement: 'return' expression ';';

expressionStatement: expression ';';

assignStatement: accessExpression '=' expression ';';

varStatement:
	latteType varInitialization (',' varInitialization)* ';';

varInitialization: IDENTIFIER ('=' expression)?;

expression:
	op = ('-' | '!') expression								# unaryExpr
	| expression op = ('*' | '/') expression				# binaryMulExpr
	| expression op = ('+' | '-') expression				# binaryAddExpr
	| expression op = ('%' | '@') expression				# binaryModExpr
	| expression op = ('>' | '<' | '>=' | '<=') expression	# binaryCompExpr
	| expression op = ('==' | '!=') expression				# binaryEqExpr
	| expression '&&' expression							# binaryAndExpr
	| expression '||' expression							# binaryOrExpr
	| '(' expression ')'									# parenExpr
	| '{' expression (',' expression)* '}'					# arrayExpr
	| IDENTIFIER '(' (expression (',' expression)*)? ')'	# callExpr
	| accessExpression										# accessExpr
	| INT_CONST												# intConstExpr
	| REAL_CONST											# realConstExpr
	| CHAR_CONST											# charConstExpr
	| STRING_CONST											# stringConstExpr;

accessExpression:
	IDENTIFIER ('[' expression (',' expression)* ']')?;

latteType:
	nativeType '(' INT_CONST ')' (ARRAY '(' arrayShape ')')?;

nativeType: INT | REAL;

arrayShape: '*' | INT_CONST (',' INT_CONST)*;