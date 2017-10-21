from turtle import Turtle

t = Turtle()
t.st()
for i in range(4):
    t.forward(100)
    t.left(90)
t.setposition(t.xcor() + 20, t.ycor() + 20)
for i in range(4):
    t.forward(100)
    t.left(90)
t.goto(t.xcor() - 20, t.ycor() - 20)
t.setposition(t.xcor(), t.ycor() + 100)
t.goto(t.xcor() + 20, t.ycor() + 20)
t.forward(100)
t.goto(t.xcor() - 20, t.ycor() - 20)
t.right(90)
t.forward(100)
t.goto(t.xcor() + 20, t.ycor() + 20)
t.ht()