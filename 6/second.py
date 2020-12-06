def get_lines():
    with open("input.txt") as f:
        return [line.strip() for line in f.readlines()]

yesDict = {}
total = 0
groupSize = 0
for line in get_lines():
    if len(line) == 0:
        total += sum(value == groupSize for value in yesDict.values())
        groupSize = 0
        yesDict = {}
    else:
        groupSize += 1
        for char in line:
            if char not in yesDict:
                yesDict[char] = 1
            else:
                yesDict[char] = yesDict[char] + 1
total += sum(value == groupSize for value in yesDict.values())
print(total)