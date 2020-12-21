f = f = open('input.txt', 'r')
lines = f.readlines()
passwordCount = 0

for line in lines:
    tokens = line.split()
    ranged = tokens[0].rsplit('-', 1)
    char = tokens[1][0]
    pos1 = int(ranged[0]) - 1
    pos2 = int(ranged[1]) - 1
    string = tokens[2]
    if (string[pos1] == char) ^ (string[pos2] == char):
        passwordCount += 1
print(passwordCount)