# Dictionaries

messages = {'date':'01-22-19', 'sender':'me', 'receiver':'you',
            'message':'Hey man how dee do ???'}

print(messages['message'])
print(messages.items()) # items() method

spam = {'color': 'red', 'age': 42}
print(list(messages.values())) # values method

print(messages.get('message2', "hi"))

import pprint
pprint.pprint(messages)

# Data structure of a tic-tac-toe-board

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
theBoard['mid-M'] = 'X'
printBoard(theBoard)

"""
turn = 'X'
for i in range(9):
    print(theBoard)
    print('Turn for ' + turn + '. Move on which space??')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard)
"""

allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
                'Bob': {'ham sandwiches': 3, 'apples': 2},
                'Carol': {'cups': 3, 'apple pies': 1}}

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('Number of things being brought:')
print(' - Apples         ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups           ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes          ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies')))



# Fantasy game inventory

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

# Outputs
"""
Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger
Total number of items: 62
"""

def displayInventory(dictionary):

    print("Inventory:")

    count = 0

    keyList = dictionary.keys()

    for key in sorted(keyList):
        print(str(key) + " " + str(dictionary[key]))
        count += dictionary[key]

    print("Total number of items: " + str(count))

displayInventory(inventory)


# List to Dictionary Function for Fantasy Game Inventory

print("List to Dictionary Function for Fantasy Game Inventory \n")
def addToInventory(dictionary, addedItems):

    currentKeyList = dictionary.keys()

    for item in addedItems:
        if item not in currentKeyList:
            dictionary[item] = 1
        else:
            dictionary[item] += 1

    return dictionary # this is important, without it, the code won't work

inv = {'gold coin': 42, 'rope': 1}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)