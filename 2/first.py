def passwordAccepted(ranged, char, string):
    total = 0
    for x in string:
        if x == char:
            total += 1
    return int(ranged[0]) <= total and total <= int(ranged[1])

f = f = open('input.txt', 'r')
lines = f.readlines()
passwordCount = 0

for line in lines:
    tokens = line.split()
    ranged = tokens[0].rsplit('-', 1)
    char = tokens[1][0]
    if passwordAccepted(ranged, char, tokens[2]):
        passwordCount += 1


print(passwordCount)