# Generated from gcode.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .gcodeParser import gcodeParser
else:
    from gcodeParser import gcodeParser

# This class defines a complete listener for a parse tree produced by gcodeParser.
class gcodeListener(ParseTreeListener):

    # Enter a parse tree produced by gcodeParser#start.
    def enterStart(self, ctx:gcodeParser.StartContext):
        pass

    # Exit a parse tree produced by gcodeParser#start.
    def exitStart(self, ctx:gcodeParser.StartContext):
        pass


    # Enter a parse tree produced by gcodeParser#nodrawExpr.
    def enterNodrawExpr(self, ctx:gcodeParser.NodrawExprContext):
        pass

    # Exit a parse tree produced by gcodeParser#nodrawExpr.
    def exitNodrawExpr(self, ctx:gcodeParser.NodrawExprContext):
        pass


    # Enter a parse tree produced by gcodeParser#drawlineExpr.
    def enterDrawlineExpr(self, ctx:gcodeParser.DrawlineExprContext):
        pass

    # Exit a parse tree produced by gcodeParser#drawlineExpr.
    def exitDrawlineExpr(self, ctx:gcodeParser.DrawlineExprContext):
        pass


    # Enter a parse tree produced by gcodeParser#clockwisecircleExpr.
    def enterClockwisecircleExpr(self, ctx:gcodeParser.ClockwisecircleExprContext):
        pass

    # Exit a parse tree produced by gcodeParser#clockwisecircleExpr.
    def exitClockwisecircleExpr(self, ctx:gcodeParser.ClockwisecircleExprContext):
        pass


    # Enter a parse tree produced by gcodeParser#printlineExpr.
    def enterPrintlineExpr(self, ctx:gcodeParser.PrintlineExprContext):
        pass

    # Exit a parse tree produced by gcodeParser#printlineExpr.
    def exitPrintlineExpr(self, ctx:gcodeParser.PrintlineExprContext):
        pass



del gcodeParser