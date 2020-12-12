def get_lines():
    with open("input.txt") as f:
        return [line.strip() for line in f.readlines()]

Matrix = [list(line) for line in get_lines()]
WIDTH = len(Matrix[0])
HEIGHT = len(Matrix)    

def doLogic():
    newMatrix = [l[:] for l in Matrix]
    for y in range(HEIGHT):
        for x in range(WIDTH):
            count =  checkHor(y, x) + checkVert(y, x) + checkDiagonal(y, x)
            if Matrix[y][x] == 'L' and count == 0:
                newMatrix[y][x] = '#'
            elif Matrix[y][x] == '#' and count > 4:
                newMatrix[y][x] = 'L'
    return newMatrix

def checkHor(y, x):
    count = 0
    i = x-1
    while i in range(WIDTH):
        if Matrix[y][i] == '#':
            count += 1
            break
        elif Matrix[y][i] == 'L':
            break
        i -= 1
    i = x + 1
    while i in range(WIDTH):
        if Matrix[y][i] == '#':
            count += 1
            break
        elif Matrix[y][i] == 'L':
            break
        i += 1
    return count

def checkVert(y, x):
    count = 0
    i = y-1
    while i in range(HEIGHT):
        if Matrix[i][x] == '#':
            count += 1
            break
        elif Matrix[i][x] == 'L':
            break
        i -= 1
    i = y + 1
    while i in range(HEIGHT):
        if Matrix[i][x] == '#':
            count += 1
            break
        elif Matrix[i][x] == 'L':
            break
        i += 1
    return count

def checkDiagonal(y, x):
    a = [-1, 1]
    b = [-1, 1]
    count = 0

    for i in range(2):
        for j in range(2):
            count += runDiagonal(y, x, a[i], b[j])

    return count

def runDiagonal(y, x, a, b):
    i = y + a
    j = x + b

    while i in range(HEIGHT) and j in range(WIDTH):
        if Matrix[i][j] == '#':
            return 1
        elif Matrix[i][j] == 'L':
            return 0
        j += b
        i += a
    return 0

lastState = None
i = 0
while (lastState != Matrix):
    i += 1
    lastState = Matrix[:]
    Matrix = doLogic()

total = sum([sum([1 if s == '#' else 0 for s in row]) for row in Matrix])
print(total)