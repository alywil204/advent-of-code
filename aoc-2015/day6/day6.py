import re
import time

# Setup

STATE = 0
X1 = 1
Y1 = 2
X2 = 3
Y2 = 4


def parse_instruction(instruction):
    parser = re.compile(
        "^(turn off|turn on|toggle) (\d+),(\d+) through (\d+),(\d+)")
    match = parser.match(instruction)
    return [match[1]] + [
        int(match[i]) for i in range(2, 6)
    ]


instructions = [parse_instruction(line)
                for line in open("input.txt", "r").readlines()]

# Part One


grid = [[False for _ in range(1000)] for _ in range(1000)]

instruction_states = {"toggle": None, "turn off": False, "turn on": True}

t0 = time.time()
for instruction in instructions:
    instruction_state = instruction_states[instruction[STATE]]
    for x in range(instruction[X1], instruction[X2] + 1):
        y1, y2 = instruction[Y1], instruction[Y2] + 1
        if instruction_state is None:
            grid[x][y1:y2] = [not state for state in grid[x][y1:y2]]
        else:
            grid[x][y1:y2] = [instruction_state for _ in range(y1, y2)]
t1 = time.time()

print('--Part One--')
print(f'Time: {t1-t0}')
print(sum([sum(row) for row in grid]))

# Part Two


grid = [[0 for _ in range(1000)] for _ in range(1000)]

instruction_values = {"toggle": 2, "turn off": -1, "turn on": 1}

t0 = time.time()
for instruction in instructions:
    value = instruction_values[instruction[STATE]]
    for x in range(instruction[X1], instruction[X2] + 1):
        y1, y2 = instruction[Y1], instruction[Y2] + 1
        grid[x][y1:y2] = [max(0, state + value) for state in grid[x][y1:y2]]
t1 = time.time()

print('--Part Two--')
print(f'Time: {t1-t0}')
print(sum([sum(row) for row in grid]))
