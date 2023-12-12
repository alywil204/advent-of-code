from itertools import pairwise

# Setup

with open("input.txt", "r") as input_file:
    histories = [[int(x) for x in line.split()] for line in input_file]

def extrapolate_history(hist, backwards=False):
    if not any(hist):
        return 0
    pairwise_sums = list(y - x for x, y in pairwise(hist))
    return hist[(-1, 0)[backwards]] \
        + extrapolate_history(pairwise_sums, backwards) * ((1, -1)[backwards])

# Part One

print('--Part One--')
print(sum(extrapolate_history(hist) for hist in histories))

# Part Two

print('--Part Two--')
print(sum(extrapolate_history(hist, True) for hist in histories))
