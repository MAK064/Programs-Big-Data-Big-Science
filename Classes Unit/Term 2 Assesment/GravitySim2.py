from JMSSGraphicsV124 import *
import random
import math

width = 1200
height = 800
fps = 60

g = 2.5
listlen = 200

jmss = Graphics(width = width, height = height, title = "Gravity Sim" , fps = fps)

class Particle():
    def __init__(self, img = None, x = 0, y = 0, x_vel = 0, y_vel = 0, x_acc = 0, y_acc = 0, \
                 width = None, height = None, lifetime = 0, life = 0, opacity = 1.0, mass = 0, x_grav = 0, y_grav = 0, r = 0, g = 0, b = 0):
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
def particleSpawn():
    while len(particle_list) < listlen:
        p = Particle()
        p.x = random.randint(300,900)
        p.y = random.randint(200,600)

        p.mass = 6 * random.random()

        p.x_acc = 0
        p.y_acc = 0

        p.x_vel = random.randint(-1,1)
        p.y_vel = random.randint(-1,1)

        if p.mass < 1.5:
            p.b = 1
        elif 1.5 < p.mass < 4:
            p.g = 1
        elif 4 < p.mass < 6:
            p.r = 1

        particle_list.append(p)

def Gravity_Calc(ob1 , ob2):
    global x_grav, y_grav, x_grav_multi, y_grav_multi

    x_grav = 0
    y_grav = 0

    x_distance = (ob2.x/30) - (ob1.x/30)
    y_distance = (ob2.y/30) - (ob1.y/30)
    pythag_dsq = x_distance**2 + y_distance**2

    if pythag_dsq == 0:
        pythag_dsq = 1

    ob1.x_grav = g * x_distance / pythag_dsq
    ob1.y_grav = g * y_distance / pythag_dsq

def screenCheck():
    global particle_list, listlen
    for i in range(0 , listlen):
        if i < len(particle_list):
            if (particle_list[i].x > width + 1 or particle_list[i].x < -1 or particle_list[i].y > height + 1 or particle_list[i].y < -1):
                del particle_list[i]


@jmss.mainloop
def Sim():
    global particle_list
    jmss.clear()
    particleSpawn()
    for i in range(0 , len(particle_list)):
        for a in range(0 , len(particle_list)):
            if particle_list[i] != particle_list[a]:
                Gravity_Calc(particle_list[i] , particle_list[a])

        particle_list[i].x_vel += particle_list[i].x_grav / particle_list[i].mass
        particle_list[i].y_vel += particle_list[i].y_grav / particle_list[i].mass

        particle_list[i].x += particle_list[i].x_vel
        particle_list[i].y += particle_list[i].y_vel

        jmss.drawPixel(int(particle_list[i].x),int(particle_list[i].y),particle_list[i].r,particle_list[i].g,particle_list[i].b,1)
        jmss.drawPixel(int(particle_list[i].x) + 1,int(particle_list[i].y),particle_list[i].r,particle_list[i].g,particle_list[i].b,1)
        jmss.drawPixel(int(particle_list[i].x) - 1,int(particle_list[i].y),particle_list[i].r,particle_list[i].g,particle_list[i].b,1)
        jmss.drawPixel(int(particle_list[i].x),int(particle_list[i].y + 1),particle_list[i].r,particle_list[i].g,particle_list[i].b,1)
        jmss.drawPixel(int(particle_list[i].x),int(particle_list[i].y - 1),particle_list[i].r,particle_list[i].g,particle_list[i].b,1)

    for i in range(0 , len(particle_list)):
        particle_list[i].x_grav = 0
        particle_list[i].y_grav = 0
    screenCheck()
jmss.run()
