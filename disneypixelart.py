from turtle import Turtle

t = Turtle()
# I don't have GIMP on this computer, so I can't find out
# the exact hexadecimal values. I tried to get close,
# though.
tp, black, green, dgreen, brown, dbrown = 'white', 'black', '#00FF00', '#006600', '#FFD480', '#994D00' 

width = 21
height = 27
side = 10

t.speed(1000)

t.penup()
t.setposition(-(width * (side/2)), height * (side/2))
t.pendown()
def row(pixels):
    for (color, count) in pixels:
        t.color(color)
        for j in range(count):
            t.begin_fill()
            for k in range(4):
                t.forward(side)
                t.right(90)
            t.end_fill()
            t.forward(side)
    t.penup()
    t.back(width * side)
    t.right(90)
    t.forward(side)
    t.left(90)
    t.pendown()
t.speed(50)

row([(tp, 14), (black, 3), (tp, 4)])
row([(tp, 13), (black, 5), (tp, 3)])
row([(tp, 13), (black, 5), (tp, 3)])
row([(tp, 6), (black, 2), (dbrown, 4), (black, 6), (tp, 3)])
row([(tp, 4), (black, 3), (dbrown, 1), (brown, 4), (dbrown, 1), (black, 2), (tp, 6)])
row([(tp, 3), (black, 3), (dbrown, 1), (brown, 1), (tp, 1), (brown, 2), (tp, 1), (brown, 1), (dbrown, 1), (tp, 7)])
row([(tp, 3), (black, 2), (dbrown, 1), (brown, 1), (tp, 6), (brown, 1), (dbrown, 1), (tp, 6)])
row([(tp, 2), (black, 3), (dbrown, 1), (brown, 1), (tp, 6), (brown, 1), (dbrown, 1), (tp, 6)])
row([(tp, 2), (black, 3), (dbrown, 1), (brown, 1), (tp, 1), (black, 1), (tp, 2), (black, 1), (tp, 1), (brown, 1), (dbrown, 1), (tp, 6)])
row([(tp, 2), (black, 3), (dbrown, 1), (brown, 1), (tp, 1), (black, 1), (tp, 2), (black, 1), (tp, 1), (brown, 1), (dbrown, 1), (tp, 6)])
row([(tp, 1), (black, 3), (dbrown, 1), (brown, 10), (dbrown, 1), (tp, 5)])
row([(tp, 1), (black, 3), (dbrown, 1), (brown, 4), (black, 2), (brown, 4), (dbrown, 1), (tp, 5)])
row([(tp, 1), (black, 4), (dbrown, 1), (brown, 8), (dbrown, 1), (tp, 6)])
row([(tp, 2), (black, 3), (tp, 1), (dbrown, 1), (brown, 6), (dbrown, 1), (tp, 7)])
row([(tp, 7), (dgreen, 1), (green, 4), (dgreen, 1), (tp, 8)])
row([(tp, 6), (dbrown, 1), (brown, 6), (dbrown, 1), (tp, 7)])
row([(tp, 5), (dbrown, 1), (brown, 8), (dbrown, 1), (tp, 6)])
row([(tp, 5), (dbrown, 1), (brown, 8), (dbrown, 1), (tp, 6)])
row([(tp, 5), (dbrown, 1), (brown, 8), (dbrown, 1), (tp, 6)])
row([(tp, 1), (dbrown, 2), (tp, 2), (dbrown, 1), (brown, 2), (dbrown, 1), (brown, 2), (dbrown, 1), (brown, 2), (dbrown, 1), (tp, 2), (dbrown, 2), (tp, 2)])
row([(dbrown, 1), (brown, 2), (dbrown, 2), (brown, 3), (dbrown, 1), (brown, 2), (dbrown, 1), (brown, 3), (dbrown, 2), (brown, 2), (dbrown, 1), (tp, 1)])
row([(dbrown, 1), (brown, 3), (dbrown, 1), (brown, 3), (dbrown, 1), (brown, 2), (dbrown, 1), (brown, 3), (dbrown, 1), (brown, 3), (dbrown, 1), (tp, 1)])
row([(dbrown, 1), (brown, 3), (dbrown, 1), (brown, 3), (dbrown, 1), (brown, 2), (dbrown, 1), (brown, 3), (dbrown, 1), (brown, 3), (dbrown, 1), (tp, 1)])
row([(dbrown, 1), (brown, 3), (dbrown, 1), (brown, 3), (dbrown, 4), (brown, 3), (dbrown, 1), (brown, 3), (dbrown, 1), (tp, 1)])
row([(tp, 1), (dbrown, 4), (brown, 3), (dbrown, 1), (tp, 2), (dbrown, 1), (brown, 3), (dbrown, 4), (tp, 2)])
row([(tp, 5), (dbrown, 3), (tp, 4), (dbrown, 3), (tp, 6)])
row([(tp, 21)])