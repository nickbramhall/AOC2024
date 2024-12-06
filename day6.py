import time
import os

input_file = 'input/day6.txt'

# Read in all the data and strip out any whitespace at the end of lines
all_lines = [line.rstrip('\n') for line in open(input_file)]

# print(all_lines)

# Find start position

y=0
for line in all_lines:
    x=0
    for c in line:
        if c == "^":
            start_pos=(x,y)
        x+=1
    y+=1

print(start_pos)

def clear():
    os.system( 'cls' )

def movement(row,col,direction):
    if direction == "up":
        col=col
        row=row-1
    if direction == "down":
        col=col
        row=row+1
    if direction == "left":
        col=col-1
        row=row
    if direction == "right":
        col=col+1
        row=row
    return row,col

def grid_printer():
    clear()
    for i in range(no_rows):
        row_print=''
        for j in range(no_cols):
            if all_lines[i][j] == "#":
                row_print = row_print + '#'
            elif (i,j) in visited:
                row_print = row_print + 'X'
            else:
                row_print = row_print + '.'
        print(row_print)

no_rows=len(all_lines)
no_cols=len(all_lines[0])

print(f'Grid is {no_rows} rows by {no_cols} columns')

# The initial gaurd's position counts as a visited square so needs adding into the visited list here

sum=1
row=start_pos[1]
col=start_pos[0]
direction="up"
visited=[(row,col)]
path=[]

while True:
    new_row,new_col = movement(row,col,direction)
    # print(f'Moved to {new_col},{new_row} which contains a {all_lines[new_row][new_col]}')
    if new_col >= no_cols or new_col < 0:
        # print('Out of bounds!')
        break
    if new_row >= no_rows or new_row < 0:
        # print('Out of bounds!')
        break
    # Get the new square contents
    if all_lines[new_row][new_col] == "#":
        # print('Square is occupied so turn')
        if direction == "up":
            direction = "right"
        elif direction == "right":
            direction = "down"
        elif direction == "down":
            direction = "left"
        else:
            direction = "up"
    else:
        # print('Square is empty so move on')
        path.append((new_row,new_col))
        if (new_row,new_col) not in visited:
            visited.append((new_row,new_col))
            sum += 1
        row=new_row
        col=new_col
    # print(f'Moved to {new_col},{new_row} which contains a {all_lines[new_row][new_col]}')
    # grid_printer()
    # time.sleep(1)
print(f'Part 1: {sum}')

# Part 2

def path_tester():

    row=start_pos[1]
    col=start_pos[0]
    direction="up"
    visited=[(row,col)]
    counter=0
    out_of_bounds=False

    while counter < 10000:
        new_row,new_col = movement(row,col,direction)
        # print(f'Moved to {new_col},{new_row} which contains a {all_lines[new_row][new_col]}')
        if new_col >= no_cols or new_col < 0:
            out_of_bounds=True
            break
        if new_row >= no_rows or new_row < 0:
            out_of_bounds=True
            break
        # Get the new square contents
        if all_lines[new_row][new_col] == "#":
            # print('Square is occupied so turn')
            if direction == "up":
                direction = "right"
            elif direction == "right":
                direction = "down"
            elif direction == "down":
                direction = "left"
            else:
                direction = "up"
        else:
            # print('Square is empty so move on')
            if (new_row,new_col) not in visited:
                visited.append((new_row,new_col))
            row=new_row
            col=new_col
        counter+=1

    if out_of_bounds is True:
        return False
    else:
        return True

# We can only place a single obstruction so it must be somewhere on the existing path. So test each square along the path for loops???
# What is the criteria for a loop? No out of bounds after 100 attempts?

def replace_str_index(text,index,replacement):
    return f'{text[:index]}{replacement}{text[index+1:]}'

count=0
loop_obstructions=[]

for location in path:
    # add obstruction at the first location
    if all_lines[location[0]][location[1]]!='#':
        #print(all_lines)
        all_lines[location[0]]=replace_str_index(all_lines[location[0]],location[1],'#')
        #print(all_lines)
        # all_lines[location[0]][location[1]]='#'
        test_result=path_tester()
        if test_result is False:
            all_lines[location[0]]=replace_str_index(all_lines[location[0]],location[1],'.')
        else:
            # print('Loop found!')
            if location not in loop_obstructions:
                loop_obstructions.append(location)
                count+=1
            all_lines[location[0]]=replace_str_index(all_lines[location[0]],location[1],'.')
        #print(all_lines)

print(f'Part 2: {count}')
# print(loop_obstructions)
# This works but is suuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuper slow