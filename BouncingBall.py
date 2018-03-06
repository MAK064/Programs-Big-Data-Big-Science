from JMSSGraphics import *
import random

# Dimentions
width = 1200
height = 800
fps = 60

jmss = Graphics(width = width, height = height, title = "Bouncing Ball", fps = fps)

#Setting Initail Variables (Randomly)
BallX = random.randint(1, (height - 65))
BallY = random.randint(1, (height - 65))

momentum = random.uniform(0, 10)
G = random.uniform(1, -1)
TFall = random.uniform(-100, 0)

if (random.randint(0, 1) == 1):
    direction = 1
else:
    direction = -1

#Debug Tools
print (direction)
print (momentum)
print (G)
print (TFall)
print ("(" + str(BallX) + ", " + str(BallY) + ")")

ball = jmss.loadImage("ball.png")

@jmss.mainloop
def simulation():
    global BallX, BallY, TFall, G, width, direction, momentum

    jmss.clear(0,0,0,1)

    #Does logic and draws mario when inbetween top and bottom of screen
    if 0 <= BallY < (height - 64):
        jmss.drawImage( ball , x = BallX, y = BallY)
        BallX += direction*momentum
        BallY += G*TFall

    #Does logic and draws mario when above top of screen
    elif BallY >= (height - 64):
        jmss.drawImage( ball , x = BallX, y = (height - 64))
        TFall = TFall*(-0.5)
        BallX += direction * momentum
        BallY = height - 64 + G*TFall

    #Does logic and draws mario when below screen
    else:
        jmss.drawImage( ball , x = BallX, y = 0)
        TFall = TFall*(-1)
        BallX += direction * momentum
        BallY += G*TFall

    #Logic for x direcion reversal
    if (0 >= BallX or BallX >= (width - 64)):
        direction = direction*(-1)

    #Draws text onscreen displaying info
    jmss.drawText("Ball's Position is: (" + str(int(BallX)) + ", " + str(int(BallY)) + ")" , x = 0, y = 0)
    jmss.drawText("G = " + str(G/(2/6))  , x = width - 68, y = 0)
    jmss.drawText("Ball's sideways momentum is ~ " + str(int(momentum)) , x = width - 205, y = 12)

    #Increment timefalling
    TFall += 1

jmss.run()