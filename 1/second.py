def doTheThing(lines):
    singleDict = dict()
    pairDict = dict()
    for line in lines:
        one = int(line.strip())
        goal = 2020-one

        if (goal in pairDict):
            return one*pairDict[goal]

        singleDict[one] = one

        for item in singleDict:
            two = item + one
            if two < 2020:
                pairDict[two] = one * item
    return None

f = f = open('input.txt', 'r')
lines = f.readlines()
print(doTheThing(lines))