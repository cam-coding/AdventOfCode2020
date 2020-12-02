file1 = open('c:\\Users\\Cam\\Documents\\code\\AdventOfCode2020\\1\\input.txt', 'r') 
Lines = file1.readlines() 
  
myDict = dict()
for line in Lines:
    numb = int(line.strip())
    pair = 2020-numb
    if (pair in myDict):
        print(myDict[pair] * numb)
    else:
        myDict[numb] = numb