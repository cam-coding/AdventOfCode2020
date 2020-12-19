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
realWidth = Width + DoubleCycles
Height = len(LINES)
realHeight = Height + DoubleCycles

Galaxy = [[['.' for k in range(realHeight)] for j in range(realWidth)] for i in range(DoubleCycles)]
for i in range(Height):
    for j in range(Width):
        Galaxy[Cycles][Cycles + i][Cycles + j] = LINES[i][j]
#I guess the input wraps around on itself? okie
for j in range(realHeight):
    print(Galaxy[Cycles][j])

def doThing(Galaxy):
    for i in range(Cycles):
        newGalaxy = copy.deepcopy(Galaxy)
        for z in range(Cycles -i, Cycles + i + 1):
            for y in range(realHeight):
                for x in range(realWidth):
                    count = countClose(z, y, x)
                    if (i == 0):
                        if count > 1 and count < 4:
                            print("y: {} x: {} count:{} current: {}".format(y, x, count, Galaxy[z][y][x]))
                    if Galaxy[z][y][x] == '#' and (count != 2 and count != 3):
                        newGalaxy[z][y][x] = '.'
                    elif Galaxy[z][y][x] == '.' and count == 3:
                        newGalaxy[z][y][x] = '#'
        Galaxy = copy.deepcopy(newGalaxy)
        if (i == 0):
            for j in range(realHeight):
                print(newGalaxy[Cycles][j])


def countClose(currentZ, currentY, currentX):
    count = 0
    z = currentZ -1
    if (currentZ == Cycles and currentY == 5 and currentX == 4):
        print("Hello")
        print(Galaxy[currentZ][currentY][currentX])
    while z in range (min(DoubleCycles, currentZ + 2)):
        y = currentY -1
        while y in range (min(realHeight, currentY + 2)):
            x = currentX -1
            while x in range (min(realWidth, currentX + 2)):
                if (currentZ == Cycles and currentY == 5 and currentX == 4):
                    if Galaxy[z][y][x] == '#':
                        print("z: {} y: {} x: {} ".format(z, y, x))
                if Galaxy[z][y][x] == '#':
                    count += 1
                x += 1
            y += 1
        z += 1
    return count

doThing(Galaxy)
finalCount = 0
for z in range(DoubleCycles):
    for y in range(realHeight):
        for x in range(realWidth):
            if Galaxy[z][y][x] == '#':
                    finalCount += 1

print(finalCount)
#pprint.pprint(distance)