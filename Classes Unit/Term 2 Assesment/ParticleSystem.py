from Particle import *
import random

width = 1200
height = 800
fps = 60

jmss = Graphics(width = width, height = height, title = "Luigi" , fps = fps)

particle_list = []
particle_img = jmss.loadImage("star.png")

for i in range(0,1000):
    star = Particle()
    star.x = random.randint(0,1200)
    star.y = random.randint(0,800)
    star.img = particle_img
    particle_list.append(star)

@jmss.mainloop
def Sim():

    jmss.clear(0,0,0,1)
    for i in range(0,len(particle_list)):
        jmss.drawImage(particle_list[i].img,particle_list[i].x,particle_list[i].y)

    for i in range(0,len(particle_list)):
        particle_list[i].x += random.randint(-20,20)
        particle_list[i].y += random.randint(-20,20)
        if particle_list[i].y >= 800 or particle_list[i].y <= 0:
            particle_list[i].y = height/2
        if particle_list[i].x >= 1200 or particle_list[i].x <= 0:
            particle_list[i].x = width/2

jmss.run()
