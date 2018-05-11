from JMSSGraphicsV12 import *
import math

width = 1200
height = 800
fps = 60

jmss = Graphics(width = width, height = height, title = "Bouncing Ball", fps = fps)

ball = jmss.loadImage("ball.png")

ball_pos = [0,0]
speed = 0
count = 0

@jmss.mainloop
def Parabola():
    global ball_pos, speed, count

    ball_pos[0] = 0
    jmss.clear(0,0,0,1)

    while ball_pos[0] <= 1152:
        ball_pos[1] = 200*math.sin(2*ball_pos[0] - speed)+400
        jmss.drawImage(ball, ball_pos[0], ball_pos[1])
        ball_pos[0] += (22 + count)

    jmss.drawText(str(count + 22), 0, 0)

    if jmss.isKeyDown(KEY_SPACE) != True:
        count += 0.003
    speed += 0.03

jmss.run()
