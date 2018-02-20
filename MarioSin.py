from JMSSGraphics import *
import math
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
    jmss.drawImage("mario.png" , x = M1x , y = M1y)
    jmss.drawImage('mario.png' , x = M2x, y = M2y)

    M1y -= 12 #Frequency
    M1x = 200*math.sin(Time/5) + 400 #Make Mario move in Sinusoidal manner
    M2y -= (G*Time) #Non-Linear Movement
    Time += 1

jmss.run()
