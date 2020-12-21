def get_lines():
    with open("input.txt") as f:
        return [line.strip() for line in f.readlines() if line.strip()]

Lines = get_lines()
Width = len(Lines[0])
Height = len(Lines)

def mathable(stack):
    return len(stack) > 2 and isinstance(stack[len(stack) - 3], int) and (stack[len(stack) - 2] == "+" or stack[len(stack) - 2] == "*") and isinstance(stack[len(stack) - 1], int)

total = 0
for line in Lines:
    stack = []
    for char in line:
        if char.isspace():
            continue
        print(stack)
        if char == "(" or char == "*" or char == "+":
            stack.append(char)
        elif char.isnumeric():
            if len(stack) == 0:
                stack.append(int(char))
            elif stack[len(stack) - 1] == "*":
                stack.pop()
                num = stack.pop()
                stack.append(num * int(char))
            elif stack[len(stack) - 1] == "+":
                stack.pop()
                num = stack.pop()
                stack.append(num + int(char))
            else:
                stack.append(int(char))
        elif char == ")":
            while stack[len(stack) - 2] != "(" or not isinstance(stack[len(stack) - 1], int):
                if stack[len(stack) - 2] == "*":
                    num1 = stack.pop()
                    stack.pop()
                    num2 = stack.pop()
                    stack.append(num1 * num2)
                elif stack[len(stack) - 2] == "+":
                    num1 = stack.pop()
                    stack.pop()
                    num2 = stack.pop()
                    stack.append(num1 + num2)

            temp = stack.pop()
            stack.pop()
            stack.append(temp)
        
        while (mathable(stack)):
            if stack[len(stack) - 2] == "*":
                num1 = stack.pop()
                stack.pop()
                num2 = stack.pop()
                stack.append(num1 * num2)
            elif stack[len(stack) - 2] == "+":
                num1 = stack.pop()
                stack.pop()
                num2 = stack.pop()
                stack.append(num1 + num2)
    stack.reverse()
    while len(stack) != 1:
        if stack[len(stack) - 2] == "*":
            num1 = stack.pop()
            stack.pop()
            num2 = stack.pop()
            stack.append(num1 * num2)
        elif stack[len(stack) - 2] == "+":
            num1 = stack.pop()
            stack.pop()
            num2 = stack.pop()
            stack.append(num1 + num2)
    print(stack)
    total += stack[0]

print(total)