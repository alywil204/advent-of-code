# Setup

DEST_START = 0
SOURCE_START = 1
RANGE_LEN = 2

with open("input.txt", "r") as input_file:
    lines = input_file.readlines()

    seeds = [int(seed) for seed in lines[0].split(':')[1].split()]
    maps = []
    for line in lines[2:]:
        if 'map' in line:
            maps.append([])
            maps_index = len(maps) - 1
        else:
            line = line.split()
            if len(line) != 0:
                maps[maps_index].append([int(x) for x in line])

# Part One

seed_map = {seed: seed for seed in seeds}

for map in maps:
    for seed in seeds:
        for conversion in map:
            if seed_map[seed] in range(conversion[SOURCE_START], conversion[SOURCE_START] + conversion[RANGE_LEN]):
                seed_map[seed] = seed_map[seed] - conversion[SOURCE_START] + \
                    conversion[DEST_START]
                break

print('--Part One--')
print(min(seed_map.values()))

# Part Two


def range_end(range):
    return range[0] + range[1] - 1


def cut_range(range1, range2):
    # cut range 1 using range 2
    ranges = [[range1[0], range1[1]]]
    range2end = range_end(range2)
    range1end = range_end(range1)
    if range2[0] > range1[0] and range2[0] <= range_end(range1):
        ranges[0][1] = range2[0] - range1[0]
        ranges.append([range2[0], range1end - range2[0] + 1])
    if range2end < range1end and range2end >= range1[0]:
        ranges[-1][1] = range2end - ranges[-1][0] + 1
        ranges.append([range2end + 1, range1end - range2end])
    return ranges


def add_range_to_maps(range, conversion_value, seeds, ranges):
    seeds[range[0]] = conversion_value
    ranges[range[0]] = range[1]


seed_ranges = [[seeds[i], seeds[i+1]] for i in range(0, len(seeds), 2)]
seed_map = {seed[0]: seed[0] for seed in seed_ranges}
range_map = {seed[0]: seed[1] for seed in seed_ranges}

for map in maps:
    ranges_to_check = list(range_map.items())
    r = 0
    while r < len(ranges_to_check):
        for conversion in map:
            range_to_check = ranges_to_check[r]
            mapped_range = [seed_map[range_to_check[0]], range_to_check[1]]

            if mapped_range[0] >= conversion[1] and range_end(mapped_range) <= range_end(conversion[1:]):
                seed_map[range_to_check[0]] = mapped_range[0] - conversion[SOURCE_START] + \
                    conversion[DEST_START]
                break

            cut_ranges = cut_range(mapped_range, conversion[1:])
            # map onto seed_map ranges:

            if len(cut_ranges) == 1:
                continue

            range_to_update = 1 if conversion[1] == cut_ranges[1][0] else 0

            cut_ranges = [
                [cut_range[0] + range_to_check[0] - mapped_range[0], cut_range[1]] for cut_range in cut_ranges]

            add_range_to_maps(
                cut_ranges[range_to_update], cut_ranges[range_to_update][0] - cut_ranges[0][0] + mapped_range[0] - conversion[SOURCE_START] +
                conversion[DEST_START], seed_map, range_map)
            for ind, range in enumerate(cut_ranges):
                if ind != range_to_update:
                    add_range_to_maps(
                        range, cut_ranges[ind][0] - cut_ranges[0][0] + mapped_range[0], seed_map, range_map)
                    ranges_to_check.append(range)
            break
        r += 1

print('--Part Two--')
print(min(seed_map.values()))
