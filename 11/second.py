
def get_lines():
    with open("input.txt") as f:
        return [line.strip() for line in f.readlines()]

def doLogic(Matrix):
    newMatrix = [l[:] for l in Matrix]
    for y in range(len(Matrix)):
        for x in range(len(Matrix[0])):
            check1 = checkHor(y, x, Matrix)
            check2 = checkVert(y, x, Matrix)
            check3 = blah(y, x, Matrix)
            count =  check1 + check2 + check3
            if Matrix[y][x] == 1 and count == 0:
                newMatrix[y][x] = 2
            elif Matrix[y][x] == 2 and count > 4:
                newMatrix[y][x] = 1
    return newMatrix

def checkHor(y, x, Matrix):
    count1 = None
    count2 = None
    i = x-1
    while i > -1 and count1 == None:
        if Matrix[y][i] == 2:
            count1 = 1 
        elif Matrix[y][i] == 1:
            count1 = 0
        i -= 1
    i = x + 1
    while i < len(Matrix[0]) and count2 == None:
        if Matrix[y][i] == 2:
            count2 = 1 
        elif Matrix[y][i] == 1:
            count2 = 0
        i += 1
    if count1 == None:
        count1 = 0
    if count2 == None:
        count2 = 0
    return count1+count2

def checkVert(y, x, Matrix):
    count1 = None
    count2 = None
    i = y-1
    while i > -1 and count1 == None:
        if Matrix[i][x] == 2:
            count1 = 1 
        elif Matrix[i][x] == 1:
            count1 = 0
        i -= 1
    i = y + 1
    while i < len(Matrix) and count2 == None:
        if Matrix[i][x] == 2:
            count2 = 1 
        elif Matrix[i][x] == 1:
            count2 = 0
        i += 1
    if count1 == None:
        count1 = 0
    if count2 == None:
        count2 = 0
    return count1+count2

def blah(y, x, Matrix):
    a = [-1, 1]
    b = [-1, 1]
    count = 0

    for i in range(2):
        for j in range(2):
            count += checkDiagonal(y, x, Matrix, a[i], b[j])

    return count

def checkDiagonal(y, x, Matrix, a, b):
    i = y + a
    j = x + b

    while (i > -1 and i < len(Matrix)) and (j > -1 and j < len(Matrix[0])):
        if Matrix[i][j] == 2:
            return 1
        elif Matrix[i][j] == 1:
            return 0
        j += b
        i += a
    return 0


lines = get_lines()

Matrix = [[0 for x in range(len(lines[0]))] for y in range(len(lines))]
lastState = None

for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] == 'L':
            Matrix[y][x] = 1

i = 0
while (lastState != Matrix):
    i += 1
    lastState = Matrix[:]
    Matrix = doLogic(Matrix)

total = 0
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if Matrix[y][x] == 2:
            total += 1


for item in Matrix:
    print(item)
print(total)
print(i)