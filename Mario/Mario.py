from JMSSGraphics import *

jmss = Graphics(width = 1200, height = 800, title = "Test Game", fps = 60)

@jmss.mainloop
def Game():
    jmss.drawImage("mario.png" , x = 400 , y = 700)

jmss.run()
