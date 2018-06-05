#Matthew Kirk

from JMSSGraphicsV124 import *
import random
import math

#Sets screen info
width = 1200
height = 800
fps = -1

#particle system data
particle_amount = int(input("Input how many objects (100-200 reccomended, 500+ possible):"))
g = 2/(1*particle_amount)
dilation = 80/1
box1 = 250
particle_list = []

jmss = Graphics(width = width, height = height, title = "Gravity Sim" , fps = fps)

#Sets up the particle class
class Particle():
    def __init__(self, img = None, x = 0, y = 0, x_vel = 0, y_vel = 0, x_acc = 0, y_acc = 0, \
                 width = None, height = None, lifetime = 0, life = 0, opacity = 1.0, \
                 mass = 0, x_grav = 0, y_grav = 0, r = 0, g = 0, b = 0):

        self.x = x
        self.y = y

        self.x_vel = x_vel
        self.y_vel = y_vel

        self.x_acc = x_acc
        self.y_acc = y_acc

        self.mass = mass

        self.x_grav = x_grav
        self.y_grav = y_grav

        self.r = r
        self.g = g
        self.b = b

#Function to spawn particles when required
def particleSpawn(radius = 50, amount = 1, x_translation = 0, y_translation = 0):
    #While there are less then the specified amount of particles on the screen
    while len(particle_list) < amount:
        p = Particle()

        #Sets x and y values to be within a circle
        x_temp = 0
        x = random.randint(-1*radius,radius)
        p.y = random.randint(int(height/2 - math.sqrt(radius**2 - x**2)),int(height/2 + math.sqrt(radius**2 - x**2)))
        p.x = x + width/2

        #adds any translations (Not fully implemented)
        p.x += x_translation
        p.y += y_translation

        #Random mass generation
        p.mass = random.randint(40,800)

        #Determines the inital velocity
        p.x_vel = random.random() - 0.5
        p.y_vel = random.random() - 0.5

        #Gives each particle a colour based on mass (Red is heavy -> Blue is light)
        if p.mass < 1200/3:
            #Blue
            p.b = 1
        if 800/3 < p.mass < 2000/3:
            #Green
            p.g = 1
        if 1600/3 < p.mass < 800:
            #Red
            p.r = 1

        particle_list.append(p)

#Calculates the force of gravity between any two given objects
def Gravity_Calc(ob1 , ob2):
    global x_grav, y_grav, x_grav_multi, y_grav_multi, dilation

    #Calculates the distances between given particles
    x_distance = (ob2.x * dilation) - (ob1.x * dilation)
    y_distance = (ob2.y * dilation) - (ob1.y * dilation)
    pythag_dsq = x_distance**2 + y_distance**2

    #Prevents division by 0 errors
    if pythag_dsq == 0:
        pythag_dsq = 1

    #Gives the objects the force of gravity
    ob1.x_grav += g * (ob1.mass * ob2.mass) * x_distance / pythag_dsq
    ob1.y_grav += g * (ob1.mass * ob2.mass) * y_distance / pythag_dsq

#Checks if any particles are off screen
def screenCheck():
    global particle_list, particle_amount
    for i in range(0 , particle_amount):
        #Prevent an index error
        if i < len(particle_list):
            #Checks is particle is off any edge of the screen
            if (particle_list[i].x > width + 1 or particle_list[i].x < -1 or \
            particle_list[i].y > height + 1 or particle_list[i].y < -1):
                del particle_list[i]

#Applies the force of gravity on the particle
def physicsApplication(i):
    #Gravity to velocity
    particle_list[i].x_vel += particle_list[i].x_grav / particle_list[i].mass
    particle_list[i].y_vel += particle_list[i].y_grav / particle_list[i].mass

    #velocity to position
    particle_list[i].x += particle_list[i].x_vel
    particle_list[i].y += particle_list[i].y_vel

#Draws objects as points on the screen
def drawParticle(i):
    jmss.clear()
    #draws the center pixel
    jmss.drawPixel(int(particle_list[i].x),int(particle_list[i].y),particle_list[i].r,particle_list[i].g,particle_list[i].b,1)
    #draws surrounding pixels, can be commented out for smaller particles
    jmss.drawPixel(int(particle_list[i].x) + 1,int(particle_list[i].y),particle_list[i].r,particle_list[i].g,particle_list[i].b,1)
    jmss.drawPixel(int(particle_list[i].x) - 1,int(particle_list[i].y),particle_list[i].r,particle_list[i].g,particle_list[i].b,1)
    jmss.drawPixel(int(particle_list[i].x),int(particle_list[i].y + 1),particle_list[i].r,particle_list[i].g,particle_list[i].b,1)
    jmss.drawPixel(int(particle_list[i].x),int(particle_list[i].y - 1),particle_list[i].r,particle_list[i].g,particle_list[i].b,1)

#Does everything regarding existing particles
def particleManagment():
    #for every pair of objects that isnt the same object twice
    for i in range(0 , len(particle_list)):
        for a in range(0 , len(particle_list)):
            if particle_list[i] != particle_list[a]:
                #do gravity
                Gravity_Calc(particle_list[i] , particle_list[a])
        #apply physics to each particle
        physicsApplication(i)
        #draw each particle
        drawParticle(i)
    #resets each particles gravity to 0
    for i in range(0 , len(particle_list)):
        particle_list[i].x_grav = 0
        particle_list[i].y_grav = 0

@jmss.mainloop
#the sim itself
def Sim():
    #Spawns any missing particles
    particleSpawn(50, particle_amount)
    #Takes care of each particle
    particleManagment()
    #Deletes any particles that are off screen
    screenCheck()
jmss.run()
