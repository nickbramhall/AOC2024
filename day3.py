import re

input_file = 'input/day3.txt'

def sum_multiplier(all_expressions):
    sum=0
    for result in all_expressions:
        numbers = re.search("[\d]{1,3},[\d]{1,3}", result)
        # print(numbers.group())
        first,second = numbers.group().split(",")
        multiplier = int(first) * int(second)
        # print(multiplier)
        sum = sum + multiplier
    return sum

# Read in all the data and strip out any whitespace at the end of lines
all_lines = [line.rstrip('\n') for line in open(input_file)]

all_input=''
for line in all_lines:
    all_input=all_input+line

all_expressions = re.findall("mul\([\d]{1,3},[\d]{1,3}\)", all_input)
sum=sum_multiplier(all_expressions)

print(f'Part 1: {sum}')

# Part 2

update = all_input
i=True

while i is True:
    dont = update.find("don't()")
    if dont == -1:
        break
    next_do = update.find("do()",dont)
    end = len(update)
    update = update[0:dont] + update[next_do:end]

all_expressions = re.findall("mul\([\d]{1,3},[\d]{1,3}\)", update)
sum=sum_multiplier(all_expressions)

print(f'Part 2: {sum}')