from JMSSGraphics import *
import random
import time

width = 1200
height = 800
fps = 60

jmss = Graphics(width = width, height = height, title = "Bouncing Ball", fps = fps)

Ball = jmss.loadImage("ball.png")
Paddle = jmss.loadImage("Pong Paddle.jpg")

gamestate = "null"

def pointReset():
    global bax, bay, xdir, ydir, p1x, p1y, p2x, p2y, p1score, p2score, width, height
    bax = width/2
    bay = height/2

    if random.randint(0,1) == 1:
        xdir = 1
    else:
        xdir = -1

    if random.randint(0,1) == 1:
        ydir = 1
    else:
        ydir = -1

    p1x = 1/12*width - 16
    p1y = 1/2*height - 64

    p2x = 11/12*width - 16
    p2y = 1/2*height - 64

def gameReset():
    global p1score, p2score, winner

    p1score = 0
    p2score = 0
    winner = 0

    pointReset()

    Ball = jmss.loadImage("ball.png")
    Paddle = jmss.loadImage("Pong Paddle.jpg")

def gameDraw():
    jmss.clear()
    jmss.drawImage(Ball, x = bax, y = bay)
    jmss.drawImage(Paddle, x = p1x, y = p1y)
    jmss.drawImage(Paddle, x = p2x, y = p2y)
    jmss.drawText("Player 1's score is: " + str(p1score) , x = 0, y = height - 14)
    jmss.drawText("Player 2's score is: " + str(p2score) , x = width - 130, y = height - 14)

@jmss.mainloop
def Pong ():
    global bax, bay, xdir, ydir, height, p1y, p1x, p2y, p2x, p1score, p2score, gamestate, winner

    if gamestate == "null":
        gameReset()
        gamestate = "start"


    if gamestate == "start":
        if jmss.isKeyDown(KEY_SPACE):
            gamestate = "play"
        jmss.clear()
        jmss.drawText("Pong", x = width/2 - 50, y = height - height/5, fontSize = 40)
        jmss.drawText("Press Space to play" , width/2 - 100, 50, fontSize = 20)


    if gamestate == "play":

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

        #Checks if ball hits the ceiling/ floor (Collision with top/bottom walls)
        if (bay > height - 64 or bay < 0):
            ydir = -ydir

        #Checks if a player has scored (Collision with a side wall)
        if (bax > width - 64 or bax < 0):
            if (bax > width - 64):
                p1score += 1
                pointReset()
            else:
                p2score += 1
                pointReset()

        if p1score == 5:
            gamestate = "end"
            winner = 1
        if p2score == 5:
            gamestate = "end"
            winner = 2

        gameDraw()


    if gamestate == "end":
        if jmss.isKeyDown(KEY_SPACE):
            gamestate = "null"
            time.sleep(0.5)

        jmss.clear()
        jmss.drawText("Congratulations player " + str(winner) + ", you win!", 275 , height/2, fontSize = 30)
        jmss.drawText("Press Space to play again" , 500, 50, fontSize = 10)

jmss.run()
