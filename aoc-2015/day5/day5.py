import re

# Setup

with open("input.txt", "r") as input_files:
    strings = input_files.readlines()

# Part One


nice_count = 0

pairs_regex = '|'.join([chr(idx) * 2 for idx in range(97, 123)])


def nice_string(str):
    return len(re.findall('[aeiou]', str)) >= 3 \
        and re.search(pairs_regex, str) \
        and not re.search('ab|cd|pq|xy', str)


print('--Part One--')
print(len([1 for str in strings if nice_string(str)]))

# Part Two


nice_count = 0


def substrings_of_length(str, length):
    return set(str[i:i+length] for i in range(len(str) - length + 1))


def check_pairs(str):
    pairs = substrings_of_length(str, 2)
    return any(len(re.findall(pair, str)) >= 2 for pair in pairs)


def check_triples(str):
    triples = substrings_of_length(str, 3)
    return any(triple[0] == triple[2] for triple in triples)


def nice_string(str):
    return check_pairs(str) and check_triples(str)


print('--Part Two--')
print(len([1 for str in strings if nice_string(str)]))
