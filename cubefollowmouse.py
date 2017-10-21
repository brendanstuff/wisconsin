from processing import *

x = 0
y = 0
radius = 50
def setup():
    size(500, 500)
    fill(255)
    
def draw():
    global x, y, radius
    background(255)
    x += float(mouse.x - x)
    y += float(mouse.y - y)
    rect(x - 25, y - 25, 50, 50)
run()