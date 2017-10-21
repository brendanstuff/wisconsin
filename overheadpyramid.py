from turtle import Turtle

t = Turtle()

# I'd make this a nested loop but nah my friends are at
# my house

t.forward(0)

step = 10
x = 0
y = 0
t.speed()
t.st()
for i in range(20):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color("lightblue")
    t.forward(step)
    t.left(90)
    t.forward(step)
    t.color("purple")
    t.forward(step)
    t.left(90)
    t.forward(step)
    t.color("black")
    t.forward(step)
    t.left(90)
    t.forward(step)
    t.color("blue")
    t.forward(step)
    t.left(90)
    t.forward(step)
    step = step + 5
    y = y - 5
    
step-=5
t.left(90)
t.forward(step)
t.color("purple")
t.forward(step)
t.forward(step * -1)
t.right(90)
t.forward(step)
t.forward(step * -1)
t.color("black")
t.forward(step * -1)
t.ht()