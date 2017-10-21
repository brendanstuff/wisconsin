from turtle import Turtle

t = Turtle()

t.setpos(-100,100)

for i in range(7):
    for i in range(9):
        t.forward(50)
        t.left(60)
    t.left(120)