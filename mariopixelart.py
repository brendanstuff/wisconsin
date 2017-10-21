from turtle import Turtle

t = Turtle()
# I don't have GIMP on this computer, so I can't find out
# the exact hexadecimal values. I tried to get close,
# though.
y, b, w = 'yellow', 'black', 'white'
width = 16
height = 16
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
t.speed(15)

row([(w, 1), (b, 14), (w, 1)])
row([(b, 2), (y, 12), (b, 2)])
row([(b, 1), (y, 1), (b, 1), (y, 10), (b, 1), (y, 1), (b, 1)])
row([(b, 1), (y, 4), (w, 7), (y, 3), (b, 1)])
row([(b, 1), (y, 2), (w, 9), (y, 3), (b, 1)])
row([(b, 1), (y, 2), (w, 3), (b, 3), (w, 3), (b, 1), (y, 2), (b, 1)])
row([(b, 1), (y, 3), (b, 3), (y, 2), (w, 3), (b, 1), (y, 2), (b, 1)])
row([(b, 1), (y, 5), (w, 5), (b, 2), (y, 2), (b, 1)])
row([(b, 1), (y, 5), (w, 3), (b, 3), (y, 3), (b, 1)])
row([(b, 1), (y, 6), (b, 3), (y, 5), (b, 1)])
row([(b, 1), (y, 5), (w, 3), (y, 6), (b, 1)])
row([(b, 1), (y, 5), (w, 3), (b, 1), (y, 5), (b, 1)])
row([(b, 1), (y, 5), (b, 4), (y, 5), (b, 1)])
row([(b, 1), (y, 1), (b, 1), (y, 10), (b, 1), (y, 1), (b, 1)])
row([(b, 2), (y, 12), (b, 2)])
row([(w, 1), (b, 14), (w, 1)])
