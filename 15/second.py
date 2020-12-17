def get_lines():
    with open("input.txt") as f:
        return [line.strip() for line in f.readlines() if line.strip()]

dicts = {}

def doThing(max):
    counter = 1
    last = None
    inputNumbers = Lines[0].split(',')

    for num in inputNumbers:
        dicts[int(num)] = [counter, None]
        last = int(num)
        counter += 1

    while counter <= max:
        if dicts[last][1] == None:
            last = 0
        else:
            last = dicts[last][0] - dicts[last][1]
        AddToDict(last, counter)
        counter += 1
    return(last)

def AddToDict(last, counter):
    if last not in dicts:
        dicts[last] = [counter, None]
    else:
        dicts[last][1] = dicts[last][0]
        dicts[last][0] = counter

Lines = get_lines()
print(doThing(30000000))
