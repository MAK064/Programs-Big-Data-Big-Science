import string

while True:
    inputstr = input("Enter cypher here:")
    inKey = int(input("Enter a key:"))
    cypher = int(input("""Enter "1" to encode or "0" to decode:"""))
    code = []
    out = ""

    for ch in inputstr:
        code.append(ord(ch))

    def cypherBox(key, encode = 0):
        global out
        if encode == 0:
            key *= -1
        for element in range(0,len(code)):
            code[element] = (code[element] + key)
            code[element] = chr(code[element])
            out += str(code[element])
            if encode == 0:
                key -= 1
            else:
                key += 1

    cypherBox(inKey , cypher)

    print(out)
    wait = input("Press enter to continue")
    print(" ")
