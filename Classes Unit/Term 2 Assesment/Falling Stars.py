from JMSSGraphicsV124 import *
import random

width = 1200
height = 800
fps = 60

jmss = Graphics(width = width, height = height, title = "Luigi" , fps = fps)

class Particle():
    def __init__(self, img = None, x = 0, y = 0, vel_x = 0, vel_y = 0, acc_x = 0, acc_y = 0, \
                 width = None, height = None, lifetime = 0, life = 0, opacity = 1.0, weight = 0):
        self.x = x
        self.y = y

        self.weight = weight

        self.vel_x = vel_x
        self.vel_y = vel_y

        self.img = img


particle_list = []
particle_img = jmss.loadImage("star.png")

for i in range(0,250):
    star = Particle()
    star.x = random.randint(-42,1200)
    star.y = random.randint(-42,800)
    star.vel_x = random.randint(-5,5)
    star.vel_y = random.randint(-10,-1)
    star.img = particle_img
    particle_list.append(star)

@jmss.mainloop
def Sim():

    jmss.clear(0,0,0,1)
    for i in range(0,len(particle_list)):
        jmss.drawImage(particle_list[i].img,particle_list[i].x,particle_list[i].y)

    for i in range(0,len(particle_list)):

        particle_list[i].x += particle_list[i].vel_x
        particle_list[i].y += particle_list[i].vel_y

        if particle_list[i].x >= 1200:
            particle_list[i].x = -42
        elif particle_list[i].x <= -42:
            particle_list[i].x = 1200

        if particle_list[i].y >= 800:
            particle_list[i].y = -42
        elif particle_list[i].y <= -42:
            particle_list[i].y = 800

jmss.run()
