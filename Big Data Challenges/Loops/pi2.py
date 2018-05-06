#The most efficient

import math

Pi = 1
iter = int(input("How many iterations?"))
count = 1
term = 0

print(Pi*4)

while True: #count <= 10000:
    term = 1/((1+(count*2))*(1+(count*2)))
    Pi += term
    print("(" + str(int(count)) + ")" + str(math.sqrt(Pi*8)))
    count +=1
