from JMSSGraphics import *

jmss = Graphics(width = 1200, height = 800, title = "Test Game", fps = 60)
width = 1200
height = 800
M1x = 400
M1y = 700
M2x = 800
M2y = 700
G = 1/6
Time = 0

@jmss.mainloop
def Game():
    #print("hello world")
    global M1y, M1x, M2y, M2x, Time, G
    jmss.drawImage("mario.png" , x = 400 , y = M1y)
    jmss.drawImage('mario.png' , x = 800, y = M2y)

    M1y -= G #Linear Movement
    M2y -= (G*Time) #Non-Linear Movement
    Time += 1

jmss.run()
