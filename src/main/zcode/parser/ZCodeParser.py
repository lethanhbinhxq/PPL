# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\65")
        buf.write("\u01e5\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\3\2\3\2\3\2\3\2\3\2\3\3\3\3")
        buf.write("\5\3\u0086\n\3\3\4\3\4\3\4\5\4\u008b\n\4\3\5\3\5\3\5\5")
        buf.write("\5\u0090\n\5\3\6\3\6\3\6\3\6\5\6\u0096\n\6\3\7\3\7\3\7")
        buf.write("\3\b\3\b\5\b\u009d\n\b\3\t\3\t\3\t\5\t\u00a2\n\t\3\n\3")
        buf.write("\n\3\n\3\n\5\n\u00a8\n\n\3\13\3\13\3\f\3\f\5\f\u00ae\n")
        buf.write("\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\5\16\u00b9")
        buf.write("\n\16\3\17\3\17\3\17\3\17\3\17\5\17\u00c0\n\17\3\20\3")
        buf.write("\20\3\20\3\20\3\21\3\21\3\21\5\21\u00c9\n\21\3\22\3\22")
        buf.write("\3\22\3\22\5\22\u00cf\n\22\3\23\3\23\3\23\3\23\3\23\3")
        buf.write("\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\5\25\u00df")
        buf.write("\n\25\3\26\3\26\3\26\3\26\3\26\5\26\u00e6\n\26\3\27\3")
        buf.write("\27\3\27\3\27\3\27\3\27\3\27\5\27\u00ef\n\27\3\30\3\30")
        buf.write("\3\30\5\30\u00f4\n\30\3\31\3\31\3\31\3\31\5\31\u00fa\n")
        buf.write("\31\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\5\33\u0108\n\33\3\34\3\34\3\34\3\34\3\34\3")
        buf.write("\35\3\35\3\35\3\35\5\35\u0113\n\35\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\5\37")
        buf.write("\u0123\n\37\3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\5!\u0131")
        buf.write("\n!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3$\3")
        buf.write("$\3$\3%\3%\3%\3%\5%\u0146\n%\3&\3&\3&\3&\3&\3\'\3\'\3")
        buf.write("\'\3\'\5\'\u0151\n\'\3(\3(\3(\3(\3(\5(\u0158\n(\3)\3)")
        buf.write("\3)\3)\3)\3)\3*\3*\5*\u0162\n*\3+\3+\3+\3+\5+\u0168\n")
        buf.write("+\3,\3,\3,\3,\3,\5,\u016f\n,\3-\3-\3-\3-\3-\5-\u0176\n")
        buf.write("-\3.\3.\3.\3.\3.\3.\3.\7.\u017f\n.\f.\16.\u0182\13.\3")
        buf.write("/\3/\3/\3/\3/\3/\3/\7/\u018b\n/\f/\16/\u018e\13/\3\60")
        buf.write("\3\60\3\60\3\60\3\60\3\60\3\60\7\60\u0197\n\60\f\60\16")
        buf.write("\60\u019a\13\60\3\61\3\61\3\61\5\61\u019f\n\61\3\62\3")
        buf.write("\62\3\62\5\62\u01a4\n\62\3\63\3\63\3\63\3\63\3\63\7\63")
        buf.write("\u01ab\n\63\f\63\16\63\u01ae\13\63\3\64\3\64\3\64\3\64")
        buf.write("\3\64\5\64\u01b5\n\64\3\65\3\65\3\65\5\65\u01ba\n\65\3")
        buf.write("\66\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\5\67")
        buf.write("\u01c6\n\67\38\38\38\38\39\39\39\39\59\u01d0\n9\3:\3:")
        buf.write("\3:\3:\3;\3;\3;\3;\3;\5;\u01db\n;\3<\3<\3=\3=\3>\3>\3")
        buf.write("?\3?\3?\2\6Z\\^d@\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjln")
        buf.write("prtvxz|\2\7\3\2\b\n\3\2\36 \3\2\34\35\3\2\32\33\5\2!!")
        buf.write("#\'))\2\u01da\2~\3\2\2\2\4\u0085\3\2\2\2\6\u008a\3\2\2")
        buf.write("\2\b\u008f\3\2\2\2\n\u0095\3\2\2\2\f\u0097\3\2\2\2\16")
        buf.write("\u009c\3\2\2\2\20\u00a1\3\2\2\2\22\u00a3\3\2\2\2\24\u00a9")
        buf.write("\3\2\2\2\26\u00ad\3\2\2\2\30\u00af\3\2\2\2\32\u00b4\3")
        buf.write("\2\2\2\34\u00ba\3\2\2\2\36\u00c1\3\2\2\2 \u00c8\3\2\2")
        buf.write("\2\"\u00ce\3\2\2\2$\u00d0\3\2\2\2&\u00d6\3\2\2\2(\u00de")
        buf.write("\3\2\2\2*\u00e5\3\2\2\2,\u00ee\3\2\2\2.\u00f3\3\2\2\2")
        buf.write("\60\u00f9\3\2\2\2\62\u00fb\3\2\2\2\64\u0107\3\2\2\2\66")
        buf.write("\u0109\3\2\2\28\u0112\3\2\2\2:\u0114\3\2\2\2<\u0122\3")
        buf.write("\2\2\2>\u0124\3\2\2\2@\u0130\3\2\2\2B\u0132\3\2\2\2D\u013b")
        buf.write("\3\2\2\2F\u013e\3\2\2\2H\u0145\3\2\2\2J\u0147\3\2\2\2")
        buf.write("L\u0150\3\2\2\2N\u0157\3\2\2\2P\u0159\3\2\2\2R\u0161\3")
        buf.write("\2\2\2T\u0167\3\2\2\2V\u016e\3\2\2\2X\u0175\3\2\2\2Z\u0177")
        buf.write("\3\2\2\2\\\u0183\3\2\2\2^\u018f\3\2\2\2`\u019e\3\2\2\2")
        buf.write("b\u01a3\3\2\2\2d\u01a5\3\2\2\2f\u01b4\3\2\2\2h\u01b9\3")
        buf.write("\2\2\2j\u01bb\3\2\2\2l\u01c5\3\2\2\2n\u01c7\3\2\2\2p\u01cf")
        buf.write("\3\2\2\2r\u01d1\3\2\2\2t\u01da\3\2\2\2v\u01dc\3\2\2\2")
        buf.write("x\u01de\3\2\2\2z\u01e0\3\2\2\2|\u01e2\3\2\2\2~\177\5\b")
        buf.write("\5\2\177\u0080\5\4\3\2\u0080\u0081\5\b\5\2\u0081\u0082")
        buf.write("\7\2\2\3\u0082\3\3\2\2\2\u0083\u0086\5\n\6\2\u0084\u0086")
        buf.write("\5\60\31\2\u0085\u0083\3\2\2\2\u0085\u0084\3\2\2\2\u0086")
        buf.write("\5\3\2\2\2\u0087\u0088\7\4\2\2\u0088\u008b\5\b\5\2\u0089")
        buf.write("\u008b\7\4\2\2\u008a\u0087\3\2\2\2\u008a\u0089\3\2\2\2")
        buf.write("\u008b\7\3\2\2\2\u008c\u008d\7\4\2\2\u008d\u0090\5\b\5")
        buf.write("\2\u008e\u0090\3\2\2\2\u008f\u008c\3\2\2\2\u008f\u008e")
        buf.write("\3\2\2\2\u0090\t\3\2\2\2\u0091\u0092\5\f\7\2\u0092\u0093")
        buf.write("\5\n\6\2\u0093\u0096\3\2\2\2\u0094\u0096\5\f\7\2\u0095")
        buf.write("\u0091\3\2\2\2\u0095\u0094\3\2\2\2\u0096\13\3\2\2\2\u0097")
        buf.write("\u0098\5\16\b\2\u0098\u0099\5\b\5\2\u0099\r\3\2\2\2\u009a")
        buf.write("\u009d\5\20\t\2\u009b\u009d\5$\23\2\u009c\u009a\3\2\2")
        buf.write("\2\u009c\u009b\3\2\2\2\u009d\17\3\2\2\2\u009e\u00a2\5")
        buf.write("\22\n\2\u009f\u00a2\5\26\f\2\u00a0\u00a2\5\34\17\2\u00a1")
        buf.write("\u009e\3\2\2\2\u00a1\u009f\3\2\2\2\u00a1\u00a0\3\2\2\2")
        buf.write("\u00a2\21\3\2\2\2\u00a3\u00a4\5\24\13\2\u00a4\u00a7\7")
        buf.write("\64\2\2\u00a5\u00a6\7\"\2\2\u00a6\u00a8\5V,\2\u00a7\u00a5")
        buf.write("\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\23\3\2\2\2\u00a9\u00aa")
        buf.write("\t\2\2\2\u00aa\25\3\2\2\2\u00ab\u00ae\5\30\r\2\u00ac\u00ae")
        buf.write("\5\32\16\2\u00ad\u00ab\3\2\2\2\u00ad\u00ac\3\2\2\2\u00ae")
        buf.write("\27\3\2\2\2\u00af\u00b0\7\f\2\2\u00b0\u00b1\7\64\2\2\u00b1")
        buf.write("\u00b2\7\"\2\2\u00b2\u00b3\5V,\2\u00b3\31\3\2\2\2\u00b4")
        buf.write("\u00b5\7\r\2\2\u00b5\u00b8\7\64\2\2\u00b6\u00b7\7\"\2")
        buf.write("\2\u00b7\u00b9\5V,\2\u00b8\u00b6\3\2\2\2\u00b8\u00b9\3")
        buf.write("\2\2\2\u00b9\33\3\2\2\2\u00ba\u00bb\5\24\13\2\u00bb\u00bc")
        buf.write("\7\64\2\2\u00bc\u00bf\5\36\20\2\u00bd\u00be\7\"\2\2\u00be")
        buf.write("\u00c0\5V,\2\u00bf\u00bd\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0")
        buf.write("\35\3\2\2\2\u00c1\u00c2\7,\2\2\u00c2\u00c3\5 \21\2\u00c3")
        buf.write("\u00c4\7-\2\2\u00c4\37\3\2\2\2\u00c5\u00c6\7/\2\2\u00c6")
        buf.write("\u00c9\5\"\22\2\u00c7\u00c9\7/\2\2\u00c8\u00c5\3\2\2\2")
        buf.write("\u00c8\u00c7\3\2\2\2\u00c9!\3\2\2\2\u00ca\u00cb\7.\2\2")
        buf.write("\u00cb\u00cc\7/\2\2\u00cc\u00cf\5\"\22\2\u00cd\u00cf\3")
        buf.write("\2\2\2\u00ce\u00ca\3\2\2\2\u00ce\u00cd\3\2\2\2\u00cf#")
        buf.write("\3\2\2\2\u00d0\u00d1\7\16\2\2\u00d1\u00d2\7\64\2\2\u00d2")
        buf.write("\u00d3\5&\24\2\u00d3\u00d4\5\b\5\2\u00d4\u00d5\5.\30\2")
        buf.write("\u00d5%\3\2\2\2\u00d6\u00d7\7*\2\2\u00d7\u00d8\5(\25\2")
        buf.write("\u00d8\u00d9\7+\2\2\u00d9\'\3\2\2\2\u00da\u00db\5,\27")
        buf.write("\2\u00db\u00dc\5*\26\2\u00dc\u00df\3\2\2\2\u00dd\u00df")
        buf.write("\3\2\2\2\u00de\u00da\3\2\2\2\u00de\u00dd\3\2\2\2\u00df")
        buf.write(")\3\2\2\2\u00e0\u00e1\7.\2\2\u00e1\u00e2\5,\27\2\u00e2")
        buf.write("\u00e3\5*\26\2\u00e3\u00e6\3\2\2\2\u00e4\u00e6\3\2\2\2")
        buf.write("\u00e5\u00e0\3\2\2\2\u00e5\u00e4\3\2\2\2\u00e6+\3\2\2")
        buf.write("\2\u00e7\u00e8\5\24\13\2\u00e8\u00e9\7\64\2\2\u00e9\u00ef")
        buf.write("\3\2\2\2\u00ea\u00eb\5\24\13\2\u00eb\u00ec\7\64\2\2\u00ec")
        buf.write("\u00ed\5\36\20\2\u00ed\u00ef\3\2\2\2\u00ee\u00e7\3\2\2")
        buf.write("\2\u00ee\u00ea\3\2\2\2\u00ef-\3\2\2\2\u00f0\u00f4\5H%")
        buf.write("\2\u00f1\u00f4\5P)\2\u00f2\u00f4\3\2\2\2\u00f3\u00f0\3")
        buf.write("\2\2\2\u00f3\u00f1\3\2\2\2\u00f3\u00f2\3\2\2\2\u00f4/")
        buf.write("\3\2\2\2\u00f5\u00f6\5\62\32\2\u00f6\u00f7\5\60\31\2\u00f7")
        buf.write("\u00fa\3\2\2\2\u00f8\u00fa\5\62\32\2\u00f9\u00f5\3\2\2")
        buf.write("\2\u00f9\u00f8\3\2\2\2\u00fa\61\3\2\2\2\u00fb\u00fc\5")
        buf.write("\64\33\2\u00fc\u00fd\5\b\5\2\u00fd\63\3\2\2\2\u00fe\u0108")
        buf.write("\5\20\t\2\u00ff\u0108\5\66\34\2\u0100\u0108\5:\36\2\u0101")
        buf.write("\u0108\5B\"\2\u0102\u0108\5H%\2\u0103\u0108\5J&\2\u0104")
        buf.write("\u0108\5P)\2\u0105\u0108\5D#\2\u0106\u0108\5F$\2\u0107")
        buf.write("\u00fe\3\2\2\2\u0107\u00ff\3\2\2\2\u0107\u0100\3\2\2\2")
        buf.write("\u0107\u0101\3\2\2\2\u0107\u0102\3\2\2\2\u0107\u0103\3")
        buf.write("\2\2\2\u0107\u0104\3\2\2\2\u0107\u0105\3\2\2\2\u0107\u0106")
        buf.write("\3\2\2\2\u0108\65\3\2\2\2\u0109\u010a\58\35\2\u010a\u010b")
        buf.write("\7\"\2\2\u010b\u010c\5V,\2\u010c\u010d\5\6\4\2\u010d\67")
        buf.write("\3\2\2\2\u010e\u0113\7\64\2\2\u010f\u0110\5V,\2\u0110")
        buf.write("\u0111\5r:\2\u0111\u0113\3\2\2\2\u0112\u010e\3\2\2\2\u0112")
        buf.write("\u010f\3\2\2\2\u01139\3\2\2\2\u0114\u0115\7\24\2\2\u0115")
        buf.write("\u0116\7*\2\2\u0116\u0117\5V,\2\u0117\u0118\7+\2\2\u0118")
        buf.write("\u0119\5\b\5\2\u0119\u011a\5\64\33\2\u011a\u011b\5\b\5")
        buf.write("\2\u011b\u011c\5<\37\2\u011c\u011d\5@!\2\u011d;\3\2\2")
        buf.write("\2\u011e\u011f\5> \2\u011f\u0120\5<\37\2\u0120\u0123\3")
        buf.write("\2\2\2\u0121\u0123\3\2\2\2\u0122\u011e\3\2\2\2\u0122\u0121")
        buf.write("\3\2\2\2\u0123=\3\2\2\2\u0124\u0125\7\26\2\2\u0125\u0126")
        buf.write("\7*\2\2\u0126\u0127\5V,\2\u0127\u0128\7+\2\2\u0128\u0129")
        buf.write("\5\b\5\2\u0129\u012a\5\62\32\2\u012a?\3\2\2\2\u012b\u012c")
        buf.write("\7\25\2\2\u012c\u012d\5\b\5\2\u012d\u012e\5\62\32\2\u012e")
        buf.write("\u0131\3\2\2\2\u012f\u0131\3\2\2\2\u0130\u012b\3\2\2\2")
        buf.write("\u0130\u012f\3\2\2\2\u0131A\3\2\2\2\u0132\u0133\7\17\2")
        buf.write("\2\u0133\u0134\7\64\2\2\u0134\u0135\7\20\2\2\u0135\u0136")
        buf.write("\5V,\2\u0136\u0137\7\21\2\2\u0137\u0138\5V,\2\u0138\u0139")
        buf.write("\5\b\5\2\u0139\u013a\5\62\32\2\u013aC\3\2\2\2\u013b\u013c")
        buf.write("\7\22\2\2\u013c\u013d\5\6\4\2\u013dE\3\2\2\2\u013e\u013f")
        buf.write("\7\23\2\2\u013f\u0140\5\6\4\2\u0140G\3\2\2\2\u0141\u0142")
        buf.write("\7\13\2\2\u0142\u0146\5V,\2\u0143\u0144\7\13\2\2\u0144")
        buf.write("\u0146\5\6\4\2\u0145\u0141\3\2\2\2\u0145\u0143\3\2\2\2")
        buf.write("\u0146I\3\2\2\2\u0147\u0148\7\64\2\2\u0148\u0149\7*\2")
        buf.write("\2\u0149\u014a\5L\'\2\u014a\u014b\7+\2\2\u014bK\3\2\2")
        buf.write("\2\u014c\u014d\5V,\2\u014d\u014e\5N(\2\u014e\u0151\3\2")
        buf.write("\2\2\u014f\u0151\3\2\2\2\u0150\u014c\3\2\2\2\u0150\u014f")
        buf.write("\3\2\2\2\u0151M\3\2\2\2\u0152\u0153\7.\2\2\u0153\u0154")
        buf.write("\5V,\2\u0154\u0155\5N(\2\u0155\u0158\3\2\2\2\u0156\u0158")
        buf.write("\3\2\2\2\u0157\u0152\3\2\2\2\u0157\u0156\3\2\2\2\u0158")
        buf.write("O\3\2\2\2\u0159\u015a\7\27\2\2\u015a\u015b\5\6\4\2\u015b")
        buf.write("\u015c\5R*\2\u015c\u015d\7\30\2\2\u015d\u015e\5\6\4\2")
        buf.write("\u015eQ\3\2\2\2\u015f\u0162\5T+\2\u0160\u0162\3\2\2\2")
        buf.write("\u0161\u015f\3\2\2\2\u0161\u0160\3\2\2\2\u0162S\3\2\2")
        buf.write("\2\u0163\u0164\5\62\32\2\u0164\u0165\5T+\2\u0165\u0168")
        buf.write("\3\2\2\2\u0166\u0168\5\62\32\2\u0167\u0163\3\2\2\2\u0167")
        buf.write("\u0166\3\2\2\2\u0168U\3\2\2\2\u0169\u016a\5X-\2\u016a")
        buf.write("\u016b\7(\2\2\u016b\u016c\5X-\2\u016c\u016f\3\2\2\2\u016d")
        buf.write("\u016f\5X-\2\u016e\u0169\3\2\2\2\u016e\u016d\3\2\2\2\u016f")
        buf.write("W\3\2\2\2\u0170\u0171\5Z.\2\u0171\u0172\5|?\2\u0172\u0173")
        buf.write("\5Z.\2\u0173\u0176\3\2\2\2\u0174\u0176\5Z.\2\u0175\u0170")
        buf.write("\3\2\2\2\u0175\u0174\3\2\2\2\u0176Y\3\2\2\2\u0177\u0178")
        buf.write("\b.\1\2\u0178\u0179\5\\/\2\u0179\u0180\3\2\2\2\u017a\u017b")
        buf.write("\f\4\2\2\u017b\u017c\5z>\2\u017c\u017d\5\\/\2\u017d\u017f")
        buf.write("\3\2\2\2\u017e\u017a\3\2\2\2\u017f\u0182\3\2\2\2\u0180")
        buf.write("\u017e\3\2\2\2\u0180\u0181\3\2\2\2\u0181[\3\2\2\2\u0182")
        buf.write("\u0180\3\2\2\2\u0183\u0184\b/\1\2\u0184\u0185\5^\60\2")
        buf.write("\u0185\u018c\3\2\2\2\u0186\u0187\f\4\2\2\u0187\u0188\5")
        buf.write("x=\2\u0188\u0189\5^\60\2\u0189\u018b\3\2\2\2\u018a\u0186")
        buf.write("\3\2\2\2\u018b\u018e\3\2\2\2\u018c\u018a\3\2\2\2\u018c")
        buf.write("\u018d\3\2\2\2\u018d]\3\2\2\2\u018e\u018c\3\2\2\2\u018f")
        buf.write("\u0190\b\60\1\2\u0190\u0191\5`\61\2\u0191\u0198\3\2\2")
        buf.write("\2\u0192\u0193\f\4\2\2\u0193\u0194\5v<\2\u0194\u0195\5")
        buf.write("`\61\2\u0195\u0197\3\2\2\2\u0196\u0192\3\2\2\2\u0197\u019a")
        buf.write("\3\2\2\2\u0198\u0196\3\2\2\2\u0198\u0199\3\2\2\2\u0199")
        buf.write("_\3\2\2\2\u019a\u0198\3\2\2\2\u019b\u019c\7\31\2\2\u019c")
        buf.write("\u019f\5`\61\2\u019d\u019f\5b\62\2\u019e\u019b\3\2\2\2")
        buf.write("\u019e\u019d\3\2\2\2\u019fa\3\2\2\2\u01a0\u01a1\7\35\2")
        buf.write("\2\u01a1\u01a4\5b\62\2\u01a2\u01a4\5d\63\2\u01a3\u01a0")
        buf.write("\3\2\2\2\u01a3\u01a2\3\2\2\2\u01a4c\3\2\2\2\u01a5\u01a6")
        buf.write("\b\63\1\2\u01a6\u01a7\5f\64\2\u01a7\u01ac\3\2\2\2\u01a8")
        buf.write("\u01a9\f\4\2\2\u01a9\u01ab\5r:\2\u01aa\u01a8\3\2\2\2\u01ab")
        buf.write("\u01ae\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ac\u01ad\3\2\2\2")
        buf.write("\u01ade\3\2\2\2\u01ae\u01ac\3\2\2\2\u01af\u01b0\7*\2\2")
        buf.write("\u01b0\u01b1\5V,\2\u01b1\u01b2\7+\2\2\u01b2\u01b5\3\2")
        buf.write("\2\2\u01b3\u01b5\5h\65\2\u01b4\u01af\3\2\2\2\u01b4\u01b3")
        buf.write("\3\2\2\2\u01b5g\3\2\2\2\u01b6\u01ba\7\64\2\2\u01b7\u01ba")
        buf.write("\5l\67\2\u01b8\u01ba\5j\66\2\u01b9\u01b6\3\2\2\2\u01b9")
        buf.write("\u01b7\3\2\2\2\u01b9\u01b8\3\2\2\2\u01bai\3\2\2\2\u01bb")
        buf.write("\u01bc\7\64\2\2\u01bc\u01bd\7*\2\2\u01bd\u01be\5L\'\2")
        buf.write("\u01be\u01bf\7+\2\2\u01bfk\3\2\2\2\u01c0\u01c6\7/\2\2")
        buf.write("\u01c1\u01c6\7\6\2\2\u01c2\u01c6\7\7\2\2\u01c3\u01c6\7")
        buf.write("\61\2\2\u01c4\u01c6\5n8\2\u01c5\u01c0\3\2\2\2\u01c5\u01c1")
        buf.write("\3\2\2\2\u01c5\u01c2\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c5")
        buf.write("\u01c4\3\2\2\2\u01c6m\3\2\2\2\u01c7\u01c8\7,\2\2\u01c8")
        buf.write("\u01c9\5p9\2\u01c9\u01ca\7-\2\2\u01cao\3\2\2\2\u01cb\u01cc")
        buf.write("\5V,\2\u01cc\u01cd\5N(\2\u01cd\u01d0\3\2\2\2\u01ce\u01d0")
        buf.write("\5V,\2\u01cf\u01cb\3\2\2\2\u01cf\u01ce\3\2\2\2\u01d0q")
        buf.write("\3\2\2\2\u01d1\u01d2\7,\2\2\u01d2\u01d3\5t;\2\u01d3\u01d4")
        buf.write("\7-\2\2\u01d4s\3\2\2\2\u01d5\u01db\5V,\2\u01d6\u01d7\5")
        buf.write("V,\2\u01d7\u01d8\7.\2\2\u01d8\u01d9\5t;\2\u01d9\u01db")
        buf.write("\3\2\2\2\u01da\u01d5\3\2\2\2\u01da\u01d6\3\2\2\2\u01db")
        buf.write("u\3\2\2\2\u01dc\u01dd\t\3\2\2\u01ddw\3\2\2\2\u01de\u01df")
        buf.write("\t\4\2\2\u01dfy\3\2\2\2\u01e0\u01e1\t\5\2\2\u01e1{\3\2")
        buf.write("\2\2\u01e2\u01e3\t\6\2\2\u01e3}\3\2\2\2)\u0085\u008a\u008f")
        buf.write("\u0095\u009c\u00a1\u00a7\u00ad\u00b8\u00bf\u00c8\u00ce")
        buf.write("\u00de\u00e5\u00ee\u00f3\u00f9\u0107\u0112\u0122\u0130")
        buf.write("\u0145\u0150\u0157\u0161\u0167\u016e\u0175\u0180\u018c")
        buf.write("\u0198\u019e\u01a3\u01ac\u01b4\u01b9\u01c5\u01cf\u01da")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'true'", "'false'", "'number'", "'bool'", "'string'", 
                     "'return'", "'var'", "'dynamic'", "'func'", "'for'", 
                     "'until'", "'by'", "'break'", "'continue'", "'if'", 
                     "'else'", "'elif'", "'begin'", "'end'", "'not'", "'and'", 
                     "'or'", "'+'", "'-'", "'*'", "'/'", "'%'", "'='", "'<-'", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "'...'", "'=='", 
                     "'('", "')'", "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>", "WS", "NEWLINE", "COMMENT", "TRUE", "FALSE", 
                      "NUMBER", "BOOL", "STRING", "RETURN", "VAR", "DYNAMIC", 
                      "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
                      "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", 
                      "OR", "ADD_OP", "SUBTR_OP", "MUL_OP", "DIV_OP", "REMAINDER_OP", 
                      "EQUAL", "ASSIGN", "NOT_EQUAL", "SMALLER", "SMALLER_OR_EQUAL", 
                      "GREATER", "GREATER_OR_EQUAL", "SPREAD_OP", "EQUAL_STR", 
                      "LP", "RP", "LB", "RB", "COMMA", "NUM_LIT", "BOOL_LIT", 
                      "STRING_LIT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "IDENTIFIER", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_program_line = 1
    RULE_compulsory_newline = 2
    RULE_optional_newline = 3
    RULE_decl_list = 4
    RULE_decl = 5
    RULE_decl_type = 6
    RULE_var_decl = 7
    RULE_explicit_decl = 8
    RULE_primitive_type = 9
    RULE_implicit_decl = 10
    RULE_implicit_var = 11
    RULE_implicit_dynamic = 12
    RULE_array_decl = 13
    RULE_size_decl = 14
    RULE_size_list = 15
    RULE_tail_size = 16
    RULE_func_decl = 17
    RULE_passed_para = 18
    RULE_para_list = 19
    RULE_tail_para = 20
    RULE_parameter = 21
    RULE_body_func = 22
    RULE_stmt_list = 23
    RULE_statement = 24
    RULE_stmt_type = 25
    RULE_assign_stmt = 26
    RULE_lhs = 27
    RULE_if_stmt = 28
    RULE_elif_list = 29
    RULE_elif_stmt = 30
    RULE_else_stmt = 31
    RULE_for_stmt = 32
    RULE_break_stmt = 33
    RULE_continue_stmt = 34
    RULE_return_stmt = 35
    RULE_func_call_stmt = 36
    RULE_expr_list = 37
    RULE_tail_expr = 38
    RULE_block_stmt = 39
    RULE_body_block = 40
    RULE_block_stmt_list = 41
    RULE_expr = 42
    RULE_expr1 = 43
    RULE_expr2 = 44
    RULE_expr3 = 45
    RULE_expr4 = 46
    RULE_expr5 = 47
    RULE_expr6 = 48
    RULE_expr7 = 49
    RULE_expr8 = 50
    RULE_operand = 51
    RULE_func_call_expr = 52
    RULE_literal = 53
    RULE_array_lit = 54
    RULE_comp_expr_list = 55
    RULE_index_expr = 56
    RULE_index_operator = 57
    RULE_mul_div_rem = 58
    RULE_add_subtr = 59
    RULE_and_or = 60
    RULE_relational_op = 61

    ruleNames =  [ "program", "program_line", "compulsory_newline", "optional_newline", 
                   "decl_list", "decl", "decl_type", "var_decl", "explicit_decl", 
                   "primitive_type", "implicit_decl", "implicit_var", "implicit_dynamic", 
                   "array_decl", "size_decl", "size_list", "tail_size", 
                   "func_decl", "passed_para", "para_list", "tail_para", 
                   "parameter", "body_func", "stmt_list", "statement", "stmt_type", 
                   "assign_stmt", "lhs", "if_stmt", "elif_list", "elif_stmt", 
                   "else_stmt", "for_stmt", "break_stmt", "continue_stmt", 
                   "return_stmt", "func_call_stmt", "expr_list", "tail_expr", 
                   "block_stmt", "body_block", "block_stmt_list", "expr", 
                   "expr1", "expr2", "expr3", "expr4", "expr5", "expr6", 
                   "expr7", "expr8", "operand", "func_call_expr", "literal", 
                   "array_lit", "comp_expr_list", "index_expr", "index_operator", 
                   "mul_div_rem", "add_subtr", "and_or", "relational_op" ]

    EOF = Token.EOF
    WS=1
    NEWLINE=2
    COMMENT=3
    TRUE=4
    FALSE=5
    NUMBER=6
    BOOL=7
    STRING=8
    RETURN=9
    VAR=10
    DYNAMIC=11
    FUNC=12
    FOR=13
    UNTIL=14
    BY=15
    BREAK=16
    CONTINUE=17
    IF=18
    ELSE=19
    ELIF=20
    BEGIN=21
    END=22
    NOT=23
    AND=24
    OR=25
    ADD_OP=26
    SUBTR_OP=27
    MUL_OP=28
    DIV_OP=29
    REMAINDER_OP=30
    EQUAL=31
    ASSIGN=32
    NOT_EQUAL=33
    SMALLER=34
    SMALLER_OR_EQUAL=35
    GREATER=36
    GREATER_OR_EQUAL=37
    SPREAD_OP=38
    EQUAL_STR=39
    LP=40
    RP=41
    LB=42
    RB=43
    COMMA=44
    NUM_LIT=45
    BOOL_LIT=46
    STRING_LIT=47
    UNCLOSE_STRING=48
    ILLEGAL_ESCAPE=49
    IDENTIFIER=50
    ERROR_CHAR=51

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def optional_newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Optional_newlineContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Optional_newlineContext,i)


        def program_line(self):
            return self.getTypedRuleContext(ZCodeParser.Program_lineContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.optional_newline()
            self.state = 125
            self.program_line()
            self.state = 126
            self.optional_newline()
            self.state = 127
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Program_lineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl_list(self):
            return self.getTypedRuleContext(ZCodeParser.Decl_listContext,0)


        def stmt_list(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_program_line

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram_line" ):
                return visitor.visitProgram_line(self)
            else:
                return visitor.visitChildren(self)




    def program_line(self):

        localctx = ZCodeParser.Program_lineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_program_line)
        try:
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.decl_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                self.stmt_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Compulsory_newlineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def optional_newline(self):
            return self.getTypedRuleContext(ZCodeParser.Optional_newlineContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_compulsory_newline

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompulsory_newline" ):
                return visitor.visitCompulsory_newline(self)
            else:
                return visitor.visitChildren(self)




    def compulsory_newline(self):

        localctx = ZCodeParser.Compulsory_newlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_compulsory_newline)
        try:
            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.match(ZCodeParser.NEWLINE)
                self.state = 134
                self.optional_newline()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 135
                self.match(ZCodeParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Optional_newlineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def optional_newline(self):
            return self.getTypedRuleContext(ZCodeParser.Optional_newlineContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_optional_newline

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOptional_newline" ):
                return visitor.visitOptional_newline(self)
            else:
                return visitor.visitChildren(self)




    def optional_newline(self):

        localctx = ZCodeParser.Optional_newlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_optional_newline)
        try:
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.match(ZCodeParser.NEWLINE)
                self.state = 139
                self.optional_newline()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(ZCodeParser.DeclContext,0)


        def decl_list(self):
            return self.getTypedRuleContext(ZCodeParser.Decl_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decl_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_list" ):
                return visitor.visitDecl_list(self)
            else:
                return visitor.visitChildren(self)




    def decl_list(self):

        localctx = ZCodeParser.Decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_decl_list)
        try:
            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.decl()
                self.state = 144
                self.decl_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl_type(self):
            return self.getTypedRuleContext(ZCodeParser.Decl_typeContext,0)


        def optional_newline(self):
            return self.getTypedRuleContext(ZCodeParser.Optional_newlineContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = ZCodeParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.decl_type()
            self.state = 150
            self.optional_newline()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Var_declContext,0)


        def func_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Func_declContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decl_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_type" ):
                return visitor.visitDecl_type(self)
            else:
                return visitor.visitChildren(self)




    def decl_type(self):

        localctx = ZCodeParser.Decl_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_decl_type)
        try:
            self.state = 154
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.var_decl()
                pass
            elif token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 153
                self.func_decl()
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


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def explicit_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Explicit_declContext,0)


        def implicit_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Implicit_declContext,0)


        def array_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Array_declContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = ZCodeParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_var_decl)
        try:
            self.state = 159
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.explicit_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                self.implicit_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 158
                self.array_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Explicit_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(ZCodeParser.Primitive_typeContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_explicit_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExplicit_decl" ):
                return visitor.visitExplicit_decl(self)
            else:
                return visitor.visitChildren(self)




    def explicit_decl(self):

        localctx = ZCodeParser.Explicit_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_explicit_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.primitive_type()
            self.state = 162
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN:
                self.state = 163
                self.match(ZCodeParser.ASSIGN)
                self.state = 164
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_primitive_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = ZCodeParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
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


    class Implicit_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def implicit_var(self):
            return self.getTypedRuleContext(ZCodeParser.Implicit_varContext,0)


        def implicit_dynamic(self):
            return self.getTypedRuleContext(ZCodeParser.Implicit_dynamicContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_implicit_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplicit_decl" ):
                return visitor.visitImplicit_decl(self)
            else:
                return visitor.visitChildren(self)




    def implicit_decl(self):

        localctx = ZCodeParser.Implicit_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_implicit_decl)
        try:
            self.state = 171
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.implicit_var()
                pass
            elif token in [ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                self.implicit_dynamic()
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


    class Implicit_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_implicit_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplicit_var" ):
                return visitor.visitImplicit_var(self)
            else:
                return visitor.visitChildren(self)




    def implicit_var(self):

        localctx = ZCodeParser.Implicit_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_implicit_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(ZCodeParser.VAR)
            self.state = 174
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 175
            self.match(ZCodeParser.ASSIGN)
            self.state = 176
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Implicit_dynamicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_implicit_dynamic

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplicit_dynamic" ):
                return visitor.visitImplicit_dynamic(self)
            else:
                return visitor.visitChildren(self)




    def implicit_dynamic(self):

        localctx = ZCodeParser.Implicit_dynamicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_implicit_dynamic)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(ZCodeParser.DYNAMIC)
            self.state = 179
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN:
                self.state = 180
                self.match(ZCodeParser.ASSIGN)
                self.state = 181
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(ZCodeParser.Primitive_typeContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def size_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Size_declContext,0)


        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_decl" ):
                return visitor.visitArray_decl(self)
            else:
                return visitor.visitChildren(self)




    def array_decl(self):

        localctx = ZCodeParser.Array_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_array_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.primitive_type()
            self.state = 185
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 186
            self.size_decl()
            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN:
                self.state = 187
                self.match(ZCodeParser.ASSIGN)
                self.state = 188
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Size_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def size_list(self):
            return self.getTypedRuleContext(ZCodeParser.Size_listContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_size_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSize_decl" ):
                return visitor.visitSize_decl(self)
            else:
                return visitor.visitChildren(self)




    def size_decl(self):

        localctx = ZCodeParser.Size_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_size_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(ZCodeParser.LB)
            self.state = 192
            self.size_list()
            self.state = 193
            self.match(ZCodeParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Size_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM_LIT(self):
            return self.getToken(ZCodeParser.NUM_LIT, 0)

        def tail_size(self):
            return self.getTypedRuleContext(ZCodeParser.Tail_sizeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_size_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSize_list" ):
                return visitor.visitSize_list(self)
            else:
                return visitor.visitChildren(self)




    def size_list(self):

        localctx = ZCodeParser.Size_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_size_list)
        try:
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.match(ZCodeParser.NUM_LIT)
                self.state = 196
                self.tail_size()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 197
                self.match(ZCodeParser.NUM_LIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tail_sizeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def NUM_LIT(self):
            return self.getToken(ZCodeParser.NUM_LIT, 0)

        def tail_size(self):
            return self.getTypedRuleContext(ZCodeParser.Tail_sizeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_tail_size

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTail_size" ):
                return visitor.visitTail_size(self)
            else:
                return visitor.visitChildren(self)




    def tail_size(self):

        localctx = ZCodeParser.Tail_sizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_tail_size)
        try:
            self.state = 204
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.match(ZCodeParser.COMMA)
                self.state = 201
                self.match(ZCodeParser.NUM_LIT)
                self.state = 202
                self.tail_size()
                pass
            elif token in [ZCodeParser.RB]:
                self.enterOuterAlt(localctx, 2)

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


    class Func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def passed_para(self):
            return self.getTypedRuleContext(ZCodeParser.Passed_paraContext,0)


        def optional_newline(self):
            return self.getTypedRuleContext(ZCodeParser.Optional_newlineContext,0)


        def body_func(self):
            return self.getTypedRuleContext(ZCodeParser.Body_funcContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl" ):
                return visitor.visitFunc_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_decl(self):

        localctx = ZCodeParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_func_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(ZCodeParser.FUNC)
            self.state = 207
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 208
            self.passed_para()
            self.state = 209
            self.optional_newline()
            self.state = 210
            self.body_func()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Passed_paraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def para_list(self):
            return self.getTypedRuleContext(ZCodeParser.Para_listContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_passed_para

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPassed_para" ):
                return visitor.visitPassed_para(self)
            else:
                return visitor.visitChildren(self)




    def passed_para(self):

        localctx = ZCodeParser.Passed_paraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_passed_para)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(ZCodeParser.LP)
            self.state = 213
            self.para_list()
            self.state = 214
            self.match(ZCodeParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Para_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self):
            return self.getTypedRuleContext(ZCodeParser.ParameterContext,0)


        def tail_para(self):
            return self.getTypedRuleContext(ZCodeParser.Tail_paraContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_para_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara_list" ):
                return visitor.visitPara_list(self)
            else:
                return visitor.visitChildren(self)




    def para_list(self):

        localctx = ZCodeParser.Para_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_para_list)
        try:
            self.state = 220
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self.parameter()
                self.state = 217
                self.tail_para()
                pass
            elif token in [ZCodeParser.RP]:
                self.enterOuterAlt(localctx, 2)

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


    class Tail_paraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def parameter(self):
            return self.getTypedRuleContext(ZCodeParser.ParameterContext,0)


        def tail_para(self):
            return self.getTypedRuleContext(ZCodeParser.Tail_paraContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_tail_para

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTail_para" ):
                return visitor.visitTail_para(self)
            else:
                return visitor.visitChildren(self)




    def tail_para(self):

        localctx = ZCodeParser.Tail_paraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_tail_para)
        try:
            self.state = 227
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 222
                self.match(ZCodeParser.COMMA)
                self.state = 223
                self.parameter()
                self.state = 224
                self.tail_para()
                pass
            elif token in [ZCodeParser.RP]:
                self.enterOuterAlt(localctx, 2)

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


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(ZCodeParser.Primitive_typeContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def size_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Size_declContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = ZCodeParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_parameter)
        try:
            self.state = 236
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 229
                self.primitive_type()
                self.state = 230
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 232
                self.primitive_type()
                self.state = 233
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 234
                self.size_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Body_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def return_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Return_stmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_body_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody_func" ):
                return visitor.visitBody_func(self)
            else:
                return visitor.visitChildren(self)




    def body_func(self):

        localctx = ZCodeParser.Body_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_body_func)
        try:
            self.state = 241
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.return_stmt()
                pass
            elif token in [ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
                self.block_stmt()
                pass
            elif token in [ZCodeParser.EOF, ZCodeParser.NEWLINE, ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 3)

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


    class Stmt_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def stmt_list(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_list" ):
                return visitor.visitStmt_list(self)
            else:
                return visitor.visitChildren(self)




    def stmt_list(self):

        localctx = ZCodeParser.Stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_stmt_list)
        try:
            self.state = 247
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                self.statement()
                self.state = 244
                self.stmt_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 246
                self.statement()
                pass


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

        def stmt_type(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_typeContext,0)


        def optional_newline(self):
            return self.getTypedRuleContext(ZCodeParser.Optional_newlineContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ZCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.stmt_type()
            self.state = 250
            self.optional_newline()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Var_declContext,0)


        def assign_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Assign_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.For_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Return_stmtContext,0)


        def func_call_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Func_call_stmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Continue_stmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_type" ):
                return visitor.visitStmt_type(self)
            else:
                return visitor.visitChildren(self)




    def stmt_type(self):

        localctx = ZCodeParser.Stmt_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_stmt_type)
        try:
            self.state = 261
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 252
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 253
                self.assign_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 254
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 255
                self.for_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 256
                self.return_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 257
                self.func_call_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 258
                self.block_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 259
                self.break_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 260
                self.continue_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(ZCodeParser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def compulsory_newline(self):
            return self.getTypedRuleContext(ZCodeParser.Compulsory_newlineContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = ZCodeParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.lhs()
            self.state = 264
            self.match(ZCodeParser.ASSIGN)
            self.state = 265
            self.expr()
            self.state = 266
            self.compulsory_newline()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def index_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Index_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = ZCodeParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_lhs)
        try:
            self.state = 272
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 268
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 269
                self.expr()
                self.state = 270
                self.index_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def optional_newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Optional_newlineContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Optional_newlineContext,i)


        def stmt_type(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_typeContext,0)


        def elif_list(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_listContext,0)


        def else_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Else_stmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = ZCodeParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(ZCodeParser.IF)
            self.state = 275
            self.match(ZCodeParser.LP)
            self.state = 276
            self.expr()
            self.state = 277
            self.match(ZCodeParser.RP)
            self.state = 278
            self.optional_newline()
            self.state = 279
            self.stmt_type()
            self.state = 280
            self.optional_newline()
            self.state = 281
            self.elif_list()
            self.state = 282
            self.else_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elif_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_stmtContext,0)


        def elif_list(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_list" ):
                return visitor.visitElif_list(self)
            else:
                return visitor.visitChildren(self)




    def elif_list(self):

        localctx = ZCodeParser.Elif_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_elif_list)
        try:
            self.state = 288
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 284
                self.elif_stmt()
                self.state = 285
                self.elif_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def optional_newline(self):
            return self.getTypedRuleContext(ZCodeParser.Optional_newlineContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_stmt" ):
                return visitor.visitElif_stmt(self)
            else:
                return visitor.visitChildren(self)




    def elif_stmt(self):

        localctx = ZCodeParser.Elif_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_elif_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.match(ZCodeParser.ELIF)
            self.state = 291
            self.match(ZCodeParser.LP)
            self.state = 292
            self.expr()
            self.state = 293
            self.match(ZCodeParser.RP)
            self.state = 294
            self.optional_newline()
            self.state = 295
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def optional_newline(self):
            return self.getTypedRuleContext(ZCodeParser.Optional_newlineContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_else_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_stmt" ):
                return visitor.visitElse_stmt(self)
            else:
                return visitor.visitChildren(self)




    def else_stmt(self):

        localctx = ZCodeParser.Else_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_else_stmt)
        try:
            self.state = 302
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 297
                self.match(ZCodeParser.ELSE)
                self.state = 298
                self.optional_newline()
                self.state = 299
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def optional_newline(self):
            return self.getTypedRuleContext(ZCodeParser.Optional_newlineContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = ZCodeParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.match(ZCodeParser.FOR)
            self.state = 305
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 306
            self.match(ZCodeParser.UNTIL)
            self.state = 307
            self.expr()
            self.state = 308
            self.match(ZCodeParser.BY)
            self.state = 309
            self.expr()
            self.state = 310
            self.optional_newline()
            self.state = 311
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def compulsory_newline(self):
            return self.getTypedRuleContext(ZCodeParser.Compulsory_newlineContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = ZCodeParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.match(ZCodeParser.BREAK)
            self.state = 314
            self.compulsory_newline()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def compulsory_newline(self):
            return self.getTypedRuleContext(ZCodeParser.Compulsory_newlineContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = ZCodeParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.match(ZCodeParser.CONTINUE)
            self.state = 317
            self.compulsory_newline()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def compulsory_newline(self):
            return self.getTypedRuleContext(ZCodeParser.Compulsory_newlineContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = ZCodeParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_return_stmt)
        try:
            self.state = 323
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 319
                self.match(ZCodeParser.RETURN)
                self.state = 320
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 321
                self.match(ZCodeParser.RETURN)
                self.state = 322
                self.compulsory_newline()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def expr_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_listContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_func_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call_stmt" ):
                return visitor.visitFunc_call_stmt(self)
            else:
                return visitor.visitChildren(self)




    def func_call_stmt(self):

        localctx = ZCodeParser.Func_call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_func_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 326
            self.match(ZCodeParser.LP)
            self.state = 327
            self.expr_list()
            self.state = 328
            self.match(ZCodeParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def tail_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Tail_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_list" ):
                return visitor.visitExpr_list(self)
            else:
                return visitor.visitChildren(self)




    def expr_list(self):

        localctx = ZCodeParser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_expr_list)
        try:
            self.state = 334
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.NOT, ZCodeParser.SUBTR_OP, ZCodeParser.LP, ZCodeParser.LB, ZCodeParser.NUM_LIT, ZCodeParser.STRING_LIT, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 330
                self.expr()
                self.state = 331
                self.tail_expr()
                pass
            elif token in [ZCodeParser.RP]:
                self.enterOuterAlt(localctx, 2)

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


    class Tail_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def tail_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Tail_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_tail_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTail_expr" ):
                return visitor.visitTail_expr(self)
            else:
                return visitor.visitChildren(self)




    def tail_expr(self):

        localctx = ZCodeParser.Tail_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_tail_expr)
        try:
            self.state = 341
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 336
                self.match(ZCodeParser.COMMA)
                self.state = 337
                self.expr()
                self.state = 338
                self.tail_expr()
                pass
            elif token in [ZCodeParser.RP, ZCodeParser.RB]:
                self.enterOuterAlt(localctx, 2)

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


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def compulsory_newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Compulsory_newlineContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Compulsory_newlineContext,i)


        def body_block(self):
            return self.getTypedRuleContext(ZCodeParser.Body_blockContext,0)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = ZCodeParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.match(ZCodeParser.BEGIN)
            self.state = 344
            self.compulsory_newline()
            self.state = 345
            self.body_block()
            self.state = 346
            self.match(ZCodeParser.END)
            self.state = 347
            self.compulsory_newline()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Body_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block_stmt_list(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmt_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_body_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody_block" ):
                return visitor.visitBody_block(self)
            else:
                return visitor.visitChildren(self)




    def body_block(self):

        localctx = ZCodeParser.Body_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_body_block)
        try:
            self.state = 351
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.NOT, ZCodeParser.SUBTR_OP, ZCodeParser.LP, ZCodeParser.LB, ZCodeParser.NUM_LIT, ZCodeParser.STRING_LIT, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 349
                self.block_stmt_list()
                pass
            elif token in [ZCodeParser.END]:
                self.enterOuterAlt(localctx, 2)

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


    class Block_stmt_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def block_stmt_list(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmt_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_block_stmt_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt_list" ):
                return visitor.visitBlock_stmt_list(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt_list(self):

        localctx = ZCodeParser.Block_stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_block_stmt_list)
        try:
            self.state = 357
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 353
                self.statement()
                self.state = 354
                self.block_stmt_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 356
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr1Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr1Context,i)


        def SPREAD_OP(self):
            return self.getToken(ZCodeParser.SPREAD_OP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = ZCodeParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_expr)
        try:
            self.state = 364
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 359
                self.expr1()
                self.state = 360
                self.match(ZCodeParser.SPREAD_OP)
                self.state = 361
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 363
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr2Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr2Context,i)


        def relational_op(self):
            return self.getTypedRuleContext(ZCodeParser.Relational_opContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = ZCodeParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_expr1)
        try:
            self.state = 371
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 366
                self.expr2(0)
                self.state = 367
                self.relational_op()
                self.state = 368
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 370
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(ZCodeParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(ZCodeParser.Expr2Context,0)


        def and_or(self):
            return self.getTypedRuleContext(ZCodeParser.And_orContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 382
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 376
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 377
                    self.and_or()
                    self.state = 378
                    self.expr3(0) 
                self.state = 384
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(ZCodeParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(ZCodeParser.Expr3Context,0)


        def add_subtr(self):
            return self.getTypedRuleContext(ZCodeParser.Add_subtrContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 90
        self.enterRecursionRule(localctx, 90, self.RULE_expr3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 394
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 388
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 389
                    self.add_subtr()
                    self.state = 390
                    self.expr4(0) 
                self.state = 396
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(ZCodeParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(ZCodeParser.Expr4Context,0)


        def mul_div_rem(self):
            return self.getTypedRuleContext(ZCodeParser.Mul_div_remContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 92
        self.enterRecursionRule(localctx, 92, self.RULE_expr4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 406
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 400
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 401
                    self.mul_div_rem()
                    self.state = 402
                    self.expr5() 
                self.state = 408
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def expr5(self):
            return self.getTypedRuleContext(ZCodeParser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(ZCodeParser.Expr6Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = ZCodeParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_expr5)
        try:
            self.state = 412
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 409
                self.match(ZCodeParser.NOT)
                self.state = 410
                self.expr5()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.SUBTR_OP, ZCodeParser.LP, ZCodeParser.LB, ZCodeParser.NUM_LIT, ZCodeParser.STRING_LIT, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 411
                self.expr6()
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


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUBTR_OP(self):
            return self.getToken(ZCodeParser.SUBTR_OP, 0)

        def expr6(self):
            return self.getTypedRuleContext(ZCodeParser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(ZCodeParser.Expr7Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = ZCodeParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_expr6)
        try:
            self.state = 417
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SUBTR_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 414
                self.match(ZCodeParser.SUBTR_OP)
                self.state = 415
                self.expr6()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.LP, ZCodeParser.LB, ZCodeParser.NUM_LIT, ZCodeParser.STRING_LIT, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 416
                self.expr7(0)
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


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr8(self):
            return self.getTypedRuleContext(ZCodeParser.Expr8Context,0)


        def expr7(self):
            return self.getTypedRuleContext(ZCodeParser.Expr7Context,0)


        def index_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Index_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)



    def expr7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 98
        self.enterRecursionRule(localctx, 98, self.RULE_expr7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self.expr8()
            self._ctx.stop = self._input.LT(-1)
            self.state = 426
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                    self.state = 422
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 423
                    self.index_expr() 
                self.state = 428
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def operand(self):
            return self.getTypedRuleContext(ZCodeParser.OperandContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr8" ):
                return visitor.visitExpr8(self)
            else:
                return visitor.visitChildren(self)




    def expr8(self):

        localctx = ZCodeParser.Expr8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_expr8)
        try:
            self.state = 434
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 429
                self.match(ZCodeParser.LP)
                self.state = 430
                self.expr()
                self.state = 431
                self.match(ZCodeParser.RP)
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.LB, ZCodeParser.NUM_LIT, ZCodeParser.STRING_LIT, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 433
                self.operand()
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


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def literal(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralContext,0)


        def func_call_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Func_call_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = ZCodeParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_operand)
        try:
            self.state = 439
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 436
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 437
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 438
                self.func_call_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_call_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def expr_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_listContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_func_call_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call_expr" ):
                return visitor.visitFunc_call_expr(self)
            else:
                return visitor.visitChildren(self)




    def func_call_expr(self):

        localctx = ZCodeParser.Func_call_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_func_call_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 442
            self.match(ZCodeParser.LP)
            self.state = 443
            self.expr_list()
            self.state = 444
            self.match(ZCodeParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM_LIT(self):
            return self.getToken(ZCodeParser.NUM_LIT, 0)

        def TRUE(self):
            return self.getToken(ZCodeParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(ZCodeParser.FALSE, 0)

        def STRING_LIT(self):
            return self.getToken(ZCodeParser.STRING_LIT, 0)

        def array_lit(self):
            return self.getTypedRuleContext(ZCodeParser.Array_litContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = ZCodeParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_literal)
        try:
            self.state = 451
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUM_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 446
                self.match(ZCodeParser.NUM_LIT)
                pass
            elif token in [ZCodeParser.TRUE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 447
                self.match(ZCodeParser.TRUE)
                pass
            elif token in [ZCodeParser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 448
                self.match(ZCodeParser.FALSE)
                pass
            elif token in [ZCodeParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 449
                self.match(ZCodeParser.STRING_LIT)
                pass
            elif token in [ZCodeParser.LB]:
                self.enterOuterAlt(localctx, 5)
                self.state = 450
                self.array_lit()
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


    class Array_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def comp_expr_list(self):
            return self.getTypedRuleContext(ZCodeParser.Comp_expr_listContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_lit" ):
                return visitor.visitArray_lit(self)
            else:
                return visitor.visitChildren(self)




    def array_lit(self):

        localctx = ZCodeParser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_array_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 453
            self.match(ZCodeParser.LB)
            self.state = 454
            self.comp_expr_list()
            self.state = 455
            self.match(ZCodeParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comp_expr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def tail_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Tail_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_comp_expr_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComp_expr_list" ):
                return visitor.visitComp_expr_list(self)
            else:
                return visitor.visitChildren(self)




    def comp_expr_list(self):

        localctx = ZCodeParser.Comp_expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_comp_expr_list)
        try:
            self.state = 461
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 457
                self.expr()
                self.state = 458
                self.tail_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 460
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def index_operator(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_index_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_expr" ):
                return visitor.visitIndex_expr(self)
            else:
                return visitor.visitChildren(self)




    def index_expr(self):

        localctx = ZCodeParser.Index_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_index_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 463
            self.match(ZCodeParser.LB)
            self.state = 464
            self.index_operator()
            self.state = 465
            self.match(ZCodeParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def index_operator(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_index_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operator" ):
                return visitor.visitIndex_operator(self)
            else:
                return visitor.visitChildren(self)




    def index_operator(self):

        localctx = ZCodeParser.Index_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_index_operator)
        try:
            self.state = 472
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 467
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 468
                self.expr()
                self.state = 469
                self.match(ZCodeParser.COMMA)
                self.state = 470
                self.index_operator()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mul_div_remContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MUL_OP(self):
            return self.getToken(ZCodeParser.MUL_OP, 0)

        def DIV_OP(self):
            return self.getToken(ZCodeParser.DIV_OP, 0)

        def REMAINDER_OP(self):
            return self.getToken(ZCodeParser.REMAINDER_OP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_mul_div_rem

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul_div_rem" ):
                return visitor.visitMul_div_rem(self)
            else:
                return visitor.visitChildren(self)




    def mul_div_rem(self):

        localctx = ZCodeParser.Mul_div_remContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_mul_div_rem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL_OP) | (1 << ZCodeParser.DIV_OP) | (1 << ZCodeParser.REMAINDER_OP))) != 0)):
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


    class Add_subtrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD_OP(self):
            return self.getToken(ZCodeParser.ADD_OP, 0)

        def SUBTR_OP(self):
            return self.getToken(ZCodeParser.SUBTR_OP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_add_subtr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd_subtr" ):
                return visitor.visitAdd_subtr(self)
            else:
                return visitor.visitChildren(self)




    def add_subtr(self):

        localctx = ZCodeParser.Add_subtrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_add_subtr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 476
            _la = self._input.LA(1)
            if not(_la==ZCodeParser.ADD_OP or _la==ZCodeParser.SUBTR_OP):
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


    class And_orContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_and_or

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnd_or" ):
                return visitor.visitAnd_or(self)
            else:
                return visitor.visitChildren(self)




    def and_or(self):

        localctx = ZCodeParser.And_orContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_and_or)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 478
            _la = self._input.LA(1)
            if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
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


    class Relational_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL(self):
            return self.getToken(ZCodeParser.EQUAL, 0)

        def EQUAL_STR(self):
            return self.getToken(ZCodeParser.EQUAL_STR, 0)

        def NOT_EQUAL(self):
            return self.getToken(ZCodeParser.NOT_EQUAL, 0)

        def SMALLER(self):
            return self.getToken(ZCodeParser.SMALLER, 0)

        def GREATER(self):
            return self.getToken(ZCodeParser.GREATER, 0)

        def SMALLER_OR_EQUAL(self):
            return self.getToken(ZCodeParser.SMALLER_OR_EQUAL, 0)

        def GREATER_OR_EQUAL(self):
            return self.getToken(ZCodeParser.GREATER_OR_EQUAL, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_relational_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational_op" ):
                return visitor.visitRelational_op(self)
            else:
                return visitor.visitChildren(self)




    def relational_op(self):

        localctx = ZCodeParser.Relational_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_relational_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 480
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQUAL) | (1 << ZCodeParser.NOT_EQUAL) | (1 << ZCodeParser.SMALLER) | (1 << ZCodeParser.SMALLER_OR_EQUAL) | (1 << ZCodeParser.GREATER) | (1 << ZCodeParser.GREATER_OR_EQUAL) | (1 << ZCodeParser.EQUAL_STR))) != 0)):
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[44] = self.expr2_sempred
        self._predicates[45] = self.expr3_sempred
        self._predicates[46] = self.expr4_sempred
        self._predicates[49] = self.expr7_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr7_sempred(self, localctx:Expr7Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




