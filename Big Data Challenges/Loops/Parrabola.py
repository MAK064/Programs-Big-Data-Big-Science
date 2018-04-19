from JMSSGraphics import *
import math

width = 1200
height = 800
fps = 60

jmss = Graphics(width = width, height = height, title = "Bouncing Ball", fps = fps)

ball = jmss.loadImage("ball.png")

ball_pos = [0,0]

@jmss.mainloop
def Parabola():
    global ball_pos
    while ball_pos[0] <= 1200:
        ball_pos[1] = math.sin(ball_pos[0])*128
        jmss.drawImage(ball, ball_pos[0], ball_pos[1] + 300)
        ball_pos[0] += 32
jmss.run()
