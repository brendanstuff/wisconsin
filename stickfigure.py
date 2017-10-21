# meh, stick figures is a little above my level of
# drawing

from processing import *

def setup():
    background(255)
    size(1000, 1000)
    myFont = createFont("Georgia", 16)

def draw():
    noFill()
    ellipse(250,250,40,40)
    line(250,270,250,325)
    line(230,350,250,325)
    line(280,350,250,325)
    line(250,275,220,325)
    line(250,275,280,325)
    textSize(32)
    fill(0)
    text("Hi, my name is \nDank Memes.\nAnd yours is Bill.", 300, 300)
run()
