sort = [2,1]
out = []

class Sorting:
    def compare(a , b):
        if a <= b:
            return True
        else:
            return False

    def swap(a , b):
        c = a
        a = b
        b = c

        return([a , b])

    def twoSort(a , b , c):
        print(a,b,c)
        if compare(a , b) == True:
            out = swap(a , b)
        else:
            out = [a , b]

s = Sorting()

s.twoSort(sort[0],sort[1])
print(out)
