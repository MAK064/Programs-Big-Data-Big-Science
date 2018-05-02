from JMSSGraphicsV12 import *
import math, random

width = 1200
height = 800
fps = 60

jmss = Graphics(width = width, height = height, title = "Graphics", fps = fps)
ball = jmss.loadImage("ball.png")

ZMesh = []

@jmss.mainloop
def Test():
    global CPos, ZMesh, width, height
    jmss.clear(0,0,0,1)

    for x in range(0,120):
        for y in range(0,80):
            z = (((x*10-600)**2)+((y*10-400)**2))/(10**-0.5)
            ZMesh.append([x*10,y*10,z])
            if z <= 10**5:
                jmss.drawPixel((1,0,0,1),x*10,y*10)
            elif 10**5 < z <= 2*10**5:
                jmss.drawPixel((1,1,0,1),x*10,y*10)
            elif 2*10**5 < z <= 4*10**5:
                jmss.drawPixel((0,1,0,1),x*10,y*10)
            elif 4*10**5 < z:
                jmss.drawPixel((0,1,1,1),x*10,y*10)
            else:
                print("error")

    #print(str(ZMesh[random.randint(0,120)*80+random.randint(0,80)]))

jmss.run()
