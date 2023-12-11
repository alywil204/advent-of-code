import re
from collections import defaultdict

# Setup


def bounding_box_for_match(line_number, match, grid_size):
    start = match.start()
    end = match.end()
    return [max(start-1, 0),
            max(line_number-1, 0),
            min(end, grid_size[0]-1),
            min(line_number+1, grid_size[1]-1)]


def number_bound_generator(grid):
    grid_size = (len(grid[0]), len(grid))
    return ((int(num_match.group()),
             bounding_box_for_match(ind, num_match, grid_size))
            for ind, line in enumerate(grid)
            for num_match in re.finditer('\d+', line))


with open("input.txt", "r") as input_file:
    grid = [line.strip() for line in input_file]

# Part One

part_number_sum = 0


def is_part_number(x1, y1, x2, y2):
    grid_slice = [str[x1:x2+1] for str in grid[y1:y2+1]]
    return any(re.search('[^0-9\.]', line) for line in grid_slice)


part_number_sum = sum(part_num for part_num, bounding_box
                      in number_bound_generator(grid)
                      if is_part_number(*bounding_box))

print('--Part One--')
print(part_number_sum)

# Part Two

gear_dict = defaultdict(lambda: [])

for part_num, (x1, y1, x2, y2) in number_bound_generator(grid):
    for y in range(y1, y2+1):
        for x in range(x1, x2+1):
            if grid[y][x] == "*":
                gear_dict[f'{x},{y}'].append(part_num)

gear_ratio_sum = sum(pn_list[0] * pn_list[1]
                     for pn_list in gear_dict.values()
                     if len(pn_list) == 2)

print('--Part Two--')
print(gear_ratio_sum)
