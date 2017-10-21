from turtle import Turtle

t = Turtle()

# Nested loop edition.

t.forward(0)

step = 10
x = 0
y = 0
t.speed()
t.st()
delV = 0
next = ['lightblue', 'purple', 'black', 'blue']

for i in range(20):
    t.setpos(x,y)
    for j in range(4):
        t.color(next[0])
        del next[0]
        t.forward(step)
        t.left(90)
        t.forward(step)
    step+=5
    y-=5
    next = ['lightblue', 'purple', 'black', 'blue']
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