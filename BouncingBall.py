from JMSSGraphics import *

width = 1200
height = 800
fps = 60

jmss = Graphics(width = width, height = height, title = "Bouncing Ball", fps = fps)

BallX = 1/3*width
BallY = 2/3*height
TFall = 0
direction = 1
G = -2/6

@jmss.mainloop
def simulation():
    global BallX, BallY, TFall, G, width, direction

    jmss.clear(0,0,0,1)
    if 0 <= BallY:
        jmss.drawImage("ball.png", x = BallX, y = BallY)
        BallX += direction*5
        BallY += G*TFall
    else:
        jmss.drawImage("ball.png", x = BallX, y = 0)
        TFall = TFall*(-0.98)
        BallX += direction *5
        BallY += G*TFall
    if (0 >= BallX or BallX >= (width - 64)):
        direction = direction*(-1)

    jmss.drawText("Ball's Position is: (" + str(int(BallX)) + ", " + str(int(BallY)) + ")" , x = 0, y = 0)

    TFall += 1

jmss.run()
