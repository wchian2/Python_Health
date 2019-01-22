# Passing references

def eggs(someParameter):
    someParameter.append("Hello")

spam = [1,2,3]
eggs(spam)
print(spam)

# Practice assignments

# Comma Code

spam = ['apples', 'bananas', 'tofu', 'cats']

def listingOut(list):
    newList = []
    for i in list[:-1]:
        newList.append(i)
    newList.append("and " + list[-1])
    sentence = ""
    for i in newList:
        sentence += i + ", "
    return "\'" + sentence[:-2] + "\'"

print(listingOut(spam))

# Character Picture Grid

grid = [['.', '.', '.', '.', '.', '.'],#0
        ['.', 'O', 'O', '.', '.', '.'],#1
        ['O', 'O', 'O', 'O', '.', '.'],#2
        ['O', 'O', 'O', 'O', 'O', '.'],#3
        ['.', 'O', 'O', 'O', 'O', 'O'],#4
        ['O', 'O', 'O', 'O', 'O', '.'],#5
        ['O', 'O', 'O', 'O', '.', '.'],#6
        ['.', 'O', 'O', '.', '.', '.'],#7
        ['.', '.', '.', '.', '.', '.']]#8

"""
prints:
[0][0]
[1][0]
[2][0]
[3][0]
[4][0]
[5][0]
[6][0]
[7][0]
[8][0]
/newline
[0][1]
[1][1]
[2][1]
... and so forth
"""

for y in range(len(grid[0])):
    for x in range(len(grid)):
        print(grid[x][y],end="")
    print("")

"""
OUTPUT:
..OO.OO..
.OOOOOOO.
.OOOOOOO.
..OOOOO..
...OOO...
....O....
"""