from functools import reduce

def get_lines():
    with open("input.txt") as f:
        return [int(line.strip()) for line in f.readlines()]

adapters = get_lines()
adapters.append(0)
adapters.sort()
length = len(adapters)
truthy = [False]*length
truthy[0] = True
myList = []

for i in range(1, length-1):
    if adapters[i+1] - adapters[i] == 3 or adapters[i] - adapters[i-1] == 3:
        truthy[i] = True

for i in range(0, length-2):
    if truthy[i]:
        j = i + 1
        while j < len(truthy)-1 and not truthy[j]:
            j += 1
        
        temp = pow(2, j - i - 1)
        if adapters[j] - adapters[i] > 3:
            temp -= 1
        myList.append(temp)

print(reduce(lambda x, y: x*y, myList))