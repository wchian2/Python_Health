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

