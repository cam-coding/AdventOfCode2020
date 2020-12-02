def DoTheThing(lines):
    myDict = dict()
    for line in lines:
        numb = int(line.strip())
        pair = 2020-numb
        if pair in myDict:
            return myDict[pair] * numb
        else:
            myDict[numb] = numb
    return None

f = f = open('input.txt', 'r')
lines = f.readlines()
print(DoTheThing(lines))