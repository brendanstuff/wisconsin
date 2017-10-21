from turtle import Turtle

t = Turtle()
t.shape("turtle")
t.forward(0)

length = 20

t.st()

for i in range(45):
    t.forward(length)
    t.left(90)
    length=length+10
    
t.forward(450)
    
t.ht()