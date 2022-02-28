# Generated from latte/front/parser/Latte.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3/")
        buf.write("\u0126\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\3\2\7\2\60\n")
        buf.write("\2\f\2\16\2\63\13\2\3\2\7\2\66\n\2\f\2\16\29\13\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\7\3A\n\3\f\3\16\3D\13\3\3\3\3\3\3")
        buf.write("\4\3\4\5\4J\n\4\3\5\5\5M\n\5\3\5\3\5\3\5\3\5\5\5S\n\5")
        buf.write("\3\6\5\6V\n\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\7\6_\n\6\f\6")
        buf.write("\16\6b\13\6\5\6d\n\6\3\6\3\6\3\6\7\6i\n\6\f\6\16\6l\13")
        buf.write("\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\5\b}\n\b\3\t\3\t\7\t\u0081\n\t\f\t\16\t\u0084")
        buf.write("\13\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u008f\n")
        buf.write("\n\3\13\3\13\5\13\u0093\n\13\3\13\3\13\3\13\3\f\3\f\5")
        buf.write("\f\u009a\n\f\3\f\3\f\3\r\3\r\5\r\u00a0\n\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\7\21\u00b4\n\21\f\21\16\21\u00b7")
        buf.write("\13\21\3\21\3\21\3\22\3\22\3\22\5\22\u00be\n\22\3\23\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\7\23")
        buf.write("\u00cb\n\23\f\23\16\23\u00ce\13\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\7\23\u00d7\n\23\f\23\16\23\u00da\13\23")
        buf.write("\5\23\u00dc\n\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u00e4")
        buf.write("\n\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\7\23\u00fb\n\23\f\23\16\23\u00fe\13\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\7\24\u0105\n\24\f\24\16\24\u0108\13\24\3\24")
        buf.write("\3\24\5\24\u010c\n\24\3\25\3\25\3\25\3\25\3\25\3\25\3")
        buf.write("\25\3\25\3\25\5\25\u0117\n\25\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\7\27\u011f\n\27\f\27\16\27\u0122\13\27\5\27\u0124")
        buf.write("\n\27\3\27\2\3$\30\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&(*,\2\t\3\2\f\r\3\2\16\17\4\2\f\f\20\20\3\2\21")
        buf.write("\22\3\2\23\26\3\2\27\30\3\2#$\2\u0140\2\61\3\2\2\2\4<")
        buf.write("\3\2\2\2\6I\3\2\2\2\bL\3\2\2\2\nU\3\2\2\2\fo\3\2\2\2\16")
        buf.write("|\3\2\2\2\20~\3\2\2\2\22\u0087\3\2\2\2\24\u0092\3\2\2")
        buf.write("\2\26\u0097\3\2\2\2\30\u009d\3\2\2\2\32\u00a3\3\2\2\2")
        buf.write("\34\u00a7\3\2\2\2\36\u00aa\3\2\2\2 \u00af\3\2\2\2\"\u00ba")
        buf.write("\3\2\2\2$\u00e3\3\2\2\2&\u00ff\3\2\2\2(\u010d\3\2\2\2")
        buf.write("*\u0118\3\2\2\2,\u0123\3\2\2\2.\60\5\4\3\2/.\3\2\2\2\60")
        buf.write("\63\3\2\2\2\61/\3\2\2\2\61\62\3\2\2\2\62\67\3\2\2\2\63")
        buf.write("\61\3\2\2\2\64\66\5\6\4\2\65\64\3\2\2\2\669\3\2\2\2\67")
        buf.write("\65\3\2\2\2\678\3\2\2\28:\3\2\2\29\67\3\2\2\2:;\7\2\2")
        buf.write("\3;\3\3\2\2\2<=\7\37\2\2=B\7-\2\2>?\7\3\2\2?A\7-\2\2@")
        buf.write(">\3\2\2\2AD\3\2\2\2B@\3\2\2\2BC\3\2\2\2CE\3\2\2\2DB\3")
        buf.write("\2\2\2EF\7\4\2\2F\5\3\2\2\2GJ\5\b\5\2HJ\5\n\6\2IG\3\2")
        buf.write("\2\2IH\3\2\2\2J\7\3\2\2\2KM\7!\2\2LK\3\2\2\2LM\3\2\2\2")
        buf.write("MN\3\2\2\2NO\5(\25\2OR\7-\2\2PQ\7\5\2\2QS\5$\23\2RP\3")
        buf.write("\2\2\2RS\3\2\2\2S\t\3\2\2\2TV\7!\2\2UT\3\2\2\2UV\3\2\2")
        buf.write("\2VW\3\2\2\2WX\7 \2\2XY\5(\25\2YZ\7-\2\2Zc\7\6\2\2[`\5")
        buf.write("\f\7\2\\]\7\7\2\2]_\5\f\7\2^\\\3\2\2\2_b\3\2\2\2`^\3\2")
        buf.write("\2\2`a\3\2\2\2ad\3\2\2\2b`\3\2\2\2c[\3\2\2\2cd\3\2\2\2")
        buf.write("de\3\2\2\2ef\7\b\2\2fj\7\t\2\2gi\5\16\b\2hg\3\2\2\2il")
        buf.write("\3\2\2\2jh\3\2\2\2jk\3\2\2\2km\3\2\2\2lj\3\2\2\2mn\7\n")
        buf.write("\2\2n\13\3\2\2\2op\5(\25\2pq\7-\2\2q\r\3\2\2\2r}\5\20")
        buf.write("\t\2s}\5\22\n\2t}\5\24\13\2u}\5\26\f\2v}\5\30\r\2w}\5")
        buf.write("\32\16\2x}\5\34\17\2y}\5\36\20\2z}\5\32\16\2{}\5 \21\2")
        buf.write("|r\3\2\2\2|s\3\2\2\2|t\3\2\2\2|u\3\2\2\2|v\3\2\2\2|w\3")
        buf.write("\2\2\2|x\3\2\2\2|y\3\2\2\2|z\3\2\2\2|{\3\2\2\2}\17\3\2")
        buf.write("\2\2~\u0082\7\t\2\2\177\u0081\5\16\b\2\u0080\177\3\2\2")
        buf.write("\2\u0081\u0084\3\2\2\2\u0082\u0080\3\2\2\2\u0082\u0083")
        buf.write("\3\2\2\2\u0083\u0085\3\2\2\2\u0084\u0082\3\2\2\2\u0085")
        buf.write("\u0086\7\n\2\2\u0086\21\3\2\2\2\u0087\u0088\7%\2\2\u0088")
        buf.write("\u0089\7\6\2\2\u0089\u008a\5$\23\2\u008a\u008b\7\b\2\2")
        buf.write("\u008b\u008e\5\16\b\2\u008c\u008d\7&\2\2\u008d\u008f\5")
        buf.write("\16\b\2\u008e\u008c\3\2\2\2\u008e\u008f\3\2\2\2\u008f")
        buf.write("\23\3\2\2\2\u0090\u0091\7-\2\2\u0091\u0093\7\13\2\2\u0092")
        buf.write("\u0090\3\2\2\2\u0092\u0093\3\2\2\2\u0093\u0094\3\2\2\2")
        buf.write("\u0094\u0095\7\'\2\2\u0095\u0096\5\16\b\2\u0096\25\3\2")
        buf.write("\2\2\u0097\u0099\7(\2\2\u0098\u009a\7-\2\2\u0099\u0098")
        buf.write("\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u009b\3\2\2\2\u009b")
        buf.write("\u009c\7\4\2\2\u009c\27\3\2\2\2\u009d\u009f\7)\2\2\u009e")
        buf.write("\u00a0\7-\2\2\u009f\u009e\3\2\2\2\u009f\u00a0\3\2\2\2")
        buf.write("\u00a0\u00a1\3\2\2\2\u00a1\u00a2\7\4\2\2\u00a2\31\3\2")
        buf.write("\2\2\u00a3\u00a4\7*\2\2\u00a4\u00a5\5$\23\2\u00a5\u00a6")
        buf.write("\7\4\2\2\u00a6\33\3\2\2\2\u00a7\u00a8\5$\23\2\u00a8\u00a9")
        buf.write("\7\4\2\2\u00a9\35\3\2\2\2\u00aa\u00ab\5&\24\2\u00ab\u00ac")
        buf.write("\7\5\2\2\u00ac\u00ad\5$\23\2\u00ad\u00ae\7\4\2\2\u00ae")
        buf.write("\37\3\2\2\2\u00af\u00b0\5(\25\2\u00b0\u00b5\5\"\22\2\u00b1")
        buf.write("\u00b2\7\7\2\2\u00b2\u00b4\5\"\22\2\u00b3\u00b1\3\2\2")
        buf.write("\2\u00b4\u00b7\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b5\u00b6")
        buf.write("\3\2\2\2\u00b6\u00b8\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b8")
        buf.write("\u00b9\7\4\2\2\u00b9!\3\2\2\2\u00ba\u00bd\7-\2\2\u00bb")
        buf.write("\u00bc\7\5\2\2\u00bc\u00be\5$\23\2\u00bd\u00bb\3\2\2\2")
        buf.write("\u00bd\u00be\3\2\2\2\u00be#\3\2\2\2\u00bf\u00c0\b\23\1")
        buf.write("\2\u00c0\u00c1\t\2\2\2\u00c1\u00e4\5$\23\22\u00c2\u00c3")
        buf.write("\7\6\2\2\u00c3\u00c4\5$\23\2\u00c4\u00c5\7\b\2\2\u00c5")
        buf.write("\u00e4\3\2\2\2\u00c6\u00c7\7\t\2\2\u00c7\u00cc\5$\23\2")
        buf.write("\u00c8\u00c9\7\7\2\2\u00c9\u00cb\5$\23\2\u00ca\u00c8\3")
        buf.write("\2\2\2\u00cb\u00ce\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cc\u00cd")
        buf.write("\3\2\2\2\u00cd\u00cf\3\2\2\2\u00ce\u00cc\3\2\2\2\u00cf")
        buf.write("\u00d0\7\n\2\2\u00d0\u00e4\3\2\2\2\u00d1\u00d2\7-\2\2")
        buf.write("\u00d2\u00db\7\6\2\2\u00d3\u00d8\5$\23\2\u00d4\u00d5\7")
        buf.write("\7\2\2\u00d5\u00d7\5$\23\2\u00d6\u00d4\3\2\2\2\u00d7\u00da")
        buf.write("\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9")
        buf.write("\u00dc\3\2\2\2\u00da\u00d8\3\2\2\2\u00db\u00d3\3\2\2\2")
        buf.write("\u00db\u00dc\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00e4\7")
        buf.write("\b\2\2\u00de\u00e4\5&\24\2\u00df\u00e4\7+\2\2\u00e0\u00e4")
        buf.write("\7,\2\2\u00e1\u00e4\7.\2\2\u00e2\u00e4\7/\2\2\u00e3\u00bf")
        buf.write("\3\2\2\2\u00e3\u00c2\3\2\2\2\u00e3\u00c6\3\2\2\2\u00e3")
        buf.write("\u00d1\3\2\2\2\u00e3\u00de\3\2\2\2\u00e3\u00df\3\2\2\2")
        buf.write("\u00e3\u00e0\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e3\u00e2\3")
        buf.write("\2\2\2\u00e4\u00fc\3\2\2\2\u00e5\u00e6\f\21\2\2\u00e6")
        buf.write("\u00e7\t\3\2\2\u00e7\u00fb\5$\23\22\u00e8\u00e9\f\20\2")
        buf.write("\2\u00e9\u00ea\t\4\2\2\u00ea\u00fb\5$\23\21\u00eb\u00ec")
        buf.write("\f\17\2\2\u00ec\u00ed\t\5\2\2\u00ed\u00fb\5$\23\20\u00ee")
        buf.write("\u00ef\f\16\2\2\u00ef\u00f0\t\6\2\2\u00f0\u00fb\5$\23")
        buf.write("\17\u00f1\u00f2\f\r\2\2\u00f2\u00f3\t\7\2\2\u00f3\u00fb")
        buf.write("\5$\23\16\u00f4\u00f5\f\f\2\2\u00f5\u00f6\7\31\2\2\u00f6")
        buf.write("\u00fb\5$\23\r\u00f7\u00f8\f\13\2\2\u00f8\u00f9\7\32\2")
        buf.write("\2\u00f9\u00fb\5$\23\f\u00fa\u00e5\3\2\2\2\u00fa\u00e8")
        buf.write("\3\2\2\2\u00fa\u00eb\3\2\2\2\u00fa\u00ee\3\2\2\2\u00fa")
        buf.write("\u00f1\3\2\2\2\u00fa\u00f4\3\2\2\2\u00fa\u00f7\3\2\2\2")
        buf.write("\u00fb\u00fe\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fc\u00fd\3")
        buf.write("\2\2\2\u00fd%\3\2\2\2\u00fe\u00fc\3\2\2\2\u00ff\u010b")
        buf.write("\7-\2\2\u0100\u0101\7\33\2\2\u0101\u0106\5$\23\2\u0102")
        buf.write("\u0103\7\7\2\2\u0103\u0105\5$\23\2\u0104\u0102\3\2\2\2")
        buf.write("\u0105\u0108\3\2\2\2\u0106\u0104\3\2\2\2\u0106\u0107\3")
        buf.write("\2\2\2\u0107\u0109\3\2\2\2\u0108\u0106\3\2\2\2\u0109\u010a")
        buf.write("\7\34\2\2\u010a\u010c\3\2\2\2\u010b\u0100\3\2\2\2\u010b")
        buf.write("\u010c\3\2\2\2\u010c\'\3\2\2\2\u010d\u010e\5*\26\2\u010e")
        buf.write("\u010f\7\6\2\2\u010f\u0110\7+\2\2\u0110\u0116\7\b\2\2")
        buf.write("\u0111\u0112\7\"\2\2\u0112\u0113\7\6\2\2\u0113\u0114\5")
        buf.write(",\27\2\u0114\u0115\7\b\2\2\u0115\u0117\3\2\2\2\u0116\u0111")
        buf.write("\3\2\2\2\u0116\u0117\3\2\2\2\u0117)\3\2\2\2\u0118\u0119")
        buf.write("\t\b\2\2\u0119+\3\2\2\2\u011a\u0124\7\16\2\2\u011b\u0120")
        buf.write("\7+\2\2\u011c\u011d\7\7\2\2\u011d\u011f\7+\2\2\u011e\u011c")
        buf.write("\3\2\2\2\u011f\u0122\3\2\2\2\u0120\u011e\3\2\2\2\u0120")
        buf.write("\u0121\3\2\2\2\u0121\u0124\3\2\2\2\u0122\u0120\3\2\2\2")
        buf.write("\u0123\u011a\3\2\2\2\u0123\u011b\3\2\2\2\u0124-\3\2\2")
        buf.write("\2\37\61\67BILRU`cj|\u0082\u008e\u0092\u0099\u009f\u00b5")
        buf.write("\u00bd\u00cc\u00d8\u00db\u00e3\u00fa\u00fc\u0106\u010b")
        buf.write("\u0116\u0120\u0123")
        return buf.getvalue()


class LatteParser ( Parser ):

    grammarFileName = "Latte.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'.'", "';'", "'='", "'('", "','", "')'", 
                     "'{'", "'}'", "':'", "'-'", "'!'", "'*'", "'/'", "'+'", 
                     "'%'", "'@'", "'>'", "'<'", "'>='", "'<='", "'=='", 
                     "'!='", "'&&'", "'||'", "'['", "']'", "<INVALID>", 
                     "<INVALID>", "'import'", "'procedure'", "'export'", 
                     "'array'", "'int'", "'real'", "'if'", "'else'", "'loop'", 
                     "'break'", "'continue'", "'return'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "WHITESPACE", 
                      "COMMENT", "IMPORT", "PROCEDURE", "EXPORT", "ARRAY", 
                      "INT", "REAL", "IF", "ELSE", "LOOP", "BREAK", "CONTINUE", 
                      "RETURN", "INT_CONST", "REAL_CONST", "IDENTIFIER", 
                      "CHAR_CONST", "STRING_CONST" ]

    RULE_compilationUnit = 0
    RULE_importDeclaration = 1
    RULE_topDeclaration = 2
    RULE_varDeclaration = 3
    RULE_procedureDeclaration = 4
    RULE_procedureArgument = 5
    RULE_statement = 6
    RULE_blockStatement = 7
    RULE_ifStatement = 8
    RULE_loopStatement = 9
    RULE_breakStatement = 10
    RULE_continueStatement = 11
    RULE_returnStatement = 12
    RULE_expressionStatement = 13
    RULE_assignStatement = 14
    RULE_varStatement = 15
    RULE_varInitialization = 16
    RULE_expression = 17
    RULE_accessExpression = 18
    RULE_latteType = 19
    RULE_nativeType = 20
    RULE_arrayShape = 21

    ruleNames =  [ "compilationUnit", "importDeclaration", "topDeclaration", 
                   "varDeclaration", "procedureDeclaration", "procedureArgument", 
                   "statement", "blockStatement", "ifStatement", "loopStatement", 
                   "breakStatement", "continueStatement", "returnStatement", 
                   "expressionStatement", "assignStatement", "varStatement", 
                   "varInitialization", "expression", "accessExpression", 
                   "latteType", "nativeType", "arrayShape" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    WHITESPACE=27
    COMMENT=28
    IMPORT=29
    PROCEDURE=30
    EXPORT=31
    ARRAY=32
    INT=33
    REAL=34
    IF=35
    ELSE=36
    LOOP=37
    BREAK=38
    CONTINUE=39
    RETURN=40
    INT_CONST=41
    REAL_CONST=42
    IDENTIFIER=43
    CHAR_CONST=44
    STRING_CONST=45

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CompilationUnitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(LatteParser.EOF, 0)

        def importDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatteParser.ImportDeclarationContext)
            else:
                return self.getTypedRuleContext(LatteParser.ImportDeclarationContext,i)


        def topDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatteParser.TopDeclarationContext)
            else:
                return self.getTypedRuleContext(LatteParser.TopDeclarationContext,i)


        def getRuleIndex(self):
            return LatteParser.RULE_compilationUnit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompilationUnit" ):
                return visitor.visitCompilationUnit(self)
            else:
                return visitor.visitChildren(self)




    def compilationUnit(self):

        localctx = LatteParser.CompilationUnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_compilationUnit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LatteParser.IMPORT:
                self.state = 44
                self.importDeclaration()
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LatteParser.PROCEDURE) | (1 << LatteParser.EXPORT) | (1 << LatteParser.INT) | (1 << LatteParser.REAL))) != 0):
                self.state = 50
                self.topDeclaration()
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 56
            self.match(LatteParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImportDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPORT(self):
            return self.getToken(LatteParser.IMPORT, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(LatteParser.IDENTIFIER)
            else:
                return self.getToken(LatteParser.IDENTIFIER, i)

        def getRuleIndex(self):
            return LatteParser.RULE_importDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImportDeclaration" ):
                return visitor.visitImportDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def importDeclaration(self):

        localctx = LatteParser.ImportDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_importDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(LatteParser.IMPORT)
            self.state = 59
            self.match(LatteParser.IDENTIFIER)
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LatteParser.T__0:
                self.state = 60
                self.match(LatteParser.T__0)
                self.state = 61
                self.match(LatteParser.IDENTIFIER)
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 67
            self.match(LatteParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TopDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDeclaration(self):
            return self.getTypedRuleContext(LatteParser.VarDeclarationContext,0)


        def procedureDeclaration(self):
            return self.getTypedRuleContext(LatteParser.ProcedureDeclarationContext,0)


        def getRuleIndex(self):
            return LatteParser.RULE_topDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTopDeclaration" ):
                return visitor.visitTopDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def topDeclaration(self):

        localctx = LatteParser.TopDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_topDeclaration)
        try:
            self.state = 71
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                self.varDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.procedureDeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def latteType(self):
            return self.getTypedRuleContext(LatteParser.LatteTypeContext,0)


        def IDENTIFIER(self):
            return self.getToken(LatteParser.IDENTIFIER, 0)

        def EXPORT(self):
            return self.getToken(LatteParser.EXPORT, 0)

        def expression(self):
            return self.getTypedRuleContext(LatteParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LatteParser.RULE_varDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDeclaration" ):
                return visitor.visitVarDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def varDeclaration(self):

        localctx = LatteParser.VarDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_varDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LatteParser.EXPORT:
                self.state = 73
                self.match(LatteParser.EXPORT)


            self.state = 76
            self.latteType()
            self.state = 77
            self.match(LatteParser.IDENTIFIER)
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LatteParser.T__2:
                self.state = 78
                self.match(LatteParser.T__2)
                self.state = 79
                self.expression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProcedureDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROCEDURE(self):
            return self.getToken(LatteParser.PROCEDURE, 0)

        def latteType(self):
            return self.getTypedRuleContext(LatteParser.LatteTypeContext,0)


        def IDENTIFIER(self):
            return self.getToken(LatteParser.IDENTIFIER, 0)

        def EXPORT(self):
            return self.getToken(LatteParser.EXPORT, 0)

        def procedureArgument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatteParser.ProcedureArgumentContext)
            else:
                return self.getTypedRuleContext(LatteParser.ProcedureArgumentContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatteParser.StatementContext)
            else:
                return self.getTypedRuleContext(LatteParser.StatementContext,i)


        def getRuleIndex(self):
            return LatteParser.RULE_procedureDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcedureDeclaration" ):
                return visitor.visitProcedureDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def procedureDeclaration(self):

        localctx = LatteParser.ProcedureDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_procedureDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LatteParser.EXPORT:
                self.state = 82
                self.match(LatteParser.EXPORT)


            self.state = 85
            self.match(LatteParser.PROCEDURE)
            self.state = 86
            self.latteType()
            self.state = 87
            self.match(LatteParser.IDENTIFIER)
            self.state = 88
            self.match(LatteParser.T__3)
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LatteParser.INT or _la==LatteParser.REAL:
                self.state = 89
                self.procedureArgument()
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==LatteParser.T__4:
                    self.state = 90
                    self.match(LatteParser.T__4)
                    self.state = 91
                    self.procedureArgument()
                    self.state = 96
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 99
            self.match(LatteParser.T__5)
            self.state = 100
            self.match(LatteParser.T__6)
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LatteParser.T__3) | (1 << LatteParser.T__6) | (1 << LatteParser.T__9) | (1 << LatteParser.T__10) | (1 << LatteParser.INT) | (1 << LatteParser.REAL) | (1 << LatteParser.IF) | (1 << LatteParser.LOOP) | (1 << LatteParser.BREAK) | (1 << LatteParser.CONTINUE) | (1 << LatteParser.RETURN) | (1 << LatteParser.INT_CONST) | (1 << LatteParser.REAL_CONST) | (1 << LatteParser.IDENTIFIER) | (1 << LatteParser.CHAR_CONST) | (1 << LatteParser.STRING_CONST))) != 0):
                self.state = 101
                self.statement()
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 107
            self.match(LatteParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProcedureArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def latteType(self):
            return self.getTypedRuleContext(LatteParser.LatteTypeContext,0)


        def IDENTIFIER(self):
            return self.getToken(LatteParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return LatteParser.RULE_procedureArgument

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcedureArgument" ):
                return visitor.visitProcedureArgument(self)
            else:
                return visitor.visitChildren(self)




    def procedureArgument(self):

        localctx = LatteParser.ProcedureArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_procedureArgument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.latteType()
            self.state = 110
            self.match(LatteParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockStatement(self):
            return self.getTypedRuleContext(LatteParser.BlockStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(LatteParser.IfStatementContext,0)


        def loopStatement(self):
            return self.getTypedRuleContext(LatteParser.LoopStatementContext,0)


        def breakStatement(self):
            return self.getTypedRuleContext(LatteParser.BreakStatementContext,0)


        def continueStatement(self):
            return self.getTypedRuleContext(LatteParser.ContinueStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(LatteParser.ReturnStatementContext,0)


        def expressionStatement(self):
            return self.getTypedRuleContext(LatteParser.ExpressionStatementContext,0)


        def assignStatement(self):
            return self.getTypedRuleContext(LatteParser.AssignStatementContext,0)


        def varStatement(self):
            return self.getTypedRuleContext(LatteParser.VarStatementContext,0)


        def getRuleIndex(self):
            return LatteParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = LatteParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_statement)
        try:
            self.state = 122
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 112
                self.blockStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 113
                self.ifStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 114
                self.loopStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 115
                self.breakStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 116
                self.continueStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 117
                self.returnStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 118
                self.expressionStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 119
                self.assignStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 120
                self.returnStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 121
                self.varStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatteParser.StatementContext)
            else:
                return self.getTypedRuleContext(LatteParser.StatementContext,i)


        def getRuleIndex(self):
            return LatteParser.RULE_blockStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockStatement" ):
                return visitor.visitBlockStatement(self)
            else:
                return visitor.visitChildren(self)




    def blockStatement(self):

        localctx = LatteParser.BlockStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_blockStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(LatteParser.T__6)
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LatteParser.T__3) | (1 << LatteParser.T__6) | (1 << LatteParser.T__9) | (1 << LatteParser.T__10) | (1 << LatteParser.INT) | (1 << LatteParser.REAL) | (1 << LatteParser.IF) | (1 << LatteParser.LOOP) | (1 << LatteParser.BREAK) | (1 << LatteParser.CONTINUE) | (1 << LatteParser.RETURN) | (1 << LatteParser.INT_CONST) | (1 << LatteParser.REAL_CONST) | (1 << LatteParser.IDENTIFIER) | (1 << LatteParser.CHAR_CONST) | (1 << LatteParser.STRING_CONST))) != 0):
                self.state = 125
                self.statement()
                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 131
            self.match(LatteParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(LatteParser.IF, 0)

        def expression(self):
            return self.getTypedRuleContext(LatteParser.ExpressionContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatteParser.StatementContext)
            else:
                return self.getTypedRuleContext(LatteParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(LatteParser.ELSE, 0)

        def getRuleIndex(self):
            return LatteParser.RULE_ifStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = LatteParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(LatteParser.IF)
            self.state = 134
            self.match(LatteParser.T__3)
            self.state = 135
            self.expression(0)
            self.state = 136
            self.match(LatteParser.T__5)
            self.state = 137
            self.statement()
            self.state = 140
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 138
                self.match(LatteParser.ELSE)
                self.state = 139
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOOP(self):
            return self.getToken(LatteParser.LOOP, 0)

        def statement(self):
            return self.getTypedRuleContext(LatteParser.StatementContext,0)


        def IDENTIFIER(self):
            return self.getToken(LatteParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return LatteParser.RULE_loopStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoopStatement" ):
                return visitor.visitLoopStatement(self)
            else:
                return visitor.visitChildren(self)




    def loopStatement(self):

        localctx = LatteParser.LoopStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_loopStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LatteParser.IDENTIFIER:
                self.state = 142
                self.match(LatteParser.IDENTIFIER)
                self.state = 143
                self.match(LatteParser.T__8)


            self.state = 146
            self.match(LatteParser.LOOP)
            self.state = 147
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(LatteParser.BREAK, 0)

        def IDENTIFIER(self):
            return self.getToken(LatteParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return LatteParser.RULE_breakStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStatement" ):
                return visitor.visitBreakStatement(self)
            else:
                return visitor.visitChildren(self)




    def breakStatement(self):

        localctx = LatteParser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_breakStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(LatteParser.BREAK)
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LatteParser.IDENTIFIER:
                self.state = 150
                self.match(LatteParser.IDENTIFIER)


            self.state = 153
            self.match(LatteParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(LatteParser.CONTINUE, 0)

        def IDENTIFIER(self):
            return self.getToken(LatteParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return LatteParser.RULE_continueStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStatement" ):
                return visitor.visitContinueStatement(self)
            else:
                return visitor.visitChildren(self)




    def continueStatement(self):

        localctx = LatteParser.ContinueStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_continueStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(LatteParser.CONTINUE)
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LatteParser.IDENTIFIER:
                self.state = 156
                self.match(LatteParser.IDENTIFIER)


            self.state = 159
            self.match(LatteParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(LatteParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(LatteParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LatteParser.RULE_returnStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = LatteParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(LatteParser.RETURN)
            self.state = 162
            self.expression(0)
            self.state = 163
            self.match(LatteParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(LatteParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LatteParser.RULE_expressionStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionStatement" ):
                return visitor.visitExpressionStatement(self)
            else:
                return visitor.visitChildren(self)




    def expressionStatement(self):

        localctx = LatteParser.ExpressionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_expressionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.expression(0)
            self.state = 166
            self.match(LatteParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def accessExpression(self):
            return self.getTypedRuleContext(LatteParser.AccessExpressionContext,0)


        def expression(self):
            return self.getTypedRuleContext(LatteParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LatteParser.RULE_assignStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStatement" ):
                return visitor.visitAssignStatement(self)
            else:
                return visitor.visitChildren(self)




    def assignStatement(self):

        localctx = LatteParser.AssignStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_assignStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.accessExpression()
            self.state = 169
            self.match(LatteParser.T__2)
            self.state = 170
            self.expression(0)
            self.state = 171
            self.match(LatteParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def latteType(self):
            return self.getTypedRuleContext(LatteParser.LatteTypeContext,0)


        def varInitialization(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatteParser.VarInitializationContext)
            else:
                return self.getTypedRuleContext(LatteParser.VarInitializationContext,i)


        def getRuleIndex(self):
            return LatteParser.RULE_varStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarStatement" ):
                return visitor.visitVarStatement(self)
            else:
                return visitor.visitChildren(self)




    def varStatement(self):

        localctx = LatteParser.VarStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_varStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.latteType()
            self.state = 174
            self.varInitialization()
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LatteParser.T__4:
                self.state = 175
                self.match(LatteParser.T__4)
                self.state = 176
                self.varInitialization()
                self.state = 181
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 182
            self.match(LatteParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarInitializationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(LatteParser.IDENTIFIER, 0)

        def expression(self):
            return self.getTypedRuleContext(LatteParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LatteParser.RULE_varInitialization

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarInitialization" ):
                return visitor.visitVarInitialization(self)
            else:
                return visitor.visitChildren(self)




    def varInitialization(self):

        localctx = LatteParser.VarInitializationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_varInitialization)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(LatteParser.IDENTIFIER)
            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LatteParser.T__2:
                self.state = 185
                self.match(LatteParser.T__2)
                self.state = 186
                self.expression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LatteParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class BinaryOrExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatteParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LatteParser.ExpressionContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinaryOrExpr" ):
                return visitor.visitBinaryOrExpr(self)
            else:
                return visitor.visitChildren(self)


    class ArrayExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatteParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LatteParser.ExpressionContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayExpr" ):
                return visitor.visitArrayExpr(self)
            else:
                return visitor.visitChildren(self)


    class BinaryMulExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatteParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LatteParser.ExpressionContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinaryMulExpr" ):
                return visitor.visitBinaryMulExpr(self)
            else:
                return visitor.visitChildren(self)


    class BinaryModExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatteParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LatteParser.ExpressionContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinaryModExpr" ):
                return visitor.visitBinaryModExpr(self)
            else:
                return visitor.visitChildren(self)


    class IntConstExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT_CONST(self):
            return self.getToken(LatteParser.INT_CONST, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntConstExpr" ):
                return visitor.visitIntConstExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(LatteParser.ExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)


    class CharConstExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CHAR_CONST(self):
            return self.getToken(LatteParser.CHAR_CONST, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCharConstExpr" ):
                return visitor.visitCharConstExpr(self)
            else:
                return visitor.visitChildren(self)


    class UnaryExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(LatteParser.ExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpr" ):
                return visitor.visitUnaryExpr(self)
            else:
                return visitor.visitChildren(self)


    class BinaryAddExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatteParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LatteParser.ExpressionContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinaryAddExpr" ):
                return visitor.visitBinaryAddExpr(self)
            else:
                return visitor.visitChildren(self)


    class RealConstExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def REAL_CONST(self):
            return self.getToken(LatteParser.REAL_CONST, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRealConstExpr" ):
                return visitor.visitRealConstExpr(self)
            else:
                return visitor.visitChildren(self)


    class StringConstExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING_CONST(self):
            return self.getToken(LatteParser.STRING_CONST, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringConstExpr" ):
                return visitor.visitStringConstExpr(self)
            else:
                return visitor.visitChildren(self)


    class BinaryCompExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatteParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LatteParser.ExpressionContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinaryCompExpr" ):
                return visitor.visitBinaryCompExpr(self)
            else:
                return visitor.visitChildren(self)


    class BinaryEqExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatteParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LatteParser.ExpressionContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinaryEqExpr" ):
                return visitor.visitBinaryEqExpr(self)
            else:
                return visitor.visitChildren(self)


    class BinaryAndExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatteParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LatteParser.ExpressionContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinaryAndExpr" ):
                return visitor.visitBinaryAndExpr(self)
            else:
                return visitor.visitChildren(self)


    class CallExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(LatteParser.IDENTIFIER, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatteParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LatteParser.ExpressionContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallExpr" ):
                return visitor.visitCallExpr(self)
            else:
                return visitor.visitChildren(self)


    class AccessExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def accessExpression(self):
            return self.getTypedRuleContext(LatteParser.AccessExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAccessExpr" ):
                return visitor.visitAccessExpr(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LatteParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                localctx = LatteParser.UnaryExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 190
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==LatteParser.T__9 or _la==LatteParser.T__10):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 191
                self.expression(16)
                pass

            elif la_ == 2:
                localctx = LatteParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 192
                self.match(LatteParser.T__3)
                self.state = 193
                self.expression(0)
                self.state = 194
                self.match(LatteParser.T__5)
                pass

            elif la_ == 3:
                localctx = LatteParser.ArrayExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 196
                self.match(LatteParser.T__6)
                self.state = 197
                self.expression(0)
                self.state = 202
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==LatteParser.T__4:
                    self.state = 198
                    self.match(LatteParser.T__4)
                    self.state = 199
                    self.expression(0)
                    self.state = 204
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 205
                self.match(LatteParser.T__7)
                pass

            elif la_ == 4:
                localctx = LatteParser.CallExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 207
                self.match(LatteParser.IDENTIFIER)
                self.state = 208
                self.match(LatteParser.T__3)
                self.state = 217
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LatteParser.T__3) | (1 << LatteParser.T__6) | (1 << LatteParser.T__9) | (1 << LatteParser.T__10) | (1 << LatteParser.INT_CONST) | (1 << LatteParser.REAL_CONST) | (1 << LatteParser.IDENTIFIER) | (1 << LatteParser.CHAR_CONST) | (1 << LatteParser.STRING_CONST))) != 0):
                    self.state = 209
                    self.expression(0)
                    self.state = 214
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==LatteParser.T__4:
                        self.state = 210
                        self.match(LatteParser.T__4)
                        self.state = 211
                        self.expression(0)
                        self.state = 216
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 219
                self.match(LatteParser.T__5)
                pass

            elif la_ == 5:
                localctx = LatteParser.AccessExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 220
                self.accessExpression()
                pass

            elif la_ == 6:
                localctx = LatteParser.IntConstExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 221
                self.match(LatteParser.INT_CONST)
                pass

            elif la_ == 7:
                localctx = LatteParser.RealConstExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 222
                self.match(LatteParser.REAL_CONST)
                pass

            elif la_ == 8:
                localctx = LatteParser.CharConstExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 223
                self.match(LatteParser.CHAR_CONST)
                pass

            elif la_ == 9:
                localctx = LatteParser.StringConstExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 224
                self.match(LatteParser.STRING_CONST)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 250
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 248
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                    if la_ == 1:
                        localctx = LatteParser.BinaryMulExprContext(self, LatteParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 227
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 228
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==LatteParser.T__11 or _la==LatteParser.T__12):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 229
                        self.expression(16)
                        pass

                    elif la_ == 2:
                        localctx = LatteParser.BinaryAddExprContext(self, LatteParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 230
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 231
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==LatteParser.T__9 or _la==LatteParser.T__13):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 232
                        self.expression(15)
                        pass

                    elif la_ == 3:
                        localctx = LatteParser.BinaryModExprContext(self, LatteParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 233
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 234
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==LatteParser.T__14 or _la==LatteParser.T__15):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 235
                        self.expression(14)
                        pass

                    elif la_ == 4:
                        localctx = LatteParser.BinaryCompExprContext(self, LatteParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 236
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 237
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LatteParser.T__16) | (1 << LatteParser.T__17) | (1 << LatteParser.T__18) | (1 << LatteParser.T__19))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 238
                        self.expression(13)
                        pass

                    elif la_ == 5:
                        localctx = LatteParser.BinaryEqExprContext(self, LatteParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 239
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 240
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==LatteParser.T__20 or _la==LatteParser.T__21):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 241
                        self.expression(12)
                        pass

                    elif la_ == 6:
                        localctx = LatteParser.BinaryAndExprContext(self, LatteParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 242
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 243
                        self.match(LatteParser.T__22)
                        self.state = 244
                        self.expression(11)
                        pass

                    elif la_ == 7:
                        localctx = LatteParser.BinaryOrExprContext(self, LatteParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 245
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 246
                        self.match(LatteParser.T__23)
                        self.state = 247
                        self.expression(10)
                        pass

             
                self.state = 252
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AccessExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(LatteParser.IDENTIFIER, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatteParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LatteParser.ExpressionContext,i)


        def getRuleIndex(self):
            return LatteParser.RULE_accessExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAccessExpression" ):
                return visitor.visitAccessExpression(self)
            else:
                return visitor.visitChildren(self)




    def accessExpression(self):

        localctx = LatteParser.AccessExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_accessExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(LatteParser.IDENTIFIER)
            self.state = 265
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 254
                self.match(LatteParser.T__24)
                self.state = 255
                self.expression(0)
                self.state = 260
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==LatteParser.T__4:
                    self.state = 256
                    self.match(LatteParser.T__4)
                    self.state = 257
                    self.expression(0)
                    self.state = 262
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 263
                self.match(LatteParser.T__25)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LatteTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nativeType(self):
            return self.getTypedRuleContext(LatteParser.NativeTypeContext,0)


        def INT_CONST(self):
            return self.getToken(LatteParser.INT_CONST, 0)

        def ARRAY(self):
            return self.getToken(LatteParser.ARRAY, 0)

        def arrayShape(self):
            return self.getTypedRuleContext(LatteParser.ArrayShapeContext,0)


        def getRuleIndex(self):
            return LatteParser.RULE_latteType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLatteType" ):
                return visitor.visitLatteType(self)
            else:
                return visitor.visitChildren(self)




    def latteType(self):

        localctx = LatteParser.LatteTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_latteType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.nativeType()
            self.state = 268
            self.match(LatteParser.T__3)
            self.state = 269
            self.match(LatteParser.INT_CONST)
            self.state = 270
            self.match(LatteParser.T__5)
            self.state = 276
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LatteParser.ARRAY:
                self.state = 271
                self.match(LatteParser.ARRAY)
                self.state = 272
                self.match(LatteParser.T__3)
                self.state = 273
                self.arrayShape()
                self.state = 274
                self.match(LatteParser.T__5)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NativeTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(LatteParser.INT, 0)

        def REAL(self):
            return self.getToken(LatteParser.REAL, 0)

        def getRuleIndex(self):
            return LatteParser.RULE_nativeType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNativeType" ):
                return visitor.visitNativeType(self)
            else:
                return visitor.visitChildren(self)




    def nativeType(self):

        localctx = LatteParser.NativeTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_nativeType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            _la = self._input.LA(1)
            if not(_la==LatteParser.INT or _la==LatteParser.REAL):
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


    class ArrayShapeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_CONST(self, i:int=None):
            if i is None:
                return self.getTokens(LatteParser.INT_CONST)
            else:
                return self.getToken(LatteParser.INT_CONST, i)

        def getRuleIndex(self):
            return LatteParser.RULE_arrayShape

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayShape" ):
                return visitor.visitArrayShape(self)
            else:
                return visitor.visitChildren(self)




    def arrayShape(self):

        localctx = LatteParser.ArrayShapeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_arrayShape)
        self._la = 0 # Token type
        try:
            self.state = 289
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LatteParser.T__11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 280
                self.match(LatteParser.T__11)
                pass
            elif token in [LatteParser.INT_CONST]:
                self.enterOuterAlt(localctx, 2)
                self.state = 281
                self.match(LatteParser.INT_CONST)
                self.state = 286
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==LatteParser.T__4:
                    self.state = 282
                    self.match(LatteParser.T__4)
                    self.state = 283
                    self.match(LatteParser.INT_CONST)
                    self.state = 288
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[17] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 9)
         




