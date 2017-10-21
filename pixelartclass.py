from turtle import Turtle

t = Turtle()

size = 20

row = 5

blue = 3

t.st()

for i in range(row):
    t.begin_fill()
    for j in range(4):
            t.forward(size)
            t.right(90)
    t.end_fill()
    t.forward(size)
t.back(size * row)
t.setpos(t.xcor(), t.ycor() + size)

# Next row

t.begin_fill()

for i in range(4):
    t.forward(size)
    t.right(90)        
t.forward(size)
t.end_fill()

# 3 blue squares

t.color("blue")

for i in range(blue):
    t.begin_fill()
    for j in range(4):
            t.forward(size)
            t.right(90)
    t.end_fill()
    t.forward(size)

# 1 black square
t.color("black")
t.begin_fill()
for i in range(4):
    t.forward(size)
    t.right(90)        
t.forward(size)
t.end_fill()

    
t.setpos(t.xcor() - (size * row), t.ycor())
t.setpos(t.xcor(), t.ycor() + size)

t.begin_fill()

for i in range(4):
    t.forward(size)
    t.right(90)        
t.forward(size)
t.end_fill()

# 3 blue squares

t.color("blue")

for i in range(blue):
    t.begin_fill()
    for j in range(4):
            t.forward(size)
            t.right(90)
    t.end_fill()
    t.forward(size)

# 1 black square
t.color("black")
t.begin_fill()
for i in range(4):
    t.forward(size)
    t.right(90)        
t.forward(size)
t.end_fill()

    
t.setpos(t.xcor() - (size * row), t.ycor())
t.setpos(t.xcor(), t.ycor() + size)

t.begin_fill()

for i in range(4):
    t.forward(size)
    t.right(90)        
t.forward(size)
t.end_fill()

# 3 blue squares

t.color("blue")

for i in range(blue):
    t.begin_fill()
    for j in range(4):
            t.forward(size)
            t.right(90)
    t.end_fill()
    t.forward(size)

# 1 black square
t.color("black")
t.begin_fill()
for i in range(4):
    t.forward(size)
    t.right(90)        
t.forward(size)
t.end_fill()

    
t.setpos(t.xcor() - (size * row), t.ycor())
t.setpos(t.xcor(), t.ycor() + size)

for i in range(row):
    t.begin_fill()
    for j in range(4):
            t.forward(size)
            t.right(90)
    t.end_fill()
    t.forward(size)
t.back(size * row)
t.setpos(t.xcor(), t.ycor() + size)

t.ht()