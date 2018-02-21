from JMSSGraphics import *

width = int(input("Please enter your desired width (>450 reccomended): "))
height = int(input("Please enter your desired height (>300 reccomended): "))
fps = int(input("Please enter your desired fps (higher = faster simulation) :"))
jmss = Graphics(width = width, height = height, title = "Test Game", fps = fps)
M1x = width / 3
M1y = height - (height/5)
M2x = width / 3 *2
M2y = height - (height/5)
G = 1/6        #10m/s /60s
Time = 0

@jmss.mainloop
def Game():
    global M1y, M1x, M2y, M2x, Time, G

    jmss.clear(0,0,0,1)
    if (M1y >= 0) : #Checks is Mario is at y = 0
        jmss.drawImage("mario.png" , x = M1x , y = M1y)
    else:           #Makes sure Mario doesn't disapear when he reaches y = 0
        jmss.drawImage("mario.png" , x = M1x , y = 0)
    if (M2y >= 0) : #Checks is Mario is at y = 0
        jmss.drawImage('mario.png' , x = M2x , y = M2y)
    else:           #Makes sure Mario doesn't disapear when he reaches y = 0
        jmss.drawImage("mario.png" , x = M2x , y = 0)

    M1y -= G #Linear Movement
    M2y -= (G*Time) #Non-Linear Movement
    Time += 1

jmss.run()
