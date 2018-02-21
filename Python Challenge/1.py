alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
CypherIn = input("Input Cypher here:")

count = 0
letter = 0
while True:
    letter = ord(CypherIn[count])
    letter += 2
    print(chr(letter))
    count += 1
