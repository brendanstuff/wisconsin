from turtle import Turtle

t = Turtle()

def sides(i):
    t.color("black")
    for i in range(i):
        t.forward(50)
        t.right(45)
def triangle(color):
    t.color(color)
    for i in range(3):
        t.forward(50)
        t.left(120)

sides(1)

triangle("green")
sides(2)
triangle("pink")
sides(2)
triangle("blue")
sides(2)
triangle("red")
sides(1)