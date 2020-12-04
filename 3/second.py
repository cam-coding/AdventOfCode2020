def DoTheThing(lines, right, down):
    width = len(lines[0]) - 1
    trees = 0
    x = 0
    for row, line in enumerate(lines):
        if row % down == 0:
            if line[x] == '#':
                trees+= 1
            x +=right
            x = x % width
    return trees

f = f = open('input.txt', 'r')
lines = f.readlines()
answer = [DoTheThing(lines, 1, 1),
            DoTheThing(lines, 3, 1),
            DoTheThing(lines, 5, 1),
            DoTheThing(lines, 7, 1),
            DoTheThing(lines, 1, 2)]
total = 1
for x in answer:
    total = total * x
print (total)