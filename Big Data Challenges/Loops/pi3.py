import math

Pi = 0
iter = int(input("How many iterations?"))
count = 1
term = 0

while count <= 100000:
    term = 1/(count*count)
    Pi += term
    print("(" + str(int(count)) + ")" + str(math.sqrt(Pi*6)))
    count +=1
