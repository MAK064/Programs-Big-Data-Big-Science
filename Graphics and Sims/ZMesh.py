from JMSSGraphicsV12 import *
import math

width = 1200
height = 800
fps = 60

jmss = Graphics(width = width, height = height, title = "Graphics", fps = fps)
ball = jmss.loadImage("ball.png")

ZMesh = []

#Prerequisits
for x in range(0,120):
    for y in range(0,80):
        z = (x**2)+(y**2)/(10**7)
        ZMesh.append([x*10,y*10,z])

@jmss.mainloop
def Test():
    global CPos, ZMesh, width, height
    jmss.clear(0,0,0,1)

    for x in range(0,120):
        for y in range(0,80):
            jmss.drawText()

jmss.run()
