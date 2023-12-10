# Generated from gcode.g4 by ANTLR 4.13.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .gcodeParser import gcodeParser
else:
    from gcodeParser import gcodeParser

# This class defines a complete generic visitor for a parse tree produced by gcodeParser.

import turtle
tutu = turtle.Turtle()

class gcodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by gcodeParser#start.
    def visitStart(self, ctx:gcodeParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gcodeParser#drawlineExpr.
    def visitDrawlineExpr(self, ctx:gcodeParser.DrawlineExprContext):
        target_x    = int(ctx.x_cord.text)
        target_y    = int(ctx.y_cord.text)
        cur_pos     = tutu.pos()

        if target_x > cur_pos[0]:
            tutu.right( target_x + cur_pos[0])
        else:
            tutu.left( cur_pos[0] - target_x)

        if target_y > cur_pos[1]:
            tutu.forward( target_y + cur_pos[1])
        else:
            tutu.backward( cur_pos[1] - target_y)




        return self.visitChildren(ctx)


    # Visit a parse tree produced by gcodeParser#printlineExpr.
    def visitPrintlineExpr(self, ctx:gcodeParser.PrintlineExprContext):
        print(f"Draw line to x={ctx.x_cord.text} y={ctx.y_cord.text}")
        return self.visitChildren(ctx)

del gcodeParser
