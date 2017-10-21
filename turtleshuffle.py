from turtle import Turtle
from random import randint

a = Turtle()
b = Turtle()
c = Turtle()
d = Turtle()
e = Turtle()
f = Turtle()
g = Turtle()
h = Turtle()
i = Turtle()

t = [a, b, c, d, e, f, g, h, i]

x = -100
y = 50


swapElement = 0
swapWith = 0

# coloring the turtles

a.color(randint(0, 255), randint(0, 255), randint(0, 255))
b.color(randint(0, 255), randint(0, 255), randint(0, 255))
c.color(randint(0, 255), randint(0, 255), randint(0, 255))
d.color(randint(0, 255), randint(0, 255), randint(0, 255))
e.color(randint(0, 255), randint(0, 255), randint(0, 255))
f.color(randint(0, 255), randint(0, 255), randint(0, 255))
g.color(randint(0, 255), randint(0, 255), randint(0, 255))
h.color(randint(0, 255), randint(0, 255), randint(0, 255))
i.color(randint(0, 255), randint(0, 255), randint(0, 255))



for i in range(9):
    if i == 3 or i == 6:
        y -= 50
        x -= 100
    else:
        x += 50
    t[i].setposition(x, y)

for i in range(100):
    
    swapElement = randint(0, 8)
    swapWith = randint(0, 8)

    swapX = t[swapElement].xcor()
    swapY = t[swapElement].ycor()

    t[swapElement].setpos(t[swapWith].xcor(), t[swapWith].ycor())
    t[swapWith].setpos(swapX, swapY)