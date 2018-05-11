Pi = 1
iter = int(input("How many iterations?"))
count = 1
term = 0

print(Pi*4)

while count <= 100000:
    term = 1/(1+(count*2))
    if count % 2 != 0:
        term = -term
    Pi += term
    print("(" + str(int(count)) + ")" + str(Pi*4))
    count +=1
