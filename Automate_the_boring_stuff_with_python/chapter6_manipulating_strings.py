print("William"[:-3]) # Output "Will" ... this gives me an idea...

name = "This place"
print(name.upper()) # THIS PLACE

print("william".isalpha()) # True

print("William".startswith("Will")) # True

print("William".center(50, '-')) # ---------------------William----------------------

def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 15, 5)
printPicnic(picnicItems, 20, 6)

import pyperclip
pyperclip.copy('Hello world!')
pyperclip.copy('Greetings world!!')
print(pyperclip.paste())

# Table Printer Problem Set

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(list):

    colWidths = [0] * len(list)
    colWidths_index = 0
    for item in tableData:
        colWidths[colWidths_index] = max([len(x) for x in item])
        colWidths_index += 1

    new_list = []
    for x in range(len(tableData[0])):
        for y in range(len(tableData)):
            new_list.append(tableData[y][x])

    for x in range(len(new_list)):
        print(new_list[x].rjust(colWidths[x % 3]), end=' ')
        if x % 3 == 2:
            print('\n')

printTable(tableData)