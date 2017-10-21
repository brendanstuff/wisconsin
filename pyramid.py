from turtle import Turtle

t = Turtle()

t.shape("turtle")

t.st()

t.color("red")
t.begin_fill()
for i in range(2):
    t.forward(40)
    t.left(120)
    t.forward(40)
    t.left(120)
t.end_fill()

t.left(180);

t.color("green")

t.begin_fill()
for i in range(2):
    t.forward(40)
    t.right(120)
    t.forward(40)
    t.right(120)
t.end_fill()

t.setpos(t.xcor() - 40, t.ycor())
t.color("blue")

t.begin_fill()
for i in range(2):
    t.forward(40)
    t.right(120)
    t.forward(40)
    t.right(120)
t.end_fill()

t.ht()