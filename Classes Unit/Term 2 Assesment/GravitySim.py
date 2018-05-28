from JMSSGraphicsV124 import *
import random

width = 1200
height = 800
fps = 60

g = 6.674*10**-3

jmss = Graphics(width = width, height = height, title = "Luigi" , fps = fps)

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

for i in range(0,3):
    p = Particle()
    p.x = random.randint(0,1200)
    p.y = random.randint(0,800)

    p.mass = 400 #random.randint(200000,200000)

    p.x_acc = 0
    p.y_acc = 0

    p.x_vel = 0
    p.y_vel = 0

    particle_list.append(p)

def Gravity_Calc(ob1 , ob2):
    global x_grav, y_grav, x_grav_multi, y_grav_multi, g

    x_distance = (ob2.x) - (ob1.x)
    y_distance = (ob2.y) - (ob1.y)
    pythag_distance = math.sqrt(x_distance**2 + y_distance**2)

    print(pythag_distance)

    if x_distance**2 > 1 and y_distance**2 > 4:

        print(True)

        x_vector = (x_distance / (x_distance + y_distance)) * pythag_distance
        y_vector = (y_distance / (x_distance + y_distance)) * pythag_distance

        ob1.x_grav += g*(ob1.mass*ob2.mass)/(x_vector**2)
        ob1.y_grav += g*(ob1.mass*ob2.mass)/(y_vector**2)

        if x_distance < 0:
            ob1.x_grav *= -1
        if y_distance < 0:
            ob1.y_grav *= -1
        if x_distance > 0:
            ob1.x_grav *= 1
        if y_distance > 0:
            ob1.y_grav *= 1

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

        print(particle_list[i].x_grav,particle_list[i].y_grav)

        particle_list[i].x += particle_list[i].x_vel
        particle_list[i].y += particle_list[i].y_vel

        print(particle_list[i].x,particle_list[i].y)
        jmss.drawPixel(int(particle_list[i].x),int(particle_list[i].y),1,1,1,1)
        jmss.drawPixel(int(particle_list[i].x) + 1,int(particle_list[i].y),1,1,1,1)
        jmss.drawPixel(int(particle_list[i].x) - 1,int(particle_list[i].y),1,1,1,1)
        jmss.drawPixel(int(particle_list[i].x),int(particle_list[i].y + 1),1,1,1,1)
        jmss.drawPixel(int(particle_list[i].x),int(particle_list[i].y - 1),1,1,1,1)

    for i in range(0 , len(particle_list)):
        particle_list[i].x_grav = 0
        particle_list[i].y_grav = 0
jmss.run()
