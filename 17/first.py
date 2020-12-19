from collections import deque
import math
import pprint
import copy
import numpy as np

def get_lines():
    with open("input.txt") as f:
        return [line.strip() for line in f.readlines() if line.strip()]

global space 


LINES = get_lines()
Cycles = 6
BufferCycles = Cycles + 1
DoubleCycles = BufferCycles*2
Width = len(LINES[0])
maxWidth = Width + DoubleCycles
Height = len(LINES)
maxHeight = Height + DoubleCycles

space = np.full((DoubleCycles + 1, maxHeight, maxWidth), '.')
for i in range(Height):
    for j in range(Width):
        space[BufferCycles][BufferCycles + i][BufferCycles + j] = LINES[i][j]

def county(currentZ, currentY, currentX):
    count = 0
    for z in range(currentZ - 1, currentZ + 2):
        for y in range(currentY - 1, currentY + 2):
            for x in range(currentX - 1, currentX + 2):
                if space[z][y][x] == '#':
                    count += 1

    if space[currentZ][currentY][currentX] == '#':
        count -= 1
    return count

def dumbMethod():
    global space
    for i in range(Cycles):
        newSpace = copy.deepcopy(space)
        print("z {} to {}".format(BufferCycles - i - 1, BufferCycles + i + 2))
        print("y {} to {}".format(BufferCycles - i - 1, BufferCycles + Height + i + 1))
        print("x {} to {}".format(BufferCycles - i - 1, BufferCycles + Width + i + 1))
        for z in range(BufferCycles - i - 1, BufferCycles + i + 2):
            for y in range(BufferCycles - i - 1, BufferCycles + Height + i + 1):
                for x in range(BufferCycles - i - 1, BufferCycles + Width + i + 1):
                    count = county(z, y, x)
                    if space[z][y][x] == '#' and (count != 2 and count != 3):
                        newSpace[z][y][x] = '.'
                    elif space[z][y][x] == '.' and count == 3:
                        newSpace[z][y][x] = '#'
        print(newSpace[BufferCycles])
        space = copy.deepcopy(newSpace)
        print("hi")
        print(space[BufferCycles])

    total = 0
    print(maxWidth)
    print(maxHeight)
    for i in range(DoubleCycles + 1):
        for j in range(maxHeight):
            for k in range(maxWidth):
                if space[i][j][k] == '#':
                    total += 1
    return total

print(dumbMethod())
#print(countClose(BufferCycles, BufferCycles+1, BufferCycles+1))