import re

input_file = 'input/day3-sample.txt'

# Read in all the data and strip out any whitespace at the end of lines
all_lines = [line.rstrip('\n') for line in open(input_file)]

# print(all_lines)

sum=0

for line in all_lines:
    all_expressions = re.findall("mul\([\d]{1,3},[\d]{1,3}\)", line)

    print(all_expressions)

    # sum = 0

    for result in all_expressions:
        numbers = re.search("[\d]{1,3},[\d]{1,3}", result)
        # print(numbers.group())
        first,second = numbers.group().split(",")
        multiplier = int(first) * int(second)
        # print(multiplier)
        sum = sum + multiplier

print(sum)

# Part 2

# dont = all_lines[0].find("don't()")

donts = []
dos = []

for match in re.finditer("don't\(\)", all_lines[0]):
    print(match.span(), match.group())
    donts.append(match.span()[1])

for match in re.finditer("do\(\)", all_lines[0]):
    print(match.span(), match.group())
    dos.append(match.span()[1])

    

# dont = re.split("don't()", all_lines[0])

print(donts)
print(dos)

slices = []

for position_do in dos:
    for position_dont in donts:
        if position_dont > position_do:
            slices.append(position_do)
            slices.append(position_dont)
            break

print(slices)

final=''

for i in range(0,len(slices)-1,2):
    print(f'Slicing {slices[i]} to {slices[i+1]}')
    sliced=all_lines[0][slices[i]:slices[i+1]]
    final = final + sliced

print(final)


all_expressions = re.findall("mul\([\d]{1,3},[\d]{1,3}\)", final)

print(all_expressions)

sum = 0

for result in all_expressions:
    numbers = re.search("[\d]{1,3},[\d]{1,3}", result)
    # print(numbers.group())
    first,second = numbers.group().split(",")
    multiplier = int(first) * int(second)
    # print(multiplier)
    sum = sum + multiplier

print(sum)



