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

@lru_cache(maxsize = 128)
def blink(stone):
    stone_string=str(stone)
    if len(stone_string) % 2 == 0: 
        length_of_stone=len(stone_string)
        splitat=length_of_stone // 2
        left, right = stone_string[:splitat], stone_string[splitat:]
        return [int(left), int(right)]
    else:
        value = int(stone) * 2024
        return [value]

def many_blinks(rounds):

    stones_dict={'0': [1]}
    duplicate_stones_dict=defaultdict()

    for stone in stones:
        duplicate_stones_dict[f'{stone}']=1

    for j in range(rounds):
        # print(f'Blink {j}')
        for k,v in duplicate_stones_dict.copy().items():
            # print(f'Key: {k} -- Value: {v}')
            if v > 0:
                try:
                    change=stones_dict[f'{k}']
                    duplicate_stones_dict[f'{k}']-=v
                    for item in change:
                        try:
                            duplicate_stones_dict[f'{item}']+=v
                        except:
                            duplicate_stones_dict[f'{item}']=v
                except:
                    #print(k)
                    change=blink(k)
                    #print(change)
                    stones_dict[f'{k}']=change
                    duplicate_stones_dict[f'{k}']-=v
                    for item in change:
                        try:
                            duplicate_stones_dict[f'{item}']+=v
                        except:
                            duplicate_stones_dict[f'{item}']=v
            #print(stones_dict)
            #print(duplicate_stones_dict)

    sum=0

    for k,v in duplicate_stones_dict.items():
        sum = sum + v

    return sum

part1=many_blinks(25)
print(f'Part 1: {part1}')

part2=many_blinks(75)
print(f'Part 2: {part2}')