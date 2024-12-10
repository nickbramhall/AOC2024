import os

input_file = 'input/day10-sample.txt'

# Read in all the data and strip out any whitespace at the end of lines
all_lines = [line.rstrip('\n') for line in open(input_file)]

# Find start position

start_positions=[]

row=0
for line in all_lines:
    col=0
    for c in line:
        if c == "0":
            start_pos=(row,col)
            start_positions.append(start_pos)
        col+=1
    row+=1

print(start_positions)

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

def valid_moves(start_pos):
    # Try up
    

visited=set()

start_pos=(0,2)

valid_moves=valid_moves(start_pos)
