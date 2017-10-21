from turtle import Turtle

t = Turtle()

t.width(1)

side = 10

width = 11

height = 9

white, black, grey, pink, transparent = "white", "black", "#EEF4F4", "#FF686C", "#ADD8E6"

t.speed(500)

#bgcolor won't work, bug?

t.color("#ADD8E6")

#couldnt really use a loop here. or i was just too lazy to
#think, not sure on that one

#i would have used bgcolor but it wouldnt work for some
#reason.

t.begin_fill()
t.left(90)
t.setpos(260, 420)
t.left(90)
t.forward(260 * 2)
t.left(90)
t.forward(1200)
t.left(90)
t.forward(260 * 2)
t.left(90)
t.forward(1200)
t.end_fill()
t.setposition(-(width * (side/2)), height * (side/2))

t.right(90)

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
    
row([(transparent, 1), (white, 1), (white, 1), (white, 1), (white, 1), (white, 1)])
row([(transparent, 5), (white, 1), (white, 1), (white, 1), (white, 1), (white, 1), (white, 1), (white, 1)])
row([(transparent, 4), (white, 1), (white, 1), (black, 1), (white, 1), (black, 1), (white, 1), (white, 1)])
row([(transparent, 4), (white, 7)])
row([(transparent, 5), (white, 2), (black, 1), (white, 2), (grey, 1), (white, 3)])
row([(transparent, 2), (grey, 1), (white, 1), (pink, 1), (white, 1), (grey, 1), (white, 5)])
row([(transparent, 1), (white, 1), (grey, 3), (white, 5)])
row([(transparent, 2), (white, 9)])
row([(transparent, 3), (white, 1), (transparent, 1), (white, 1), (transparent, 2), (white, 1), (transparent, 1), (white, 1)])
t.ht()