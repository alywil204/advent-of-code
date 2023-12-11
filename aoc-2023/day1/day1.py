import re

## Setup

input_file = open("input.txt").readlines()

## Part One

digits = (re.sub('[^0-9]', '', line) for line in input_file)
calibration_values = (int(digit[0] + digit[-1]) for digit in digits)

print('--Part One--')
print(sum(calibration_values))

## Part Two

spellings = ["one", "two", "three", "four", "five", 
             "six", "seven", "eight", "nine"]
def str_2_int(str_rep):
    return int(str_rep) if len(str_rep) == 1 else spellings.index(str_rep) + 1

any_number_regex = '|'.join(spellings + [str(i) for i in range(0,10)])
reverse_regex = any_number_regex[::-1]
def calibration_value(line):
    # first number
    num1 = re.search(any_number_regex, line)[0]
    # second number
    num2 = re.search(reverse_regex, line[::-1])[0][::-1]
    return 10 * str_2_int(num1) + str_2_int(num2)

revised_calibration_values = (calibration_value(line) for line in input_file)

print('--Part Two--')
print(sum(revised_calibration_values))
