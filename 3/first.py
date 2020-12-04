def DoTheThing(lines):
    width = len(lines[0]) - 1
    trees = 0
    x = 0
    for line in lines:
        if line[x] == '#':
            trees+= 1
        x +=3
        x = x % width
    return trees

f = f = open('input.txt', 'r')
lines = f.readlines()
print(DoTheThing(lines))