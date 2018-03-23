from JMSSGraphics import *
import random
import time

#Graphics startup
width = 1200
height = 800
fps = 60
jmss = Graphics(width = width, height = height, title = "Bouncing Ball", fps = fps)

#Load images and sounds
Ball = jmss.loadImage("ball.png")
Paddle = jmss.loadImage("Pong Paddle.jpg")
GreenZ = jmss.loadImage("Green Zone.png")
RedZ = jmss.loadImage("RedZone.png")
p1blip = jmss.loadSound("BlipF4.wav")
p2blip = jmss.loadSound("BlipF5.wav")

#Sets initial gamestate
gamestate = "null"

#Resets game after a point
def pointReset():
    global bax, bay, xdir, ydir, p1x, p1y, p2x, p2y, p1score, p2score, width, height, reset, Redx, Greenx
    bax = width/2
    bay = height/2

    #X direction (positive or negative)
    if random.randint(0,1) == 1:
        xdir = 1
    else:
        xdir = -1

    #Y direction (positive or negative)
    if random.randint(0,1) == 1:
        ydir = 1
    else:
        ydir = -1

    #Paddle placement
    p1x = 1/12*width - 16
    p1y = 1/2*height - 64

    p2x = 11/12*width - 16
    p2y = 1/2*height - 64

    #Red Zone Placement
    Redx = random.randint(p1x + 16, p2x - 144)

    #Green Zone Placement
    Greenx = random.randint(p1x + 16, p2x - 144)

    #Detirmines if reset has occured
    reset = 1

#Resets the game
def gameReset():
    global p1score, p2score, winner, reset

    p1score = 0
    p2score = 0
    winner = 0
    reset = 1

    pointReset()

#Draws objects in the game
def gameDraw():
    jmss.clear()
    jmss.drawImage(RedZ, Redx, 0)
    jmss.drawImage(GreenZ, Greenx, 0)
    jmss.drawImage(Ball, x = bax, y = bay)
    jmss.drawImage(Paddle, x = p1x, y = p1y)
    jmss.drawImage(Paddle, x = p2x, y = p2y)
    jmss.drawText("Player 1's score is: " + str(p1score) , x = 0, y = height - 16)
    jmss.drawText("Player 2's score is: " + str(p2score) , x = width - 130, y = height - 16)

@jmss.mainloop
#Game logic
def Pong ():
    global bax, bay, xdir, ydir, height, p1y, p1x, p2y, p2x, p1score, p2score, gamestate, winner, reset, p1blip, p2blip

    #Runs game reset
    if gamestate == "null":
        gameReset()
        gamestate = "start"

    #Start screen
    if gamestate == "start":
        #Checks if the space bar is down to start the game
        if jmss.isKeyDown(KEY_SPACE):
            gamestate = "play"

        #Draws the start screen
        jmss.clear()
        jmss.drawText("Pong", x = width/2 - 50, y = height - height/5, fontSize = 40)
        jmss.drawText("Controls", width/5, 3*height/5, fontSize = 30)
        jmss.drawText("Player 1: Use 'W' and 'S' to move up and down", width/10, 5*height/10, fontSize = 15)
        jmss.drawText("Player 2: Use 'I' and 'K' to move up and down", width/10, 5*height/10 - 20, fontSize = 15)
        jmss.drawText("Information", 3*width/5+100, 3*height/5, fontSize = 30)
        jmss.drawText("The first player to get to five points wins", 6*width/10, 5*height/10, fontSize = 15)
        jmss.drawText("The green zone makes the ball move faster", 6*width/10, 5*height/10 - 20, fontSize = 15)
        jmss.drawText("The red zone makes the ball move slower", 6*width/10, 5*height/10 - 40, fontSize = 15)
        jmss.drawText("Press Space to play" , width/2 - 100, 50, fontSize = 20)

    #Win screen amd reset
    if gamestate == "end":
        # Checks if the space bar is down to reset the game
        if jmss.isKeyDown(KEY_SPACE):
            gamestate = "null"
            time.sleep(0.5)

        #Draws the end screen
        jmss.clear()
        jmss.drawText("Congratulations player " + str(winner) + ", you win!", 275 , height/2, fontSize = 30)
        jmss.drawText("Press Space to play again" , 500, 50, fontSize = 10)

    #Game code
    if gamestate == "play":

        #Pauses after a reset
        if reset == 1:
            time.sleep(1)
            reset = 0

        #Key Checks and respective movements
        if jmss.isKeyDown(KEY_W):
            p1y += 7
        if jmss.isKeyDown(KEY_S):
            p1y -= 7
        if jmss.isKeyDown(KEY_I):
            p2y += 7
        if jmss.isKeyDown(KEY_K):
            p2y -= 7

        #Ball movement
        #Moves the ball in the x direction
        bax += 7*xdir

        #Checks if the ball is in the green/red box and applies appropriate y movement
        if Greenx - 64 < bax < Greenx + 192:
            bay += 7*ydir*2
        elif Redx - 64 < bax < Redx + 192:
            bay += 7*ydir*0.4
        else:
            bay += 7*ydir

        #Paddle collision
        #If the ball would make contact with paddle 1 or 2 it snaps the ball to the paddle and reverses the direction it goes in
        if (p1x <= bax <= p1x + 30 and p1y - 64 < bay < p1y + 128):
            xdir = -xdir
            bax = p1x + 32
            jmss.playSound(p1blip, False)
        if (p2x >= bax >= p2x - 62 and p2y - 64 < bay < p2y + 128):
            xdir = -xdir
            bax = p2x - 64
            jmss.playSound(p2blip, False)

        #Checks if ball hits the ceiling/ floor (Collision with top/bottom walls)
        if bay > height - 64:
            ydir = -ydir
            bay = height - 64
        elif bay < 0:
            ydir = -ydir
            bay = 0


        #Checks if a player has scored (Collision with a side wall)
        if (bax > width - 64 or bax < 0):
            if (bax > width - 64):
                p1score += 1
                pointReset()
            else:
                p2score += 1
                pointReset()

        #If a player hits 5 points, the game goes into the end state
        if p1score == 5:
            gamestate = "end"
            winner = 1
        if p2score == 5:
            gamestate = "end"
            winner = 2

        #Draws everything for the game
        gameDraw()

jmss.run()
