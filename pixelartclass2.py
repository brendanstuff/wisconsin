from turtle import Turtle

t = Turtle()
size = 20
row = 5
blue = 3
s = size

colors = ["black", "blue", "black"]
numbers = [1, 3, 1]

t.st()

def nextLine(size, row):
    t.back(size * row)
    t.left(90)
    t.forward(size)
    t.right(90)

def square(size, color):
    t.color(color)
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()
    t.forward(size)
    
def row(colors, numbers, size):
    numSquares = 0
    for i in range(len(colors)):
        for j in range(numbers[i]):
            square(size, colors[i])
        numSquares += numbers[i]
    nextLine(size, numSquares)


row(colors, numbers, size)