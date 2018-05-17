from JMSSGraphicsV124 import *
from Particle import *

width = 1200
height = 800
fps = 60

jmss = Graphics(width = width, height = height, title = "Luigi" , fps = fps)

luigis = []

for i in range(0,20):
    luigi = Particle()
    luigi.x = i * 60
    luigi.y = 0
    luigi.img = jmss.loadImage("luigi.png")
    luigis.append(luigi)

@jmss.mainloop
def Screen():
    jmss.clear(0,0,0,1)

    for i in range(0,20):
        jmss.drawImage(luigis[i].img, luigis[i].x, luigis[i].y)


jmss.run()
