from JMSSGraphicsV124 import *
import random
import math

width = 1200
height = 800
fps = 60

g = 6.674*10**-2

jmss = Graphics(width = width, height = height, title = "Gravity Sim" , fps = fps)

class Particle():
    def __init__(self, img = None, x = 0, y = 0, x_vel = 0, y_vel = 0, x_acc = 0, y_acc = 0, \
                 width = None, height = None, lifetime = 0, life = 0, opacity = 1.0, mass = 0):
        self.x = x
        self.y = y

        self.mass = mass

        self.x_vel = x_vel
        self.y_vel = y_vel
        self.x_acc = x_acc
        self.y_acc = y_acc

        self.img = img


particle_list = []

for i in range(0,2):
    p = Particle()
    p.x = random.randint(0,1200)
    p.y = random.randint(0,800)

    p.mass = 4000 #random.randint(200000,200000)

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
    pythag_distance = math.sqrt(abs(x_distance**2 + y_distance**2))

    x_grav =
