input_file = 'input/day2.txt'

# Read in all the data and strip out any whitespace at the end of lines
all_lines = [line.rstrip('\n') for line in open(input_file)]

print(all_lines)

# Safety Criteria
# - The levels are either all increasing or all decreasing.
# - Any two adjacent levels differ by at least one and at most three.

def all_positive(levels):
    safe = True
    i=0
    for i in range(len(levels)-1):
        next_level = int(levels[i+1])
        this_level = int(levels[i])
        difference = next_level - this_level
        # print(f'{next_level} - {this_level} = {difference}')
        if difference <= 0 or difference > 3:
            safe = False
            break
    return safe

def all_negative(levels):
    safe = True
    i=0
    for i in range(len(levels)-1):
        next_level = int(levels[i+1])
        this_level = int(levels[i])
        difference = this_level - next_level
        # print(f'{this_level} - {next_level} = {difference}')
        if difference <= 0 or difference > 3:
            safe = False
            break
    return safe  

safe_count = 0
line_count = 0
unsafe_reports = []

for line in all_lines:
    levels=line.split()
    # report = [int(level) for level in rep.split()]
    # print(levels)
    all_positive_check = all_positive(levels)
    all_negative_check = all_negative(levels)
    # print(f'Check all rising? {all_positive_check}')
    # print(f'Check all falling? {all_negative_check}')
    if all_positive_check is True or all_negative_check is True:
        print(f'Report is safe!')
        safe_count += 1
    else:
        print(f'Report is unsafe!')
        unsafe_reports.append(line_count)
    line_count += 1

print(f'Part 1: {safe_count} safe reports')

# Part 2

print(f'Starting part 2')

# Just check the reports recorded as unsafe in part 1
# Try removing an element and then checking pass criteria

for report in unsafe_reports:
    level=all_lines[report].split()
    for i in range(len(level)):
        new_level = level[:]
        new_level.pop(i)
        all_positive_check = all_positive(new_level)
        all_negative_check = all_negative(new_level)
        # print(f'Check all rising? {all_positive_check}')
        # print(f'Check all falling? {all_negative_check}')
        if all_positive_check is True or all_negative_check is True:
            print(f'Report is now safe!')
            safe_count += 1
            break

print(f'Part 2: {safe_count} safe reports')