input_file = 'input/day6.txt'

# Read in all the data and strip out any whitespace at the end of lines
all_lines = [line.rstrip('\n') for line in open(input_file)]

print(all_lines)

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

no_rows=len(all_lines)
no_cols=len(all_lines[0])

print(f'Grid is {no_rows} rows by {no_cols} columns')

sum=0
row=start_pos[1]
col=start_pos[0]
direction="up"
visited=[]

while True:
    new_row,new_col = movement(row,col,direction)
    # print(f'Moved to {new_col},{new_row} which contains a {all_lines[new_row][new_col]}')
    if new_col >= no_cols or new_col < 0:
        print('Out of bounds!')
        break
    if new_row >= no_rows or new_row < 0:
        print('Out of bounds!')
        break
    # Get the new square contents
    if all_lines[new_row][new_col] == "#":
        print('Square is occupied so turn')
        if direction == "up":
            direction = "right"
        elif direction == "right":
            direction = "down"
        elif direction == "down":
            direction = "left"
        else:
            direction = "up"
    else:
        print('Square is empty so move on')
        if (new_row,new_col) not in visited:
            visited.append((new_row,new_col))
            sum += 1
        row=new_row
        col=new_col
    # print(f'Moved to {new_col},{new_row} which contains a {all_lines[new_row][new_col]}')
print(sum)