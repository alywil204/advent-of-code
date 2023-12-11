from itertools import combinations
import math

# Setup

with open("input.txt", "r") as input_file:
    present_dims = [[int(side) for side in line.split("x")]
                    for line in input_file]

# Part One


def wrapping_paper_area(present):
    edge_combos = combinations(range(0, 3), 2)
    sides = [present[combo[0]] * present[combo[1]] for combo in edge_combos]
    return sum(sides) * 2 + min(sides)


print('--Part One--')
print(sum(wrapping_paper_area(present) for present in present_dims))

# Part Two


def ribbon_length(present):
    return (sum(present) - max(present)) * 2 + math.prod(present)


print('--Part Two--')
print(sum(ribbon_length(present) for present in present_dims))
