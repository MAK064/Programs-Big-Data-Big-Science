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

p1score = 0
p2score = 0

gamestate = "Null"

Ball = jmss.loadImage("ball.png")
Paddle = jmss.loadImage("Pong Paddle.jpg")

@jmss.mainloop
def Pong ():
    global bax, bay, xdir, ydir, height, p1y, p1x, p2y, p2x, p1score, p2score

    #Key Checks and respective movements
    if jmss.isKeyDown(KEY_W):
        p1y += 4
    if jmss.isKeyDown(KEY_S):
        p1y -= 4
    if jmss.isKeyDown(KEY_I):
        p2y += 4
    if jmss.isKeyDown(KEY_K):
        p2y -= 4

    #Ball movement
    bax += 7*xdir
    bay += 7*ydir

    #Paddle collision
    if (bax <= p1x + 30 and p1y - 64 < bay < p1y + 128):
        xdir = -xdir
        bax = p1x + 32
    if (bax >= p2x - 62 and p2y - 64 < bay < p2y + 128):
        xdir = -xdir
        bax = p2x - 64

    #Checks if a player has scored
    if (bax > width - 64 or bax < 0):
        if (bax > width - 64):
            p1score += 1
            bax = width - 64
            xdir = -xdir
        else:
            p2score += 1
            bax = 0
            xdir = -xdir
    #Checks if ball hits the ceiling
    if (bay > height - 64 or bay < 0):
        ydir = -ydir

    jmss.clear()
    jmss.drawImage(Ball, x = bax, y = bay)
    jmss.drawImage(Paddle, x = p1x, y = p1y)
    jmss.drawImage(Paddle, x = p2x, y = p2y)
    jmss.drawText("Player 1's score is: " + str(p1score) , x = 0, y = height - 14)
    jmss.drawText("Player 2's score is: " + str(p2score) , x = width - 130, y = height - 14)

jmss.run()
