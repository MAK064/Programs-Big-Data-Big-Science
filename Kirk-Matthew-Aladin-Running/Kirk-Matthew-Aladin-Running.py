from JMSSGraphicsV12 import *

#Sets display settings
width = 1200
height = 800
fps = 60

jmss = Graphics(width = width, height = height, title = "Graphics", fps = fps)

#Initiates lists for animation frames
frames_running = []
frames_jumping = []

#Sets the Y values for the clouds and ground
Cloud_Y = 600
Ground_Y = 191

#Initiates initial positions for Clouds and Ground
Cloud_Positions = [[0,Cloud_Y],[800,Cloud_Y],[1600,Cloud_Y]]
Ground_Positions = [[0,Ground_Y],[800,Ground_Y],[1600,Ground_Y]]

#Initiates counters for managing animation frames
Run_Counter = 0
Ground_Counter = 0
Jump_Counter = 0
Cloud_Counter = 0
count = 0

#Loads Images
    #Loads running frames
for i in range(1,9):
    frames_running.append(jmss.loadImage("Animation and background images/Aladdin0" + str(i) + ".png"))

    #Loads jumping frames
for i in range(1,6):
    frames_jumping.append(jmss.loadImage("Animation and background images/Jump0" + str(i) + ".png"))

    #Loads Clouds and Background images
Cloud = jmss.loadImage("Animation and background images/clouds.png")
Bg = jmss.loadImage("Animation and background images/bg.png")

#Does logic and draws Aladdin when he is running
def Running():
    global Run_Counter, count

    #Uses Run_Counter to detirmine which frame to draw
    jmss.drawImage(frames_running[Run_Counter], width/2 - 86, height/2 - 122)

    #Every 6th display frame increments the Run_Counter
    if count % 6 == 0:
        Run_Counter +=1
    #When the Run_Counter reaches the length of the animation, reset it
    if Run_Counter >= len(frames_running):
        Run_Counter = 0

#Does logic and draws Aladdin when he is jumping
def Jumping():
    global Jump_Counter, count

    #Uses Jump_Counter to detirmine which frame to draw
    jmss.drawImage(frames_jumping[Jump_Counter], width/2 - 86, (height/2 - 122)+(-30*(Jump_Counter-1.75)**2+250))

    #Every 6th display frame increments the Jump_Counter
    if count % 6 == 0:
        Jump_Counter +=1
    #When the Jump_Counter reaches the length of the animation, reset it
    if Jump_Counter >= 5:
        Jump_Counter = 0
#Does logic and drawing for the clouds
def Clouds():
    global Cloud_Counter,Cloud_Positions

    #Every 4th display frame moves all the clouds
    if Cloud_Counter % 4 == 0:
        for element in Cloud_Positions:
            element[0] -= 5

    #For each cloud image
    for element in Cloud_Positions:
        #If the clouds are off screen, move them
        if element[0] <= -800:
            element[0] = 1600
        #Draws the clouds
        jmss.drawImage(Cloud , element[0] , element[1])

    Cloud_Counter += 1

#Does logic and drawing for the ground
def Ground():
    global Ground_Counter,Ground_Positions

    #Every 6th display frame moves the ground
    if Ground_Counter % 6 == 0:
        for element in Ground_Positions:
            element[0] -= 8

    #For each ground image
    for element in Ground_Positions:
        #If the ground is off screen, move it
        if element[0] <= -800:
            element[0] = 1600
        #Draws the ground
        jmss.drawImage(Bg , element[0] , element[1])

    Ground_Counter += 1

#The animation logic
@jmss.mainloop
def Animation():
    global count, Run_Counter
    jmss.clear(0,0,0,1)

    #Detirmines if Aladdin should be jumping or not
    if (jmss.isKeyDown(KEY_SPACE) and (count % 6) == 0) or Jump_Counter != 0:
        Jumping()
    else:
        Running()

    #Runs the clouds and ground
    Ground()
    Clouds()

    count += 1
jmss.run()
