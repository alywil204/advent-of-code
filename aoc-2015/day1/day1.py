# Setup

with open("input.txt", "r") as input_file:
    instructions = input_file.read()

# Part One

print("--Part One--")
print(instructions.count("(") - instructions.count(")"))

# Part Two

floor = 0
directions = {"(": 1, ")": -1}
for idx, char in enumerate(instructions):
    floor += directions[char]
    if floor < 0:
        break

print("--Part Two--")
print(idx + 1)
