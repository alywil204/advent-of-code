# Setup

X = 0
Y = 1

with open("input.txt", "r") as input_file:
    directions = input_file.read()


def add_to_house_dict(house_dict, pos):
    house_dict[f'{pos[X]},{pos[Y]}'] = True


def next_location(dir, pos):
    x, y = pos
    match dir:
        case "^":
            return [x, y-1]
        case "v":
            return [x, y+1]
        case ">":
            return [x+1, y]
        case "<":
            return [x-1, y]

# Part One


pos = [0, 0]
house_dict = {}

add_to_house_dict(house_dict, pos)

for dir in directions:
    pos = next_location(dir, pos)
    add_to_house_dict(house_dict, pos)

print('--Part One--')
print(len(house_dict))

# Part Two


pos = [[0, 0], [0, 0]]
house_dict = {}

add_to_house_dict(house_dict, pos[0])

for idx, dir in enumerate(directions):
    person = idx % 2
    pos[person] = next_location(dir, pos[person])
    add_to_house_dict(house_dict, pos[person])

print('--Part Two--')
print(len(house_dict))
