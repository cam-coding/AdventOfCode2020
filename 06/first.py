def get_lines():
    with open("input.txt") as f:
        return [line.strip() for line in f.readlines()]

yesList = []
total = 0
for line in get_lines():
    if len(line) == 0:
        total += len(yesList)
        yesList = []
    else:
        for char in line:
            if char not in yesList:
                yesList.append(char)
total += len(yesList)
print(total)