# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *
# ID: 2112897



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\65")
        buf.write("\u0192\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\3\2\6\2{\n\2\r\2\16\2|\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\3\3\5\3\u0086\n\3\3\4\3\4\3\4\3\4\7\4\u008c\n\4")
        buf.write("\f\4\16\4\u008f\13\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36")
        buf.write("\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3$\3$\3$\3")
        buf.write("%\3%\3&\3&\3&\3\'\3\'\3\'\3\'\3(\3(\3(\3)\3)\3*\3*\3+")
        buf.write("\3+\3,\3,\3-\3-\3.\6.\u0135\n.\r.\16.\u0136\3/\3/\7/\u013b")
        buf.write("\n/\f/\16/\u013e\13/\3\60\3\60\5\60\u0142\n\60\3\60\6")
        buf.write("\60\u0145\n\60\r\60\16\60\u0146\3\61\3\61\5\61\u014b\n")
        buf.write("\61\3\61\5\61\u014e\n\61\3\62\3\62\5\62\u0152\n\62\3\63")
        buf.write("\3\63\3\64\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\67\3\67")
        buf.write("\3\67\3\67\7\67\u0162\n\67\f\67\16\67\u0165\13\67\3\67")
        buf.write("\3\67\3\67\38\38\38\38\38\78\u016f\n8\f8\168\u0172\13")
        buf.write("8\38\58\u0175\n8\38\38\39\39\39\3:\3:\3:\3:\3:\7:\u0181")
        buf.write("\n:\f:\16:\u0184\13:\3:\3:\3:\3;\3;\7;\u018b\n;\f;\16")
        buf.write(";\u018e\13;\3<\3<\3<\2\2=\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[\2]\2_\2a/c\60e\2")
        buf.write("g\2i\2k\2m\61o\62q\2s\63u\64w\65\3\2\16\5\2\n\13\16\16")
        buf.write("\"\"\3\2\f\f\3\2\62;\3\2\60\60\4\2GGgg\4\2--//\t\2))^")
        buf.write("^ddhhppttvv\3\2))\3\2$$\6\2\n\f\16\17$$^^\5\2C\\aac|\6")
        buf.write("\2\62;C\\aac|\2\u01a0\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2")
        buf.write("\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2")
        buf.write("\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!")
        buf.write("\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2s")
        buf.write("\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\3z\3\2\2\2\5\u0085\3\2")
        buf.write("\2\2\7\u0087\3\2\2\2\t\u0092\3\2\2\2\13\u0097\3\2\2\2")
        buf.write("\r\u009d\3\2\2\2\17\u00a4\3\2\2\2\21\u00a9\3\2\2\2\23")
        buf.write("\u00b0\3\2\2\2\25\u00b7\3\2\2\2\27\u00bb\3\2\2\2\31\u00c3")
        buf.write("\3\2\2\2\33\u00c8\3\2\2\2\35\u00cc\3\2\2\2\37\u00d2\3")
        buf.write("\2\2\2!\u00d5\3\2\2\2#\u00db\3\2\2\2%\u00e4\3\2\2\2\'")
        buf.write("\u00e7\3\2\2\2)\u00ec\3\2\2\2+\u00f1\3\2\2\2-\u00f7\3")
        buf.write("\2\2\2/\u00fb\3\2\2\2\61\u00ff\3\2\2\2\63\u0103\3\2\2")
        buf.write("\2\65\u0106\3\2\2\2\67\u0108\3\2\2\29\u010a\3\2\2\2;\u010c")
        buf.write("\3\2\2\2=\u010e\3\2\2\2?\u0110\3\2\2\2A\u0112\3\2\2\2")
        buf.write("C\u0115\3\2\2\2E\u0118\3\2\2\2G\u011a\3\2\2\2I\u011d\3")
        buf.write("\2\2\2K\u011f\3\2\2\2M\u0122\3\2\2\2O\u0126\3\2\2\2Q\u0129")
        buf.write("\3\2\2\2S\u012b\3\2\2\2U\u012d\3\2\2\2W\u012f\3\2\2\2")
        buf.write("Y\u0131\3\2\2\2[\u0134\3\2\2\2]\u0138\3\2\2\2_\u013f\3")
        buf.write("\2\2\2a\u0148\3\2\2\2c\u0151\3\2\2\2e\u0153\3\2\2\2g\u0155")
        buf.write("\3\2\2\2i\u0158\3\2\2\2k\u015b\3\2\2\2m\u015d\3\2\2\2")
        buf.write("o\u0169\3\2\2\2q\u0178\3\2\2\2s\u017b\3\2\2\2u\u0188\3")
        buf.write("\2\2\2w\u018f\3\2\2\2y{\t\2\2\2zy\3\2\2\2{|\3\2\2\2|z")
        buf.write("\3\2\2\2|}\3\2\2\2}~\3\2\2\2~\177\b\2\2\2\177\4\3\2\2")
        buf.write("\2\u0080\u0086\7\f\2\2\u0081\u0082\7\17\2\2\u0082\u0083")
        buf.write("\7\f\2\2\u0083\u0084\3\2\2\2\u0084\u0086\b\3\3\2\u0085")
        buf.write("\u0080\3\2\2\2\u0085\u0081\3\2\2\2\u0086\6\3\2\2\2\u0087")
        buf.write("\u0088\7%\2\2\u0088\u0089\7%\2\2\u0089\u008d\3\2\2\2\u008a")
        buf.write("\u008c\n\3\2\2\u008b\u008a\3\2\2\2\u008c\u008f\3\2\2\2")
        buf.write("\u008d\u008b\3\2\2\2\u008d\u008e\3\2\2\2\u008e\u0090\3")
        buf.write("\2\2\2\u008f\u008d\3\2\2\2\u0090\u0091\b\4\2\2\u0091\b")
        buf.write("\3\2\2\2\u0092\u0093\7v\2\2\u0093\u0094\7t\2\2\u0094\u0095")
        buf.write("\7w\2\2\u0095\u0096\7g\2\2\u0096\n\3\2\2\2\u0097\u0098")
        buf.write("\7h\2\2\u0098\u0099\7c\2\2\u0099\u009a\7n\2\2\u009a\u009b")
        buf.write("\7u\2\2\u009b\u009c\7g\2\2\u009c\f\3\2\2\2\u009d\u009e")
        buf.write("\7p\2\2\u009e\u009f\7w\2\2\u009f\u00a0\7o\2\2\u00a0\u00a1")
        buf.write("\7d\2\2\u00a1\u00a2\7g\2\2\u00a2\u00a3\7t\2\2\u00a3\16")
        buf.write("\3\2\2\2\u00a4\u00a5\7d\2\2\u00a5\u00a6\7q\2\2\u00a6\u00a7")
        buf.write("\7q\2\2\u00a7\u00a8\7n\2\2\u00a8\20\3\2\2\2\u00a9\u00aa")
        buf.write("\7u\2\2\u00aa\u00ab\7v\2\2\u00ab\u00ac\7t\2\2\u00ac\u00ad")
        buf.write("\7k\2\2\u00ad\u00ae\7p\2\2\u00ae\u00af\7i\2\2\u00af\22")
        buf.write("\3\2\2\2\u00b0\u00b1\7t\2\2\u00b1\u00b2\7g\2\2\u00b2\u00b3")
        buf.write("\7v\2\2\u00b3\u00b4\7w\2\2\u00b4\u00b5\7t\2\2\u00b5\u00b6")
        buf.write("\7p\2\2\u00b6\24\3\2\2\2\u00b7\u00b8\7x\2\2\u00b8\u00b9")
        buf.write("\7c\2\2\u00b9\u00ba\7t\2\2\u00ba\26\3\2\2\2\u00bb\u00bc")
        buf.write("\7f\2\2\u00bc\u00bd\7{\2\2\u00bd\u00be\7p\2\2\u00be\u00bf")
        buf.write("\7c\2\2\u00bf\u00c0\7o\2\2\u00c0\u00c1\7k\2\2\u00c1\u00c2")
        buf.write("\7e\2\2\u00c2\30\3\2\2\2\u00c3\u00c4\7h\2\2\u00c4\u00c5")
        buf.write("\7w\2\2\u00c5\u00c6\7p\2\2\u00c6\u00c7\7e\2\2\u00c7\32")
        buf.write("\3\2\2\2\u00c8\u00c9\7h\2\2\u00c9\u00ca\7q\2\2\u00ca\u00cb")
        buf.write("\7t\2\2\u00cb\34\3\2\2\2\u00cc\u00cd\7w\2\2\u00cd\u00ce")
        buf.write("\7p\2\2\u00ce\u00cf\7v\2\2\u00cf\u00d0\7k\2\2\u00d0\u00d1")
        buf.write("\7n\2\2\u00d1\36\3\2\2\2\u00d2\u00d3\7d\2\2\u00d3\u00d4")
        buf.write("\7{\2\2\u00d4 \3\2\2\2\u00d5\u00d6\7d\2\2\u00d6\u00d7")
        buf.write("\7t\2\2\u00d7\u00d8\7g\2\2\u00d8\u00d9\7c\2\2\u00d9\u00da")
        buf.write("\7m\2\2\u00da\"\3\2\2\2\u00db\u00dc\7e\2\2\u00dc\u00dd")
        buf.write("\7q\2\2\u00dd\u00de\7p\2\2\u00de\u00df\7v\2\2\u00df\u00e0")
        buf.write("\7k\2\2\u00e0\u00e1\7p\2\2\u00e1\u00e2\7w\2\2\u00e2\u00e3")
        buf.write("\7g\2\2\u00e3$\3\2\2\2\u00e4\u00e5\7k\2\2\u00e5\u00e6")
        buf.write("\7h\2\2\u00e6&\3\2\2\2\u00e7\u00e8\7g\2\2\u00e8\u00e9")
        buf.write("\7n\2\2\u00e9\u00ea\7u\2\2\u00ea\u00eb\7g\2\2\u00eb(\3")
        buf.write("\2\2\2\u00ec\u00ed\7g\2\2\u00ed\u00ee\7n\2\2\u00ee\u00ef")
        buf.write("\7k\2\2\u00ef\u00f0\7h\2\2\u00f0*\3\2\2\2\u00f1\u00f2")
        buf.write("\7d\2\2\u00f2\u00f3\7g\2\2\u00f3\u00f4\7i\2\2\u00f4\u00f5")
        buf.write("\7k\2\2\u00f5\u00f6\7p\2\2\u00f6,\3\2\2\2\u00f7\u00f8")
        buf.write("\7g\2\2\u00f8\u00f9\7p\2\2\u00f9\u00fa\7f\2\2\u00fa.\3")
        buf.write("\2\2\2\u00fb\u00fc\7p\2\2\u00fc\u00fd\7q\2\2\u00fd\u00fe")
        buf.write("\7v\2\2\u00fe\60\3\2\2\2\u00ff\u0100\7c\2\2\u0100\u0101")
        buf.write("\7p\2\2\u0101\u0102\7f\2\2\u0102\62\3\2\2\2\u0103\u0104")
        buf.write("\7q\2\2\u0104\u0105\7t\2\2\u0105\64\3\2\2\2\u0106\u0107")
        buf.write("\7-\2\2\u0107\66\3\2\2\2\u0108\u0109\7/\2\2\u01098\3\2")
        buf.write("\2\2\u010a\u010b\7,\2\2\u010b:\3\2\2\2\u010c\u010d\7\61")
        buf.write("\2\2\u010d<\3\2\2\2\u010e\u010f\7\'\2\2\u010f>\3\2\2\2")
        buf.write("\u0110\u0111\7?\2\2\u0111@\3\2\2\2\u0112\u0113\7>\2\2")
        buf.write("\u0113\u0114\7/\2\2\u0114B\3\2\2\2\u0115\u0116\7#\2\2")
        buf.write("\u0116\u0117\7?\2\2\u0117D\3\2\2\2\u0118\u0119\7>\2\2")
        buf.write("\u0119F\3\2\2\2\u011a\u011b\7>\2\2\u011b\u011c\7?\2\2")
        buf.write("\u011cH\3\2\2\2\u011d\u011e\7@\2\2\u011eJ\3\2\2\2\u011f")
        buf.write("\u0120\7@\2\2\u0120\u0121\7?\2\2\u0121L\3\2\2\2\u0122")
        buf.write("\u0123\7\60\2\2\u0123\u0124\7\60\2\2\u0124\u0125\7\60")
        buf.write("\2\2\u0125N\3\2\2\2\u0126\u0127\7?\2\2\u0127\u0128\7?")
        buf.write("\2\2\u0128P\3\2\2\2\u0129\u012a\7*\2\2\u012aR\3\2\2\2")
        buf.write("\u012b\u012c\7+\2\2\u012cT\3\2\2\2\u012d\u012e\7]\2\2")
        buf.write("\u012eV\3\2\2\2\u012f\u0130\7_\2\2\u0130X\3\2\2\2\u0131")
        buf.write("\u0132\7.\2\2\u0132Z\3\2\2\2\u0133\u0135\t\4\2\2\u0134")
        buf.write("\u0133\3\2\2\2\u0135\u0136\3\2\2\2\u0136\u0134\3\2\2\2")
        buf.write("\u0136\u0137\3\2\2\2\u0137\\\3\2\2\2\u0138\u013c\t\5\2")
        buf.write("\2\u0139\u013b\t\4\2\2\u013a\u0139\3\2\2\2\u013b\u013e")
        buf.write("\3\2\2\2\u013c\u013a\3\2\2\2\u013c\u013d\3\2\2\2\u013d")
        buf.write("^\3\2\2\2\u013e\u013c\3\2\2\2\u013f\u0141\t\6\2\2\u0140")
        buf.write("\u0142\t\7\2\2\u0141\u0140\3\2\2\2\u0141\u0142\3\2\2\2")
        buf.write("\u0142\u0144\3\2\2\2\u0143\u0145\t\4\2\2\u0144\u0143\3")
        buf.write("\2\2\2\u0145\u0146\3\2\2\2\u0146\u0144\3\2\2\2\u0146\u0147")
        buf.write("\3\2\2\2\u0147`\3\2\2\2\u0148\u014a\5[.\2\u0149\u014b")
        buf.write("\5]/\2\u014a\u0149\3\2\2\2\u014a\u014b\3\2\2\2\u014b\u014d")
        buf.write("\3\2\2\2\u014c\u014e\5_\60\2\u014d\u014c\3\2\2\2\u014d")
        buf.write("\u014e\3\2\2\2\u014eb\3\2\2\2\u014f\u0152\5\t\5\2\u0150")
        buf.write("\u0152\5\13\6\2\u0151\u014f\3\2\2\2\u0151\u0150\3\2\2")
        buf.write("\2\u0152d\3\2\2\2\u0153\u0154\7$\2\2\u0154f\3\2\2\2\u0155")
        buf.write("\u0156\7^\2\2\u0156\u0157\t\b\2\2\u0157h\3\2\2\2\u0158")
        buf.write("\u0159\t\t\2\2\u0159\u015a\t\n\2\2\u015aj\3\2\2\2\u015b")
        buf.write("\u015c\n\13\2\2\u015cl\3\2\2\2\u015d\u0163\5e\63\2\u015e")
        buf.write("\u0162\5g\64\2\u015f\u0162\5i\65\2\u0160\u0162\5k\66\2")
        buf.write("\u0161\u015e\3\2\2\2\u0161\u015f\3\2\2\2\u0161\u0160\3")
        buf.write("\2\2\2\u0162\u0165\3\2\2\2\u0163\u0161\3\2\2\2\u0163\u0164")
        buf.write("\3\2\2\2\u0164\u0166\3\2\2\2\u0165\u0163\3\2\2\2\u0166")
        buf.write("\u0167\5e\63\2\u0167\u0168\b\67\4\2\u0168n\3\2\2\2\u0169")
        buf.write("\u0170\5e\63\2\u016a\u016f\5g\64\2\u016b\u016f\5i\65\2")
        buf.write("\u016c\u016f\5k\66\2\u016d\u016f\5\5\3\2\u016e\u016a\3")
        buf.write("\2\2\2\u016e\u016b\3\2\2\2\u016e\u016c\3\2\2\2\u016e\u016d")
        buf.write("\3\2\2\2\u016f\u0172\3\2\2\2\u0170\u016e\3\2\2\2\u0170")
        buf.write("\u0171\3\2\2\2\u0171\u0174\3\2\2\2\u0172\u0170\3\2\2\2")
        buf.write("\u0173\u0175\5e\63\2\u0174\u0173\3\2\2\2\u0174\u0175\3")
        buf.write("\2\2\2\u0175\u0176\3\2\2\2\u0176\u0177\b8\5\2\u0177p\3")
        buf.write("\2\2\2\u0178\u0179\7^\2\2\u0179\u017a\n\b\2\2\u017ar\3")
        buf.write("\2\2\2\u017b\u0182\5e\63\2\u017c\u0181\5g\64\2\u017d\u0181")
        buf.write("\5i\65\2\u017e\u0181\5k\66\2\u017f\u0181\5q9\2\u0180\u017c")
        buf.write("\3\2\2\2\u0180\u017d\3\2\2\2\u0180\u017e\3\2\2\2\u0180")
        buf.write("\u017f\3\2\2\2\u0181\u0184\3\2\2\2\u0182\u0180\3\2\2\2")
        buf.write("\u0182\u0183\3\2\2\2\u0183\u0185\3\2\2\2\u0184\u0182\3")
        buf.write("\2\2\2\u0185\u0186\5e\63\2\u0186\u0187\b:\6\2\u0187t\3")
        buf.write("\2\2\2\u0188\u018c\t\f\2\2\u0189\u018b\t\r\2\2\u018a\u0189")
        buf.write("\3\2\2\2\u018b\u018e\3\2\2\2\u018c\u018a\3\2\2\2\u018c")
        buf.write("\u018d\3\2\2\2\u018dv\3\2\2\2\u018e\u018c\3\2\2\2\u018f")
        buf.write("\u0190\13\2\2\2\u0190\u0191\b<\7\2\u0191x\3\2\2\2\25\2")
        buf.write("|\u0085\u008d\u0136\u013c\u0141\u0146\u014a\u014d\u0151")
        buf.write("\u0161\u0163\u016e\u0170\u0174\u0180\u0182\u018c\b\b\2")
        buf.write("\2\3\3\2\3\67\3\38\4\3:\5\3<\6")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WS = 1
    NEWLINE = 2
    COMMENT = 3
    TRUE = 4
    FALSE = 5
    NUMBER = 6
    BOOL = 7
    STRING = 8
    RETURN = 9
    VAR = 10
    DYNAMIC = 11
    FUNC = 12
    FOR = 13
    UNTIL = 14
    BY = 15
    BREAK = 16
    CONTINUE = 17
    IF = 18
    ELSE = 19
    ELIF = 20
    BEGIN = 21
    END = 22
    NOT = 23
    AND = 24
    OR = 25
    ADD_OP = 26
    SUBTR_OP = 27
    MUL_OP = 28
    DIV_OP = 29
    REMAINDER_OP = 30
    EQUAL = 31
    ASSIGN = 32
    NOT_EQUAL = 33
    SMALLER = 34
    SMALLER_OR_EQUAL = 35
    GREATER = 36
    GREATER_OR_EQUAL = 37
    SPREAD_OP = 38
    EQUAL_STR = 39
    LP = 40
    RP = 41
    LB = 42
    RB = 43
    COMMA = 44
    NUM_LIT = 45
    BOOL_LIT = 46
    STRING_LIT = 47
    UNCLOSE_STRING = 48
    ILLEGAL_ESCAPE = 49
    IDENTIFIER = 50
    ERROR_CHAR = 51

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'true'", "'false'", "'number'", "'bool'", "'string'", "'return'", 
            "'var'", "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
            "'break'", "'continue'", "'if'", "'else'", "'elif'", "'begin'", 
            "'end'", "'not'", "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'='", "'<-'", "'!='", "'<'", "'<='", "'>'", "'>='", 
            "'...'", "'=='", "'('", "')'", "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>",
            "WS", "NEWLINE", "COMMENT", "TRUE", "FALSE", "NUMBER", "BOOL", 
            "STRING", "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", 
            "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", 
            "NOT", "AND", "OR", "ADD_OP", "SUBTR_OP", "MUL_OP", "DIV_OP", 
            "REMAINDER_OP", "EQUAL", "ASSIGN", "NOT_EQUAL", "SMALLER", "SMALLER_OR_EQUAL", 
            "GREATER", "GREATER_OR_EQUAL", "SPREAD_OP", "EQUAL_STR", "LP", 
            "RP", "LB", "RB", "COMMA", "NUM_LIT", "BOOL_LIT", "STRING_LIT", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "IDENTIFIER", "ERROR_CHAR" ]

    ruleNames = [ "WS", "NEWLINE", "COMMENT", "TRUE", "FALSE", "NUMBER", 
                  "BOOL", "STRING", "RETURN", "VAR", "DYNAMIC", "FUNC", 
                  "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", "IF", "ELSE", 
                  "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "ADD_OP", 
                  "SUBTR_OP", "MUL_OP", "DIV_OP", "REMAINDER_OP", "EQUAL", 
                  "ASSIGN", "NOT_EQUAL", "SMALLER", "SMALLER_OR_EQUAL", 
                  "GREATER", "GREATER_OR_EQUAL", "SPREAD_OP", "EQUAL_STR", 
                  "LP", "RP", "LB", "RB", "COMMA", "INT", "DEC", "EXP", 
                  "NUM_LIT", "BOOL_LIT", "DOUBLE_QUOTE", "ESCAPE_SEQ", "QUOTE_STR", 
                  "CHAR", "STRING_LIT", "UNCLOSE_STRING", "ILLEGAL", "ILLEGAL_ESCAPE", 
                  "IDENTIFIER", "ERROR_CHAR" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[1] = self.NEWLINE_action 
            actions[53] = self.STRING_LIT_action 
            actions[54] = self.UNCLOSE_STRING_action 
            actions[56] = self.ILLEGAL_ESCAPE_action 
            actions[58] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = '\n';
     

    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text[1:-1];
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	if self.text.find('\n') != -1:
            		print("newline error")
            		raise UncloseString(self.text[1:(self.text.find('\n') - 1)])
            	if self.text[-1] != '"':
            		print(self.text[-1])
            		print("double quote error")
            		raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

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

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise ErrorToken(self.text)
     


