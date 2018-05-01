from JMSSGraphicsV12 import *
import math

width = 1200
height = 800
fps = 60

jmss = Graphics(width = width, height = height, title = "Graphics", fps = fps)

ball = jmss.loadImage("ball.png")

ball_pos = [0,0,0]
r = [320]

def Equasion():
    if 600 - r[0] <= ball_pos[0] <= 600 + r[0]:
        ball_pos[1] = math.sqrt(r[0]**2 - (ball_pos[0] - 600)**2) + 400
    else:
        ball_pos[1] = -1000

    if 600 - r[0] <= ball_pos[0] <= 600 + r[0]:
        ball_pos[2] = -1*math.sqrt(r[0]**2 - (ball_pos[0] - 600)**2) + 400
    else:
        ball_pos[2] = -1000

@jmss.mainloop
def Parabola():
    global ball_pos

    ball_pos[0] = 0
    jmss.clear(0,0,0,1)

    while ball_pos[0] <= 1152:
        Equasion()

        if ball_pos[2] != 0:
            jmss.drawImage(ball, ball_pos[0], ball_pos[1])
            jmss.drawImage(ball, ball_pos[0], ball_pos[2])
        else:
            jmss.drawImage(ball, ball_pos[0], ball_pos[1])

        ball_pos[0] += 8
jmss.run()
