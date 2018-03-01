from JMSSGraphics import *

# Dimentions
width = 1200
height = 800
fps = 60

jmss = Graphics(width = width, height = height, title = "Bouncing Ball", fps = fps)

#Setting Initail Variables
BallX = 1/3*width
BallY = 2/3*height
TFall = 0
direction = 1
momentum = 5
G = -2/6

@jmss.mainloop
def simulation():
    global BallX, BallY, TFall, G, width, direction, momentum

    jmss.clear(0,0,0,1)

    #Draws Mario
    if 0 <= BallY < (height - 64):
        jmss.drawImage("ball.png", x = BallX, y = BallY)
        BallX += direction*5
        BallY += G*TFall
    elif BallY >= (height - 64):
        jmss.drawImage("ball.png", x = BallX, y = (height - 64))
        TFall = TFall*(-1)
        BallX += direction * momentum
        BallY += G*TFall
    else:
        jmss.drawImage("ball.png", x = BallX, y = 0)
        TFall = TFall*(-1.02)
        BallX += direction * momentum
        BallY += G*TFall
    if (0 >= BallX or BallX >= (width - 64)):
        direction = direction*(-1)

    jmss.drawText("Ball's Position is: (" + str(int(BallX)) + ", " + str(int(BallY)) + ")" , x = 0, y = 0)

    TFall += 1

jmss.run()
