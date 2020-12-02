file1 = open('c:\\Users\\Cam\\Documents\\code\\AdventOfCode2020\\1\\input.txt', 'r') 
Lines = file1.readlines() 
  
singleDict = dict()
pairDict = dict()
for line in Lines:
    one = int(line.strip())
    goal = 2020-one

    if (goal in pairDict):
        print(one*pairDict[goal])

    singleDict[one] = one

    for item in singleDict:
        two = item + one
        if (two < 2020):
            pairDict[two] = one * item