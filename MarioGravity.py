from JMSSGraphics import *

width = 1200 #int(input("Please enter your desired width (>450 reccomended): "))
height = 800 #int(input("Please enter your desired height (>300 reccomended): "))
fps = 60 #int(input("Please enter your desired fps (higher = faster simulation): "))
jmss = Graphics(width = width, height = height, title = "Test Game", fps = fps)

M1x = width / 3
M1y = height - (height/5)
M2x = width / 3 *2
M2y = height - (height/5)
G = (0-1/6)        #10m/s /60s
TFall = 0

@jmss.mainloop
def Game():
    global M1y, M1x, M2y, M2x, TFall, G

    jmss.clear(0,0,0,1)
    if (M1y >= 0) :
        jmss.drawImage("mario.png" , x = M1x , y = M1y)
        M1y += (6*G)
    else:
        jmss.drawImage("mario.png" , x = M1x , y = 0)
        M1y = 0

    if (M2y >= 1) :
        jmss.drawImage('mario.png' , x = M2x , y = M2y)
        M2y += (G*TFall)

    elif(M2y < 1):
        jmss.drawImage("mario.png" , x = M2x , y = 0)
        TFall = -((7/10)*TFall)                                 #Detirmines how much velocity carries over after bouncing
        M2y += (G*TFall)

    if (M2y <= 1):                                              #Checks if M2Y is still below 5
        M2x -= 0.5
        M2y = 0

    jmss.drawText("Mario2's Co-ordinates: (" + str(int(M2x)) + ", " + str(int(M2y)) + ")",x = 0 ,y = 0)
    jmss.drawText("Mario1's Co-ordinates: (" + str(int(M1x)) + ", " + str(int(M1y)) + ")",x = 0 ,y = 13)

    M2x += 0.5
    TFall += 1


jmss.run()
