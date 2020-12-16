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

    myStuff = {}
    listOfPrimes = []
    for i in range(len(things)):
        if things[i] != 'x':
            listOfPrimes.append(int(things[i])
            myStuff[int(things[i])] = i

    LCM = math.lcm(listOfPrimes.__reduce__)
    print(myStuff)
    #Chinese Remainder theorem my guy https://www.reddit.com/r/adventofcode/comments/kcb3bb/2020_day_13_part_2_can_anyone_tell_my_why_this/
    return "hello"

print(logic())