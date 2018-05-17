sort = [2,1]
out = []

class Sorting:
    def compare(self , a , b):

        if a <= b:
            return True
        else:
            return False

    def swap(self , a , b):
        print(a,b)
        c = a
        a = b
        b = c
        print(a,b)

        return([a , b])

    def twoSort(self , a , b):
        if s.compare(a , b) == True:
            out.append(s.swap(a , b))
        else:
            out.append([a , b])

s = Sorting()

s.twoSort(sort[0],sort[1])
print(out)
