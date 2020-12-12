import copy

def get_lines():
    with open("input.txt") as f:
        return [line.strip() for line in f.readlines() if line.strip()]

def FindBadLines(commands):
    for i in range(len(commands)):
        if commands[i][0] == "acc":
            continue
        fresh = copy.deepcopy(commands)
        fresh[i] = ("jmp", fresh[i][1]) if commands[i][0] == "nop" else ("nop", fresh[i][1])
        result = RunProgram(fresh)
        if result[0]:
            return result[1]
    return None

def RunProgram(fresh):
    pc=0
    counter = []
    value = 0
    while pc < len(fresh):
        if pc not in counter:
            counter.append(pc)
        else:
            return False, value
        if fresh[pc][0] == 'acc':
            value = value + fresh[pc][1]
        elif fresh[pc][0] == 'jmp':
            pc = pc + fresh[pc][1] - 1
        pc += 1

    return True, value

commands = [line.split() for line in get_lines()]
commands = [(com, int(num)) for com, num in commands]
print(FindBadLines(commands))