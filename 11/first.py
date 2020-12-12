
def get_lines():
    with open("input.txt") as f:
        return [line.strip() for line in f.readlines()]

def doLogic(Matrix):
    newMatrix = [l[:] for l in Matrix]
    for y in range(len(Matrix)):
        for x in range(len(Matrix[0])):
            count = occ(y, x, Matrix)
            if Matrix[y][x] == 1 and count == 0:
                newMatrix[y][x] = 2
            elif Matrix[y][x] == 2 and count > 3:
                newMatrix[y][x] = 1
    return newMatrix

def occ(y, x, Matrix):
    count = 0
    for i in range(max(y-1, 0), min(y+2, len(Matrix))):
        for j in range(max(x-1, 0), min(x+2, len(Matrix[0]))):
            if not (i == y and j == x):
                if Matrix[i][j] == 2:
                    count += 1
    return count


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


print(total)
print(i)