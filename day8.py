from itertools import combinations

input_file = 'input/day8.txt'

# Read in all the data and strip out any whitespace at the end of lines
all_lines = [line.rstrip('\n') for line in open(input_file)]

# print(all_lines)

no_rows=len(all_lines)
no_cols=len(all_lines[0])

print(f'Grid is {no_rows} rows by {no_cols} columns')

def grid_printer():
    for i in range(no_rows):
        row_print=''
        for j in range(no_cols):
            if (i,j) in results:
                row_print = row_print + '0'
            elif (i,j) in an_inbounds:
                row_print = row_print + '#'
            else:
                row_print = row_print + '.'
        print(row_print)

search_chars=set()

for row in range(no_rows):
    for col in range(no_cols):
        c=all_lines[row][col]
        search_chars.add(c)

search_chars.remove('.')

print(search_chars)

# search_chars=['0','A']

results={}

for c in search_chars:
    results[c]=[]

position=[]

for row in range(no_rows):
    for col in range(no_cols):
        c=all_lines[row][col]
        for char in search_chars:
            if c == char:
                temp_list=results[char]
                temp_list.append((row,col))
                results[char]=temp_list

print(results)

def antinode(position1,position2):
    row_distance=abs(position1[0]-position2[0])
    col_distance=abs(position1[1]-position2[1])
    if position2[1] < position1[1]:
        antinode1_row=position1[0]-row_distance
        antinode1_col=position1[1]+col_distance
        antinode2_row=position2[0]+row_distance
        antinode2_col=position2[1]-col_distance
    else:
        antinode1_row=position1[0]-row_distance
        antinode1_col=position1[1]-col_distance
        antinode2_row=position2[0]+row_distance
        antinode2_col=position2[1]+col_distance
    return (antinode1_row,antinode1_col),(antinode2_row,antinode2_col)


def antinode2(position1,position2,multiplier):
    row_distance=abs(position1[0]-position2[0])
    col_distance=abs(position1[1]-position2[1])
    if position2[1] < position1[1]:
        antinode1_row=position1[0]-(row_distance*multiplier)
        antinode1_col=position1[1]+(col_distance*multiplier)
        antinode2_row=position2[0]+(row_distance*multiplier)
        antinode2_col=position2[1]-(col_distance*multiplier)
    else:
        antinode1_row=position1[0]-(row_distance*multiplier)
        antinode1_col=position1[1]-(col_distance*multiplier)
        antinode2_row=position2[0]+(row_distance*multiplier)
        antinode2_col=position2[1]+(col_distance*multiplier)
    return (antinode1_row,antinode1_col),(antinode2_row,antinode2_col)

antinodes=set()

for values in results.values():
    # print(values)
    position_pairs = combinations(values, 2)
    for pair in position_pairs:
        # print(pair)
        antinode_pair=antinode(pair[0],pair[1])
        for an_pair in antinode_pair:
            antinodes.add(an_pair)

# print(antinodes)

an_inbounds=[]

for antinode in antinodes:
    # print(antinode)
    if antinode[0] >= 0 and antinode[0] <= no_rows-1 and antinode[1] >= 0 and antinode[1] <= no_cols-1:
        an_inbounds.append(antinode)

print(an_inbounds)

print(len(an_inbounds))

grid_printer()

# Part 2

antinodes=set()

for values in results.values():
    for value in values:
        antinodes.add(value)
    # print(values)
    position_pairs = combinations(values, 2)
    for pair in position_pairs:
        # print(pair)
        multiplier=1
        while multiplier < 100:
            antinode_pair=antinode2(pair[0],pair[1],multiplier)
            for an_pair in antinode_pair:
                antinodes.add(an_pair)
            multiplier+=1

an_inbounds=[]

for antinode in antinodes:
    # print(antinode)
    if antinode[0] >= 0 and antinode[0] <= no_rows-1 and antinode[1] >= 0 and antinode[1] <= no_cols-1:
        an_inbounds.append(antinode)

print(an_inbounds)

print(len(an_inbounds))

grid_printer()