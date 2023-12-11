import re

## Setup

R = 0
G = 1
B = 2
colour_range = range(R, B+1)

colour_patterns = [f'(\d+) {colour}' for colour in ['red', 'green', 'blue']]
def colour_amount(round, colour_index):
    match = re.search(colour_patterns[colour_index], round)
    return 0 if match is None else int(match[1])

def rgb_for_round(round):
    return [colour_amount(round, colour) for colour in colour_range]

def game_generator(file):
    with open(file) as games:
        games = (game.split(':')[1].split(';') for game in games.readlines())
        return ([rgb_for_round(round) for round in game] for game in games)

def minimal_set(game):
    return [max(colour) for colour in list(zip(*game))]

minimal_sets = [minimal_set(game) for game in game_generator("input.txt")]

## Part One

def possible_game(min_set, totals):
    return all(min_set[colour] <= totals[colour] for colour in colour_range)

totals = (12, 13, 14)
possible_ids = (idx + 1 for idx, min_set 
                in enumerate(minimal_sets) 
                if possible_game(min_set, totals))

print('--Part One--')
print(sum(possible_ids))

## Part Two

powers = (s[R] * s[G] * s[B] for s in minimal_sets)

print('--Part Two--')
print(sum(powers))
