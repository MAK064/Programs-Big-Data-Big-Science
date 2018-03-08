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

p1x = 1/12*width
p1y = 1/2*height

#p2x =
#p2y =


Ball = jmss.loadImage("ball.png")
Paddle = jmss.loadImage("Pong Paddle.jpg")

@jmss.mainloop
def Pong ():
    global bax, bay, xdir, ydir, height, p1y, p1x

    if jmss.isKeyDown(KEY_W):
        p1y += 3
    if jmss.isKeyDown(KEY_S):
        p1y -= 3


    if (bax > width - 64 or bax < 0 or (p1x <= bax <= (p1x + 35) and p1y <= bay <= (p1y + 125))):
        xdir = -xdir

    if (bay > height - 64 or bay < 0):
        ydir = -ydir

    bax += 5*xdir
    bay += 5*ydir

    jmss.clear()
    jmss.drawImage(Ball, x = bax, y = bay)
    jmss.drawImage(Paddle, x = p1x, y = p1y)

jmss.run()
