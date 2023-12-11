# Setup

with open("input.txt", "r") as input_file:
    cards = [line.split(':')[1].split('|') for line in input_file]
    cards = [[num_set.split() for num_set in line] for line in cards]

# Part One


match_counts = [len(set(winning).intersection(set(yours)))
                for winning, yours in cards]
score = sum(2 ** (match_count - 1)
            for match_count in match_counts if match_count > 0)

print('--Part One--')
print(score)

# Part Two

card_counts = [1] * len(match_counts)
for i, match_count in enumerate(match_counts):
    start = i + 1
    end = start + match_count
    card_counts[start:end] = [x + card_counts[i]
                              for x in card_counts[start:end]]

print('--Part Two--')
print(sum(card_counts))
