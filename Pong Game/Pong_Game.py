from JMSSGraphics import *
import random

width = 1200
height = 800
fps = 60

jmss = Graphics(width = width, height = height, title = "Bouncing Ball", fps = fps)

bax = width/2
bay = height/2
xdir = 1
ydir = 1

Ball = jmss.loadImage("ball.png")


@jmss.mainloop
def Pong ():
    global bax, bay, xdir, ydir, height

    if (bax > width - 64 or bax < 0):
        xdir = -xdir

    if (bay > height - 64 or bay < 0):
        ydir = -ydir

    bax += 5*xdir
    bay += 5*ydir

    jmss.clear()
    jmss.drawImage(Ball, x = bax, y = bay)

jmss.run()
