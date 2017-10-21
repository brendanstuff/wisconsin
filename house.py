# Credit to Dank Memes

from turtle import Turtle

t = Turtle()


t.color("blue")

t.begin_fill()
t.st()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(-90)

t.end_fill()

t.begin_fill()

t.color("black")
t.right(40)
t.forward(80)
t.right(100)
t.forward(80)
t.end_fill()

t.color("red")

t.setpos(25, t.ycor() - 100)
t.st()



t.begin_fill()
t.left(140)
t.forward(40)
t.right(90)
t.forward(20)
t.right(90)
t.forward(40)
t.end_fill()

t.color("gold")

t.setpos(t.xcor() - 7, t.ycor() + 20)
t.begin_fill()
t.circle(2)
t.end_fill()
t.ht()