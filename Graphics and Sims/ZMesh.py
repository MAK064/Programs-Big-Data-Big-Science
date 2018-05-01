from JMSSGraphicsV12 import *
import math

width = 1200
height = 800
fps = 60

jmss = Graphics(width = width, height = height, title = "Graphics", fps = fps)
ball = jmss.loadImage("ball.png")

CPos = [0,0]
ZMesh = []

@jmss.mainloop
def Test():
    global CPos, ZMesh, width, height
    jmss.clear(0,0,0,1)
    CPos[0] = 0
    CPos[1] = 0
    
    while CPos[0] <= width:

        while CPos[1] <= height:

            z = (CPos[0]**2)+(CPos[1]**2)/(10**7)
            ZMesh.append([CPos[0],CPos[1],z])
            CPos[1] +=10

        CPos[0] += 10

    print(ZMesh)

jmss.run()
