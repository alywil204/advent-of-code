from math import ceil, floor, sqrt

# Setup


def sqrt_disc(time, record):
    return sqrt(time**2 - 4*record)


def ways_to_beat(time, record):
    return \
        floor((-time + sqrt_disc(time, record)) / 2) \
        - ceil((-time - sqrt_disc(time, record)) / 2) \
        + 1


# Part One

with open("input.txt", "r") as input_file:
    time_list, record_list = ([
        int(x) for x in input_file.readline().split(':')[1].split()
    ] for _ in range(2))

product = 1
for time, record in zip(time_list, record_list):
    product *= ways_to_beat(time, record)

print('--Part One--')
print(product)

# Part Two

with open("input.txt", "r") as input_file:
    time, record = (
        int("".join(input_file.readline().split(':')[1].split()))
        for _ in range(2)
    )

print('--Part Two--')
print(ways_to_beat(time, record))
