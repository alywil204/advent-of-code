import re
import math

# Setup

with open("input.txt", "r") as input_file:
    lr = [0 if char == 'L' else 1 for char in input_file.readline().strip()]
    input_file.readline()

    network = {}
    for line in input_file:
        matches = re.match(r'(...) = \((...), (...)\)', line)
        network[matches[1]] = [matches[2], matches[3]]

# Part One

node = 'AAA'
steps = 0
while node != 'ZZZ':
    node = network[node][lr[steps % len(lr)]]
    steps += 1
   

print('--Part One--')
print(steps)

# Part Two

nodes = [key for key in network.keys() if key[-1] == 'A']
cycle_lengths = [0 for _ in nodes]
steps = 0
while not all(length > 0 for length in cycle_lengths):
    for i, node in enumerate(nodes):
        nodes[i] = network[node][lr[steps % len(lr)]]
        if nodes[i][-1] == 'Z':
            # I don't know why I can assume it will make it back here on a cycle but it works
            cycle_lengths[i] = steps + 1
    steps += 1

print('--Part Two--')
print(math.lcm(*cycle_lengths))
