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
        4,0,4,39,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,0,1,
        1,1,1,1,1,1,1,1,1,1,1,1,2,4,2,21,8,2,11,2,12,2,22,1,2,1,2,4,2,27,
        8,2,11,2,12,2,28,3,2,31,8,2,1,3,4,3,34,8,3,11,3,12,3,35,1,3,1,3,
        0,0,4,1,1,3,2,5,3,7,4,1,0,1,3,0,9,10,13,13,32,32,42,0,1,1,0,0,0,
        0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,1,9,1,0,0,0,3,13,1,0,0,0,5,20,
        1,0,0,0,7,33,1,0,0,0,9,10,5,71,0,0,10,11,5,48,0,0,11,12,5,49,0,0,
        12,2,1,0,0,0,13,14,5,112,0,0,14,15,5,114,0,0,15,16,5,105,0,0,16,
        17,5,110,0,0,17,18,5,116,0,0,18,4,1,0,0,0,19,21,2,48,57,0,20,19,
        1,0,0,0,21,22,1,0,0,0,22,20,1,0,0,0,22,23,1,0,0,0,23,30,1,0,0,0,
        24,26,5,46,0,0,25,27,2,48,57,0,26,25,1,0,0,0,27,28,1,0,0,0,28,26,
        1,0,0,0,28,29,1,0,0,0,29,31,1,0,0,0,30,24,1,0,0,0,30,31,1,0,0,0,
        31,6,1,0,0,0,32,34,7,0,0,0,33,32,1,0,0,0,34,35,1,0,0,0,35,33,1,0,
        0,0,35,36,1,0,0,0,36,37,1,0,0,0,37,38,6,3,0,0,38,8,1,0,0,0,5,0,22,
        28,30,35,1,6,0,0
    ]

class gcodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    NUMBER = 3
    WS = 4

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'G01'", "'print'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "WS" ]

    ruleNames = [ "T__0", "T__1", "NUMBER", "WS" ]

    grammarFileName = "gcode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


