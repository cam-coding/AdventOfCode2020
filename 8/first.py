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
            print(":hello")
            return value
        
        if commands[pc][0] == 'acc':
            value = value + commands[pc][1]
        elif commands[pc][0] == 'jmp':
            temp = pc + commands[pc][1]
            if temp in counter:
                return pc
            pc = temp -1
        pc += 1
    print(":hello")
    return value

commands = []
for line in get_lines():
    tokens = line.split()
    number = 0
    number = int(tokens[1][1:])
    if tokens[1][0] == '-':
        number = number * -1
    commands.append((tokens[0], number))

print(run_program(commands))