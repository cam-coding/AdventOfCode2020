def get_lines():
    with open("input.txt") as f:
        return [line.strip() for line in f.readlines()]

def run_program(commands):
    pc=0
    counter = []
    value = 0
    while pc < len(commands):
        if pc not in counter:
            counter.append(pc)
        else:
            return value
        if commands[pc][0] == 'acc':
            value = value + commands[pc][1]
        elif commands[pc][0] == 'jmp':
            pc = pc + commands[pc][1] - 1
        pc += 1
    return value

commands = [line.split() for line in get_lines()]
commands = [(com, int(num)) for com, num in commands]
print(run_program(commands))