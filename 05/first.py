import math

def Tree(low, high, instruct, lowChar):
    dif = math.floor((high-low + 1)/2)
    if len(instruct) == 1:
        if instruct[0] == lowChar:
            return low
        return high
    if instruct[0] == lowChar:
        return Tree(low, low + dif-1, instruct[1:], lowChar)
    return Tree(low + dif, high, instruct[1:], lowChar)

f = open('input.txt', 'r')
lines = f.readlines()
max = 0
listOfIds = []

for line in lines:
    first = line[:7]
    second = line.strip()[7:]
    a = Tree(0, 127, first, 'F')
    b = Tree(0, 7, second, 'L')
    newMax = a*8 + b
    listOfIds.append(newMax)
    if newMax > max:
        max = newMax
print(max)

listOfIds.sort()
for i in range(len(listOfIds)):
    if i != len(listOfIds)-1:
        if listOfIds[i+1] != (listOfIds[i] + 1):
            print("missing: " + str(listOfIds[i] + 1))