# Generated from gcode.g4 by ANTLR 4.13.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .gcodeParser import gcodeParser
else:
    from gcodeParser import gcodeParser

# This class defines a complete generic visitor for a parse tree produced by gcodeParser.

import gcode_functions

class gcodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by gcodeParser#start.
    def visitStart(self, ctx:gcodeParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gcodeParser#nodrawExpr.
    def visitNodrawExpr(self, ctx:gcodeParser.NodrawExprContext):
        target_x = int(ctx.x_cord.text)
        target_y = int(ctx.y_cord.text)

        gcode_functions.G00_functionality(target_x, target_y)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by gcodeParser#drawlineExpr.
    def visitDrawlineExpr(self, ctx:gcodeParser.DrawlineExprContext):
        target_x    = int(ctx.x_cord.text)
        target_y    = int(ctx.y_cord.text)

        gcode_functions.G01_functionality(target_x, target_y)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by gcodeParser#drawccExpr.
    def visitDrawccExpr(self, ctx:gcodeParser.DrawccExprContext):
        start = int(ctx.x_cord.text)
        end = int(ctx.y_cord.text)
        radius = int(ctx.radius.text)
        
        gcode_functions.G02_functionality(start, end, radius)

        return self.visitChildren(ctx)

    # Visit a parse tree produced by gcodeParser#drawcccExpr.
    def visitDrawcccExpr(self, ctx:gcodeParser.DrawcccExprContext):
        start = int(ctx.x_cord.text)
        end = int(ctx.y_cord.text)
        radius = int(ctx.radius.text)

        gcode_functions.G03_functionality(start, end, radius)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by gcodeParser#printlineExpr.
    def visitPrintlineExpr(self, ctx:gcodeParser.PrintlineExprContext):
        x = int(ctx.x_cord.text)
        y = int(ctx.y_cord.text)

        gcode_functions.print_functionality()

        return self.visitChildren(x, y)


del gcodeParser
