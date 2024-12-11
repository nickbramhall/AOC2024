input_file = 'input/day11-sample.txt'

# Read in all the data and strip out any whitespace at the end of lines
all_lines = [line.rstrip('\n') for line in open(input_file)]

print(all_lines)

list3=[]

for line in all_lines:
    output=line.split()
    for entry in output:
        list3.append(int(entry))

print(list3)

def blink(stone):
    if stone == 0:
        return 1
    elif stone % 2 == 0: 
        return

    else:
        value = stone * 2024
        return value

