from JMSSGraphicsV12 import *
import math

width = 1200
height = 800
fps = 60

jmss = Graphics(width = width, height = height, title = "Bouncing Ball", fps = fps)

ball = jmss.loadImage("ball.png")

ball_pos = [0,0]
pos = 0

@jmss.mainloop
def Parabola():
    global ball_pos, pos, count

    ball_pos[0] = 0
    jmss.clear(0,0,0,1)

    while ball_pos[0] <= 1152:
        ball_pos[1] = 200*math.sin(ball_pos[0]/200 - pos)+400
        jmss.drawImage(ball, ball_pos[0], ball_pos[1])
        ball_pos[0] += 25

    pos += 0.03

jmss.run()
