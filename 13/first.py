from collections import deque
import math

def get_lines():
    with open("input.txt") as f:
        return [line.strip() for line in f.readlines() if line.strip()]

LINES = get_lines()
Leaving = int(LINES[0])
WIDTH = len(LINES[0])
Height = len(LINES)

def logic():
    times = []
    things = LINES[1].split(",")
    for item in things:
        if item != 'x':
            times.append(int(item))

    difs = {}
    for item in times:
        val = Leaving//item
        if item * val == Leaving:
            return (item * 0)
        else:
            difs[item] = ((val+1) * item) - Leaving
    
    lowest = min(difs, key=difs.get)
    return (lowest * difs[lowest])

print(logic())