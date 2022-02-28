grammar Latte;

@header {
    package latte.front;
}

Whitespace: [ \r\t\n]+ -> skip;
LineComment: '//' ~[\r\n]* -> skip;

Import: 'import';
Var: 'var';
Define: 'define';
Declare: 'declare';
Array: 'array';
Int: 'int';
Real: 'real';
If: 'if';
Else: 'else';
Loop: 'loop';
Break: 'break';
Continue: 'continue';
Return: 'return';

fragment DecConst: [1-9][0-9]* | '0';
fragment OctConst: ('0o' | '0O') [0-7]+;
fragment HexConst: ('0x' | '0X') [0-9a-fA-F]+;

IntConst: DecConst | OctConst | HexConst;

RealConst:
	[0-9]+ '.' [0-9]+ (('e' | 'E') ('+' | '-')? DecConst)?;

Identifier: [_a-zA-Z][_a-zA-Z0-9]*; 

fragment EscapeSequence:
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

fragment CChar: ~['\\\r\n] | EscapeSequence;

CharConst: '\'' CChar '\'';
StringConst: '"' CChar* '"';

compilationUnit: importDeclaration* topDeclaration* EOF;

importDeclaration: Import Identifier ('.' Identifier)* ';';

topDeclaration:
	generalVarDeclaration
	| generalVarDefinition
	| functionDeclaration
	| functionDefinition;

generalVarDeclaration:
	Declare varDeclaration (',' varDeclaration)* ';';

generalVarDefinition:
	Define varInitialization (',' varInitialization)* ';';

varDeclaration: type Identifier;

varInitialization: varDeclaration ('=' expression)?;

functionDeclaration: Declare functionSignature;

functionDefinition: Define functionSignature '{' statement* '}';

functionSignature: type Identifier '(' functionArguments? ')';

functionArguments: functionArgument (',' functionArgument)*;

functionArgument: type Identifier;

statement:
	blockStatement
	| ifStatement
	| loopStatement
	| breakStatement
	| continueStatement
	| returnStatement
	| functionCallStatement
	| assignStatement
	| returnStatement
	| varStatement;

blockStatement: '{' statement* '}';

ifStatement:
	If '(' expression ')' ifBranch = statement (
		Else elseBranch = statement
	)?;

loopStatement: Loop '(' Identifier ')' statement;

breakStatement: Break Identifier ';';

continueStatement: Continue Identifier ';';

returnStatement: 'return' expression ';';

functionCallStatement: functionCallExpression ';';

assignStatement: postfixExpression '=' expression ';';

varStatement: generalVarDeclaration | generalVarDefinition;

expression:
	expression ('*' | '/') expression
	| functionCallExpression
	| postfixExpression
	| constExpression;

functionCallExpression:
	Identifier '(' (expression (',' expression)*)? ')';

postfixExpression:
	Identifier ('[' expression (',' expression)* ']')?;

constExpression: IntConst | RealConst | CharConst | StringConst;

type: nativeType '(' IntConst ')' (Array '(' arrayShape ')')?;

nativeType: Int | Real;

arrayShape: '*' | IntConst (',' IntConst)*;