from collections import deque
import math
import pprint
import copy

def get_lines():
    with open("input.txt") as f:
        return [line.strip() for line in f.readlines() if line.strip()]

LINES = get_lines()
Cycles = 3
DoubleCycles = Cycles*2
Width = len(LINES[0])
Height = len(LINES)

Galaxy = [[['.' for k in range(Height)] for j in range(Width)] for i in range(DoubleCycles)]
for i in range(Height):
    for j in range(Width):
        Galaxy[Cycles][i][j] = LINES[i][j]

#I guess the input wraps around on itself? okie

def doThing(Galaxy):
    print("hi")
    pprint.pprint(Galaxy)
    for i in range(Cycles):
        newGalaxy = copy.deepcopy(Galaxy)
        for z in range(Cycles -i, Cycles + i + 1):
            for y in range(Height):
                for x in range(Width):
                    count = countClose(z, y, x)
                    if (i == 0):
                        print(count)
                    if Galaxy[z][y][x] == '#' and (count != 2 and count != 3):
                        newGalaxy[z][y][x] = '.'
                    elif Galaxy[z][y][x] == '.' and count == 3:
                        newGalaxy[z][y][x] = '#'
        Galaxy = copy.deepcopy(newGalaxy)
        if (i == 0):
            print(Galaxy[Cycles])


def countClose(currentZ, currentY, currentX):
    count = 0
    z = currentZ -1
    while z in range (min(DoubleCycles, currentZ + 2)):
        y = currentY -1
        while y in range (min(Height, currentY + 2)):
            x = currentX -1
            while x in range (min(Width, currentX + 2)):
                if Galaxy[z][y][x] == '#':
                    count += 1
                x += 1
            y += 1
        z += 1
    return count

doThing(Galaxy)
finalCount = 0
for z in range(Cycles*2):
    for y in range(Height):
        for x in range(Width):
            if Galaxy[z][y][x] == '#':
                    finalCount += 1

print(finalCount)
#pprint.pprint(distance)