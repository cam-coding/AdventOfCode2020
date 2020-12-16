from collections import deque
import math

def get_lines():
    with open("input.txt") as f:
        return [line.strip() for line in f.readlines() if line.strip()]

dicts = {}

def doThing():
    counter = 1
    last = None
    inputNumbers = Lines[0].split(',')

    for num in inputNumbers:
        dicts[int(num)] = [counter, None]
        last = int(num)
        counter += 1

    while counter < 30000001:
        if dicts[last][1] == None:
            last = 0
        else:
            last = dicts[last][0] - dicts[last][1]
        
        AddToDict(last, counter)

        if (counter < 2):
            print("counter: {} last: {}".format(counter, last))
        counter += 1

        if counter % 100000 == 0:
            print(counter)
    return(last)

def AddToDict(last, counter):
    if last not in dicts:
        dicts[last] = [counter, None]
    else:
        dicts[last] = [counter, dicts[last][0]]

Lines = get_lines()
WIDTH = len(Lines[0])
Height = len(Lines)



print(doThing())