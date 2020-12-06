def get_lines():
    with open("input.txt") as f:
        return [line.strip() for line in f.readlines()]

myString = ""
fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
total = 0
for line in get_lines():
    if len(line) == 0:
        total += all(ele in myString for ele in fields)
        myString = ""
    else:
        myString = myString + line
print(total)