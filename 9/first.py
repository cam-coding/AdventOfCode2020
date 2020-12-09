def get_lines():
    with open("input.txt") as f:
        return [line.strip() for line in f.readlines()]

def works(last, number):
    half = number/2
    for item in last:
        if (item != half) and (number-item) in last:
            return True
    print(last)
    return False

def findWrong(lines, size):
    last = []
    for line in lines:
        number = int(line)
        if len(last) < size:
            last.append(number)
        else:
            if not works(last, number):
                return number
            last.pop(0)
            last.append(number)


lines = get_lines()
print(findWrong(lines, 25))