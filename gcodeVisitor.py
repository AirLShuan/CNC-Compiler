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


    # Visit a parse tree produced by gcodeParser#nodrawExpr.
    def visitNodrawExpr(self, ctx:gcodeParser.NodrawExprContext):
        target_x    = int(ctx.x_cord.text)
        target_y    = int(ctx.y_cord.text)

        tutu.penup()
        tutu.speed('fastest')
        tutu.goto(target_x, target_y)
        tutu.speed('normal')
        tutu.pendown()

        return self.visitChildren(ctx)


    # Visit a parse tree produced by gcodeParser#drawlineExpr.
    def visitDrawlineExpr(self, ctx:gcodeParser.DrawlineExprContext):
        target_x    = int(ctx.x_cord.text)
        target_y    = int(ctx.y_cord.text)


        tutu.goto(target_x, target_y)
        return self.visitChildren(ctx)




    # Visit a parse tree produced by gcodeParser#clockwisecircleExpr.
    def visitClockwisecircleExpr(self, ctx:gcodeParser.ClockwisecircleExprContext):
        start = int(ctx.x_cord.text)
        end = int(ctx.y_cord.text)
        radius = int(ctx.radius.text)
        radius = radius * -1

        if start > end:
            length = start - end
        elif end > start:
            length = end - start
        else:
            length = None
        
        tutu.circle(radius, length)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by gcodeParser#printlineExpr.
    def visitPrintlineExpr(self, ctx:gcodeParser.PrintlineExprContext):
        print(f"Draw line to x={ctx.x_cord.text} y={ctx.y_cord.text}")
        return self.visitChildren(ctx)

del gcodeParser
