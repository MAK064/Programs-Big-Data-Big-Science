from JMSSGraphicsV12 import *

width = 1200
height = 800
fps = 60

jmss = Graphics(width = width, height = height, title = "Graphics", fps = fps)

frunning = []
fjump = []

rcount = 0
jcount = 0
count = 0

#Loads Images
for i in range(1,9):
    frunning.append(jmss.loadImage("Animation and background images/Aladdin0" + str(i) + ".png"))
for i in range(1,6):
    fjump.append(jmss.loadImage("Animation and background images/Jump0" + str(i) + ".png"))

def Running():
    global rcount, count
    jmss.drawImage(frunning[rcount], width/2 - 86, height/2 - 122)

    if count % 6 == 0:
        rcount +=1
    if rcount >= 8:
        rcount = 0

def Jumping():
    global jcount, count
    jmss.drawImage(fjump[jcount], width/2 - 86, (height/2 - 122)+(-30*(jcount-1.75)**2+250))

    if count % 6 == 0:
        jcount +=1
    if jcount >= 5:
        jcount = 0

@jmss.mainloop
def Animation():
    global count, rcount
    jmss.clear(0,0,0,1)

    if jmss.isKeyDown(KEY_SPACE) or jcount != 0:
        Jumping()
    else:
        Running()

    count += 1
jmss.run()
