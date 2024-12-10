input_file = 'input/day10.txt'

# Read in all the data and strip out any whitespace at the end of lines
all_lines = [line.rstrip('\n') for line in open(input_file)]

# Find all start positions

start_positions=[]

row=0
for line in all_lines:
    col=0
    for c in line:
        if c == "0":
            start_pos=(row,col,0)
            start_positions.append(start_pos)
        col+=1
    row+=1

no_rows=len(all_lines)
no_cols=len(all_lines[0])

print(f'Grid is {no_rows} rows by {no_cols} columns')

def test_inbounds(position):
    if position[0] >= 0 and position[0] < no_rows and position[1] >= 0 and position[1] < no_cols:
        return True
    else:
        return False
    
def test_height(position):
    new_height = int(all_lines[position[0]][position[1]])
    if new_height - position[2] == 1:
        return new_height
    else:
        return False

def valid_moves(position):
    up=(position[0]-1,position[1],position[2])
    down=(position[0]+1,position[1],position[2])
    left=(position[0],position[1]-1,position[2])
    right=(position[0],position[1]+1,position[2])
    moves=[up,down,left,right]
    for move in moves:
        if test_inbounds(move):
            test_new_height=test_height(move)
            if test_new_height == 9:
                unique_visited.add(move)
                times_visited.append(move)
            if test_new_height != False:
                move = (move[0],move[1],test_new_height)
                visited.append(move)
            
overall_sum=0
pt2_overall_sum=0

for start_pos in start_positions:
    visited=[]
    unique_visited=set()
    times_visited=[]
    visited.append(start_pos)
    while visited:
        position=visited.pop(0)
        moves=valid_moves(position)
    sum=len(unique_visited)
    pt2_sum=len(times_visited)
    overall_sum=overall_sum+sum
    pt2_overall_sum=pt2_overall_sum+pt2_sum

print(f'Part 1: {overall_sum}')
print(f'Part 2: {pt2_overall_sum}')