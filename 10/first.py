def get_lines():
    with open("input.txt") as f:
        return [int(line.strip()) for line in f.readlines()]

adapters = get_lines()
adapters.append(0)
adapters.sort()
for i in range(len(adapters)-2):
    myList = [0]*4
    for j in range(i, i+3):
        dif = adapters[j] - adapters[i]
        if dif < 4:
            myList[dif] = adapters[j]
total = [0]*4
total[3] = 1
for i in range(len(adapters)-1):
    total[adapters[i+1] - adapters[i]] += 1

print(total[1]*total[3])