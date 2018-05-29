from JMSSGraphicsV124 import *
import random
import math

width = 1200
height = 800
fps = 60

particle_amount = int(input("Input how many objects (2-200 reccomended):"))
g = 2/particle_amount
d = 50/1

jmss = Graphics(width = width, height = height, title = "Gravity Sim" , fps = fps)

class Particle():
    def __init__(self, img = None, x = 0, y = 0, x_vel = 0, y_vel = 0, x_acc = 0, y_acc = 0, \
                 width = None, height = None, lifetime = 0, life = 0, opacity = 1.0, \
                 mass = 0, x_grav = 0, y_grav = 0, r = 0, g = 0, b = 0):
        self.x = x
        self.y = y

        self.mass = mass

        self.x_vel = x_vel
        self.y_vel = y_vel
        self.x_acc = x_acc
        self.y_acc = y_acc

        self.img = img
        self.r = r
        self.g = g
        self.b = b

        self.x_grav = x_grav
        self.y_grav = y_grav

particle_list = []

def particleSpawn(x1 = 0, x2 = width, y1 = 0, y2 = height, amount = 1):
    while len(particle_list) < amount:
        p = Particle()
        p.x = random.randint(x1,x2)
        p.y = random.randint(y1,y2)

        p.mass = random.randint(20,400)

        p.x_acc = 0
        p.y_acc = 0

        p.x_vel = random.randint(-1,1)
        p.y_vel = random.randint(-1,1)

        if p.mass < 600/3:
            p.b = 1
        if 400/3 < p.mass < 1000/3:
            p.g = 1
        if 800/3 < p.mass < 400:
            p.r = 1

        particle_list.append(p)

def Gravity_Calc(ob1 , ob2):
    global x_grav, y_grav, x_grav_multi, y_grav_multi, d

    x_grav = 0
    y_grav = 0

    x_distance = (ob2.x * d) - (ob1.x * d)
    y_distance = (ob2.y * d) - (ob1.y * d)
    pythag_dsq = x_distance**2 + y_distance**2

    if pythag_dsq == 0:
        pythag_dsq = 1

    ob1.x_grav += g * (ob1.mass * ob2.mass) * x_distance / pythag_dsq
    ob1.y_grav += g * (ob1.mass * ob2.mass) * y_distance / pythag_dsq

def screenCheck():
    global particle_list, particle_amount
    for i in range(0 , particle_amount):
        if i < len(particle_list):
            if (particle_list[i].x > width + 1 or particle_list[i].x < -1 or \
            particle_list[i].y > height + 1 or particle_list[i].y < -1):
                del particle_list[i]
def physicsApplication(i):
    particle_list[i].x_vel += particle_list[i].x_grav / particle_list[i].mass
    particle_list[i].y_vel += particle_list[i].y_grav / particle_list[i].mass

    particle_list[i].x += particle_list[i].x_vel
    particle_list[i].y += particle_list[i].y_vel

def drawParticle(i):
    jmss.drawPixel(int(particle_list[i].x),int(particle_list[i].y),particle_list[i].r,particle_list[i].g,particle_list[i].b,1)
    jmss.drawPixel(int(particle_list[i].x) + 1,int(particle_list[i].y),particle_list[i].r,particle_list[i].g,particle_list[i].b,1)
    jmss.drawPixel(int(particle_list[i].x) - 1,int(particle_list[i].y),particle_list[i].r,particle_list[i].g,particle_list[i].b,1)
    jmss.drawPixel(int(particle_list[i].x),int(particle_list[i].y + 1),particle_list[i].r,particle_list[i].g,particle_list[i].b,1)
    jmss.drawPixel(int(particle_list[i].x),int(particle_list[i].y - 1),particle_list[i].r,particle_list[i].g,particle_list[i].b,1)

@jmss.mainloop
def Sim():
    global particle_list,particle_amount

    jmss.clear()
    particleSpawn(width/2 - 250,width/2 + 250,height/2 - 250, height/2 + 250, particle_amount)

    for i in range(0 , len(particle_list)):
        for a in range(0 , len(particle_list)):
            if particle_list[i] != particle_list[a]:
                Gravity_Calc(particle_list[i] , particle_list[a])

        physicsApplication(i)

        drawParticle(i)

    for i in range(0 , len(particle_list)):
        particle_list[i].x_grav = 0
        particle_list[i].y_grav = 0

    screenCheck()
jmss.run()
