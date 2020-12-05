def Tree(highChar, string):
    binary = ''
    for i in range(len(string)):
        if string[i] == highChar:
            binary = binary + '1'
        else:
            binary = binary + '0'
    return int(binary, 2)

f = open('input.txt', 'r')
lines = f.readlines()
highest = 0
listOfIds = []
for line in lines:
    first = line[:7]
    second = line.strip()[7:]
    seatId = Tree('B', first)*8 + Tree('R', second)
    listOfIds.append(seatId)
    highest = max(seatId, highest)
print(highest)

listOfIds.sort()
for i in range(len(listOfIds)):
    if i != len(listOfIds)-1:
        if listOfIds[i+1] != (listOfIds[i] + 1):
            print("missing: " + str(listOfIds[i] + 1))