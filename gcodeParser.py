# Generated from gcode.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,7,28,2,0,7,0,2,1,7,1,1,0,1,0,3,0,7,8,0,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,26,8,1,1,1,0,0,
        2,0,2,0,0,30,0,6,1,0,0,0,2,25,1,0,0,0,4,7,3,2,1,0,5,7,1,0,0,0,6,
        4,1,0,0,0,6,5,1,0,0,0,7,1,1,0,0,0,8,9,5,1,0,0,9,10,5,6,0,0,10,26,
        5,6,0,0,11,12,5,2,0,0,12,13,5,6,0,0,13,26,5,6,0,0,14,15,5,3,0,0,
        15,16,5,6,0,0,16,17,5,6,0,0,17,26,5,6,0,0,18,19,5,4,0,0,19,20,5,
        6,0,0,20,21,5,6,0,0,21,26,5,6,0,0,22,23,5,5,0,0,23,24,5,6,0,0,24,
        26,5,6,0,0,25,8,1,0,0,0,25,11,1,0,0,0,25,14,1,0,0,0,25,18,1,0,0,
        0,25,22,1,0,0,0,26,3,1,0,0,0,2,6,25
    ]

class gcodeParser ( Parser ):

    grammarFileName = "gcode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'G00'", "'G01'", "'G02'", "'G03'", "'print'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "NUMBER", "WS" ]

    RULE_start = 0
    RULE_expr = 1

    ruleNames =  [ "start", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    NUMBER=6
    WS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(gcodeParser.ExprContext,0)


        def getRuleIndex(self):
            return gcodeParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = gcodeParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.state = 6
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 4
                self.expr()
                pass
            elif token in [-1]:
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


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gcodeParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class NodrawExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gcodeParser.ExprContext
            super().__init__(parser)
            self.x_cord = None # Token
            self.y_cord = None # Token
            self.copyFrom(ctx)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(gcodeParser.NUMBER)
            else:
                return self.getToken(gcodeParser.NUMBER, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNodrawExpr" ):
                listener.enterNodrawExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNodrawExpr" ):
                listener.exitNodrawExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNodrawExpr" ):
                return visitor.visitNodrawExpr(self)
            else:
                return visitor.visitChildren(self)


    class DrawcccExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gcodeParser.ExprContext
            super().__init__(parser)
            self.x_cord = None # Token
            self.y_cord = None # Token
            self.radius = None # Token
            self.copyFrom(ctx)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(gcodeParser.NUMBER)
            else:
                return self.getToken(gcodeParser.NUMBER, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDrawcccExpr" ):
                listener.enterDrawcccExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDrawcccExpr" ):
                listener.exitDrawcccExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDrawcccExpr" ):
                return visitor.visitDrawcccExpr(self)
            else:
                return visitor.visitChildren(self)


    class PrintlineExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gcodeParser.ExprContext
            super().__init__(parser)
            self.x_cord = None # Token
            self.y_cord = None # Token
            self.copyFrom(ctx)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(gcodeParser.NUMBER)
            else:
                return self.getToken(gcodeParser.NUMBER, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintlineExpr" ):
                listener.enterPrintlineExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintlineExpr" ):
                listener.exitPrintlineExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintlineExpr" ):
                return visitor.visitPrintlineExpr(self)
            else:
                return visitor.visitChildren(self)


    class DrawccExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gcodeParser.ExprContext
            super().__init__(parser)
            self.x_cord = None # Token
            self.y_cord = None # Token
            self.radius = None # Token
            self.copyFrom(ctx)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(gcodeParser.NUMBER)
            else:
                return self.getToken(gcodeParser.NUMBER, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDrawccExpr" ):
                listener.enterDrawccExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDrawccExpr" ):
                listener.exitDrawccExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDrawccExpr" ):
                return visitor.visitDrawccExpr(self)
            else:
                return visitor.visitChildren(self)


    class DrawlineExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gcodeParser.ExprContext
            super().__init__(parser)
            self.x_cord = None # Token
            self.y_cord = None # Token
            self.copyFrom(ctx)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(gcodeParser.NUMBER)
            else:
                return self.getToken(gcodeParser.NUMBER, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDrawlineExpr" ):
                listener.enterDrawlineExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDrawlineExpr" ):
                listener.exitDrawlineExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDrawlineExpr" ):
                return visitor.visitDrawlineExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = gcodeParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.state = 25
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = gcodeParser.NodrawExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 8
                self.match(gcodeParser.T__0)
                self.state = 9
                localctx.x_cord = self.match(gcodeParser.NUMBER)
                self.state = 10
                localctx.y_cord = self.match(gcodeParser.NUMBER)
                pass
            elif token in [2]:
                localctx = gcodeParser.DrawlineExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 11
                self.match(gcodeParser.T__1)
                self.state = 12
                localctx.x_cord = self.match(gcodeParser.NUMBER)
                self.state = 13
                localctx.y_cord = self.match(gcodeParser.NUMBER)
                pass
            elif token in [3]:
                localctx = gcodeParser.DrawccExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 14
                self.match(gcodeParser.T__2)
                self.state = 15
                localctx.x_cord = self.match(gcodeParser.NUMBER)
                self.state = 16
                localctx.y_cord = self.match(gcodeParser.NUMBER)
                self.state = 17
                localctx.radius = self.match(gcodeParser.NUMBER)
                pass
            elif token in [4]:
                localctx = gcodeParser.DrawcccExprContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 18
                self.match(gcodeParser.T__3)
                self.state = 19
                localctx.x_cord = self.match(gcodeParser.NUMBER)
                self.state = 20
                localctx.y_cord = self.match(gcodeParser.NUMBER)
                self.state = 21
                localctx.radius = self.match(gcodeParser.NUMBER)
                pass
            elif token in [5]:
                localctx = gcodeParser.PrintlineExprContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 22
                self.match(gcodeParser.T__4)
                self.state = 23
                localctx.x_cord = self.match(gcodeParser.NUMBER)
                self.state = 24
                localctx.y_cord = self.match(gcodeParser.NUMBER)
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





