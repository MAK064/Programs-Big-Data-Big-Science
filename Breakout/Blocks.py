from JMSSGraphicsV124 import *

height = 600
jmss = Graphics(width = 800, height = height, title = "Test" , fps = -1)

class Particle():
    def __init__(self, img = None, x = 0, y = 0, hardness = 1):

        self.x = x
        self.y = y

        self.hardness = hardness

block_list = []
B_image1 = "Block.png"

def spawnBlock(row = 0, col = 0, hardness = 1, blist = block_list):

    b = Particle()

    b.x = 50 + 100*col
    b.y = height -100 -50*row
    b.hardness = hardness

    blist.append(b)

def drawBlocks():
    jmss.clear()
    for i in range(0, len(block_list)):
        jmss.drawImage(B_image1, block_list[i].x, block_list[i].y)

#an example if you need it
@jmss.mainloop
def Test():
    for h in range(0,7):
        for w in range(0,7):
            spawnBlock(row = h, col = w)
    drawBlocks()
jmss.run()
