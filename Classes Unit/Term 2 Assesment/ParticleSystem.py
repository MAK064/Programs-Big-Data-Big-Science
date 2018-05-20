from Particle import *
import random

width = 1200
height = 800
fps = 60

jmss = Graphics(width = width, height = height, title = "Luigi" , fps = fps)

particle_list = []
particle_img = jmss.loadImage("star.png")

for i in range(0,250):
    star = Particle()
    star.x = random.randint(-42,1158)
    star.y = random.randint(-42,758)
    star.vel_x = random.randint(-5,5)
    star.vel_y = random.randint(-5,-1)
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
