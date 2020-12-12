from collections import deque

def get_lines():
    with open("input.txt") as f:
        return [line.strip() for line in f.readlines()]

lines = get_lines()

def doThing():
    direction = ['E', 'S', 'W', 'N']
    facing = deque(['E', 'S', 'W', 'N'])
    increases = [0, 0, 0, 0]

    for line in lines:
        val = int(line[1:])
        code = line[0]
        if code == 'F':
            increases[direction.index(facing[0])] += val
        elif line[0] == 'R' or line[0] == 'L':
            facing = rotateShip(facing, val, line[0])
        else:
            increases[direction.index(code)] += val
    return abs(increases[0] - increases[2]) + abs(increases[1] - increases[3])

def rotateShip(facing, val, turn):
    rotater = int(val / 90)
    if turn == 'R':
        rotater = rotater *-1
    facing.rotate(rotater)
    return facing

print(doThing())