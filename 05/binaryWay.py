def Binary(highChar, lowChar, string):
    string = string.replace(highChar, '1').replace(lowChar, '0')
    return int(string, 2)

f = open('input.txt', 'r')
lines = f.readlines()
highest = 0
listOfIds = []
for line in lines:
    seatId = Binary('B', 'F', line[:7])*8 + Binary('R', 'L', line.strip()[7:])
    listOfIds.append(seatId)
    highest = max(seatId, highest)
print(highest)

listOfIds.sort()
for i in range(len(listOfIds)):
    if i != len(listOfIds)-1:
        if listOfIds[i+1] != (listOfIds[i] + 1):
            print("missing: " + str(listOfIds[i] + 1))