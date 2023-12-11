import turtle
tutu = turtle.Turtle()

def G00_functionality(x, y):
    tutu.penup()
    tutu.speed('fastest')
    tutu.goto(x, y)
    tutu.speed('normal')
    tutu.pendown()

def G01_functionality(x, y):
    tutu.goto(x, y)

def G02_functionality(start, end, radius):
    radius = radius * -1

    if start > end:
        length = start - end
    elif end > start:
        length = end - start
    else: # in case that we are given the same start and end value.
        length = None
    
    tutu.circle(radius, length)

def G03_functionality(start, end, radius):
    if start > end:
        length = start - end
    elif end > start:
        length = end - start
    else:
        length = None
    
    tutu.circle(radius, length)

def print_functionality(x, y):
    print(f"Draw line to x={x} y={y}")