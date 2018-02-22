from JMSSGraphics import *

width = 1200 #int(input("Please enter your desired width (>450 reccomended): "))
height = 800 #int(input("Please enter your desired height (>300 reccomended): "))
fps = 10 #int(input("Please enter your desired fps (higher = faster simulation): "))
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

    else:
        jmss.drawImage("mario.png" , x = M1x , y = 0)



    if (M2y >= 20) :
        jmss.drawImage('mario.png' , x = M2x , y = M2y)

    else:
        TFall = -((2/3)*TFall)
        jmss.drawImage("mario.png" , x = M2x , y = 0)


    M1y += 6*G          #Linear Movement
    M2y += (G*TFall)     #Non-Linear Movement
    TFall += 1
    #print(M2y)

jmss.run()
