def get_lines():
    with open("input.txt") as f:
        return [int(line.strip()) for line in f.readlines()]

def works(last, number):
    for item in last:
        if (item != number/2) and (number-item) in last:
            return True
    return False

def findWrong(lines, size):
    last = []
    for number in lines:
        if len(last) < size:
            last.append(number)
        else:
            if not works(last, number):
                return number
            last.pop(0)
            last.append(number)

def findWeakness(inputNumbers, number):
    for i in range(len(inputNumbers)-1, 0, -1):
        total = 0
        j = i
        tempList = []
        while total < number:
            total = total + inputNumbers[j]
            tempList.append(inputNumbers[j])

            if total == number:
                print(min(tempList) + max(tempList))
                return
            j -= 1

lines = get_lines()
findWeakness(lines, findWrong(lines, 25))