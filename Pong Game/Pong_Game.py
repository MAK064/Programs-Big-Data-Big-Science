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

p1x = 1/12*width - 16
p1y = 1/2*height - 64

p2x = 11/12*width - 16
p2y = 1/2*height - 64


Ball = jmss.loadImage("ball.png")
Paddle = jmss.loadImage("Pong Paddle.jpg")

@jmss.mainloop
def Pong ():
    global bax, bay, xdir, ydir, height, p1y, p1x, p2y, p2x

    if jmss.isKeyDown(KEY_W):
        p1y += 3
    if jmss.isKeyDown(KEY_S):
        p1y -= 3
    if jmss.isKeyDown(KEY_I):
        p2y += 3
    if jmss.isKeyDown(KEY_K):
        p2y -= 3

    bax += 5*xdir
    bay += 5*ydir

    if ((bax <= p1x + 16 and p1y - 128 < bay < p1y + 48) or (bax >= p2x - 56 and p2y - 64 < bay < p2y + 144)):
        xdir = -xdir

    if (bax > width - 64 or bax < 0):
        xdir = -xdir
    if (bay > height - 64 or bay < 0):
        ydir = -ydir

    jmss.clear()
    jmss.drawImage(Ball, x = bax, y = bay)
    jmss.drawImage(Paddle, x = p1x, y = p1y - 64)
    jmss.drawImage(Paddle, x = p2x, y = p2y - 64)

jmss.run()
