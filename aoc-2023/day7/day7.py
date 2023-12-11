from collections import Counter
from functools import cmp_to_key

# Setup

with open("input.txt", "r") as input_file:
   hands = [[x, int(y)] for x, y in [line.split() for line in input_file]]

def hand_counts_to_strength(hand_counts):
    match sorted(hand_counts):
        case [5]:
            return 6
        case [1, 4]:
            return 5
        case [2, 3]:
            return 4
        case [1, 1, 3]:
            return 3
        case [1, 2, 2]:
            return 2
        case [1, 1, 1, 2]:
            return 1
        case [1, 1, 1, 1, 1]:
            return 0

def compare_hands(card_strength, hand_type_strength):
    def compare_func(hand1, hand2):
        hand_type1 = hand_type_strength(hand1[0])
        hand_type2 = hand_type_strength(hand2[0])
        if hand_type1 != hand_type2:
            return hand_type1 - hand_type2
        for h1, h2 in zip(hand1[0], hand2[0]):
            if h1 != h2:
                return card_strength.index(h1) - card_strength.index(h2)
        return 0
    return compare_func

def sum_winnings(hands, card_strength, hand_type_strength):
    sorted_hands = sorted(hands, key=cmp_to_key(compare_hands(card_strength, hand_type_strength)))

    return sum(rank * hand[1] for rank, hand in enumerate(sorted_hands, 1))

# Part One

card_strength = [*(str(i) for i in range(2,10)), 'T', 'J', 'Q', 'K', 'A']

def hand_type_strength(hand):
    return hand_counts_to_strength(Counter(hand).values())


print('--Part One--')
print(sum_winnings(hands, card_strength, hand_type_strength))

# Part Two

card_strength_jokers = ['J', *(str(i) for i in range(2,10)), 'T', 'Q', 'K', 'A']

def hand_type_strength_jokers(hand):
    hand_counts = Counter(hand)
    joker_count = hand_counts['J']
    del hand_counts['J']
    sorted_counts = sorted(hand_counts.values()) or [0]
    sorted_counts[-1] += joker_count
    
    return hand_counts_to_strength(sorted_counts)

print('--Part Two--')
print(sum_winnings(hands, card_strength_jokers, hand_type_strength_jokers))
