# Generated from gcode.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,6,51,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,
        0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,
        3,1,3,1,4,4,4,33,8,4,11,4,12,4,34,1,4,1,4,4,4,39,8,4,11,4,12,4,40,
        3,4,43,8,4,1,5,4,5,46,8,5,11,5,12,5,47,1,5,1,5,0,0,6,1,1,3,2,5,3,
        7,4,9,5,11,6,1,0,1,3,0,9,10,13,13,32,32,54,0,1,1,0,0,0,0,3,1,0,0,
        0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,1,13,1,0,0,0,
        3,17,1,0,0,0,5,21,1,0,0,0,7,25,1,0,0,0,9,32,1,0,0,0,11,45,1,0,0,
        0,13,14,5,71,0,0,14,15,5,48,0,0,15,16,5,48,0,0,16,2,1,0,0,0,17,18,
        5,71,0,0,18,19,5,48,0,0,19,20,5,49,0,0,20,4,1,0,0,0,21,22,5,71,0,
        0,22,23,5,48,0,0,23,24,5,50,0,0,24,6,1,0,0,0,25,26,5,112,0,0,26,
        27,5,114,0,0,27,28,5,105,0,0,28,29,5,110,0,0,29,30,5,116,0,0,30,
        8,1,0,0,0,31,33,2,48,57,0,32,31,1,0,0,0,33,34,1,0,0,0,34,32,1,0,
        0,0,34,35,1,0,0,0,35,42,1,0,0,0,36,38,5,46,0,0,37,39,2,48,57,0,38,
        37,1,0,0,0,39,40,1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,43,1,0,0,
        0,42,36,1,0,0,0,42,43,1,0,0,0,43,10,1,0,0,0,44,46,7,0,0,0,45,44,
        1,0,0,0,46,47,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,49,1,0,0,0,
        49,50,6,5,0,0,50,12,1,0,0,0,5,0,34,40,42,47,1,6,0,0
    ]

class gcodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    NUMBER = 5
    WS = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'G00'", "'G01'", "'G02'", "'print'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "NUMBER", "WS" ]

    grammarFileName = "gcode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


