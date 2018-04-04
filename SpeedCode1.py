import random

def reset():
    global deck, p1, dealer, midCard
    deck = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52]
    p1 = []
    dealer = []
    midCard = 0

def dealCards (dealt , number = 1):
    global deck, p1, dealer, midCard
    while number > 0:
        cardRem = random.randint(0,(51 - midCard))
        dealt.append(deck[cardRem])
        deck.remove(deck[cardRem])
        number -= 1
        midCard += 1

def intialDeal():
    dealCards(p1 , 2)
    dealCards(dealer , 2)

def handDisplay(player):
    display = []
    for element in player:
        floorDiv = (element - 1) // 13
        mod = (element - 1)%13
        if floorDiv == 0:
            display.append(str(mod + 1) + "C")
        elif floorDiv == 1:
            display.append(str(mod + 1) + "S")
        elif floorDiv == 2:
            display.append(str(mod + 1) + "D")
        elif floorDiv == 3:
            display.append(str(mod + 1) + "H")
    print(display)

while True:
    reset()
    intialDeal()

    handDisplay(p1)
    handDisplay(dealer)
    handDisplay(deck)
    wait = input("Press enter to continue")
