from collections import deque

def get_lines():
    with open("input.txt") as f:
        return [line.strip() for line in f.readlines()]

lines = get_lines()

def doThing():
    ship_east = 0
    ship_north = 0
    directions = ['E', 'S', 'W', 'N']
    waypoint = deque([10, 0, 0, 1])

    for line in lines:
        val = int(line[1:])
        code = line[0]
        if code == 'F':
            for i in range(val):
                ship_east += waypoint[0] - waypoint[2]
                ship_north += waypoint[3] - waypoint[1]
        elif code in directions:
            waypoint[directions.index(code)] += val
        elif code == 'R' or code == 'L':
            waypoint = rotateWaypoint(waypoint, val, code)
    return abs(ship_east) + abs(ship_north)

def rotateWaypoint(waypoint, val, turn):
    rotater = int(val / 90)
    if turn == 'L':
        rotater = rotater *-1
    waypoint.rotate(rotater)
    return waypoint

print(doThing())