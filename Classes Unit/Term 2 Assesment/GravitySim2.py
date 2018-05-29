from JMSSGraphicsV124 import *
import random
import math

width = 1200
height = 800
fps = 60

g = 1.75

jmss = Graphics(width = width, height = height, title = "Gravity Sim" , fps = fps)

class Particle():
    def __init__(self, img = None, x = 0, y = 0, x_vel = 0, y_vel = 0, x_acc = 0, y_acc = 0, \
                 width = None, height = None, lifetime = 0, life = 0, opacity = 1.0, mass = 0, x_grav = 0, y_grav = 0):
        self.x = x
        self.y = y

        self.mass = mass

        self.x_vel = x_vel
        self.y_vel = y_vel
        self.x_acc = x_acc
        self.y_acc = y_acc

        self.img = img

        self.x_grav = x_grav
        self.y_grav = y_grav

particle_list = []

for i in range(50):
    p = Particle()
    p.x = random.randint(0,1200)
    p.y = random.randint(0,800)

    p.mass = random.randint(1,4)

    p.x_acc = 0
    p.y_acc = 0

    p.x_vel = 0
    p.y_vel = 0

    particle_list.append(p)

def Gravity_Calc(ob1 , ob2):
    global x_grav, y_grav, x_grav_multi, y_grav_multi

    x_grav = 0
    y_grav = 0

    x_distance = ob2.x - ob1.x
    y_distance = ob2.y - ob1.y
    pythag_dsq = x_distance**2 + y_distance**2

    if pythag_dsq == 0:
        pythag_dsq = 1

    ob1.x_grav = g * x_distance / pythag_dsq
    ob1.y_grav = g * y_distance / pythag_dsq

@jmss.mainloop
def Sim():
    global particle_list
    jmss.clear()
    for i in range(0 , len(particle_list)):
        for a in range(0 , len(particle_list)):
            if particle_list[i] != particle_list[a]:
                Gravity_Calc(particle_list[i] , particle_list[a])

        particle_list[i].x_vel += particle_list[i].x_grav / particle_list[i].mass
        particle_list[i].y_vel += particle_list[i].y_grav / particle_list[i].mass

        particle_list[i].x += particle_list[i].x_vel
        particle_list[i].y += particle_list[i].y_vel

        jmss.drawPixel(int(particle_list[i].x),int(particle_list[i].y),1,1,1,1)
        jmss.drawPixel(int(particle_list[i].x) + 1,int(particle_list[i].y),1,1,1,1)
        jmss.drawPixel(int(particle_list[i].x) - 1,int(particle_list[i].y),1,1,1,1)
        jmss.drawPixel(int(particle_list[i].x),int(particle_list[i].y + 1),1,1,1,1)
        jmss.drawPixel(int(particle_list[i].x),int(particle_list[i].y - 1),1,1,1,1)

    for i in range(0 , len(particle_list)):
        particle_list[i].x_grav = 0
        particle_list[i].y_grav = 0
jmss.run()
