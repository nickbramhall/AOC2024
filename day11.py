from functools import lru_cache 
from collections import defaultdict

input_file = 'input/day11.txt'

# Read in all the data and strip out any whitespace at the end of lines
all_lines = [line.rstrip('\n') for line in open(input_file)]

stones=[]

for line in all_lines:
    output=line.split()
    for entry in output:
        stones.append(int(entry))

print(stones)

# Use a lru_cache from functools to avoid recalculating the change to a stone - if the value exists in the cache it will be returned without re-calculating
# A list is returned so that it can be iterated over whenter it returns 1 stone (rules 1 and 3) or 2 stones (rule 2)
@lru_cache(maxsize = 128)
def blink(stone):
    stone_string=str(stone)
    # First rule - if Stone has 0 on it, the new Stone has 1 on it
    if stone_string == '0':
        return [1]
    # Second rule - if Stone has number on it than be evenly divided, then two new stones are created with the first half and last half
    elif len(stone_string) % 2 == 0: 
        length_of_stone=len(stone_string)
        splitat=length_of_stone // 2
        left, right = stone_string[:splitat], stone_string[splitat:]
        return [int(left), int(right)]
    # Otherwise a new stone is created with the value of the new stone 2024 times the original stone's value
    else:
        value = int(stone) * 2024
        return [value]

def many_blinks(rounds):
    # First add all the starting stones into a dictionary
    duplicate_stones_dict=defaultdict()
    for stone in stones:
        duplicate_stones_dict[f'{stone}']=1
    # Now run a loop for every blink taken to determine how the stones change
    for j in range(rounds):
        for k,v in duplicate_stones_dict.copy().items():
            # If value is greater than 0 then we need to determine the change to the stone
            if v > 0:
                change=blink(k)
                # Remove the existing stones we are checking
                duplicate_stones_dict[f'{k}']-=v
                # Loop through the response and add in the stones to the dict, either increasing or adding in a new key
                for item in change:
                    try:
                        duplicate_stones_dict[f'{item}']+=v
                    except:
                        duplicate_stones_dict[f'{item}']=v
    # Now add up all the values in the stones dictionary to get the total number of stones
    sum=0
    for v in duplicate_stones_dict.values():
        sum = sum + v
    return sum

part1=many_blinks(25)
print(f'Part 1: {part1}')

part2=many_blinks(75)
print(f'Part 2: {part2}')