import re

input_file = 'input/day14.txt'

# Read in all the data and strip out any whitespace at the end of lines
all_lines = [line.rstrip('\n') for line in open(input_file)]

# print(all_lines)

pattern=r"p\=(\d+),(\d+) v\=(-?\d+),(-?\d+)"

initial_positions={}
i=0

for line in all_lines:
    results = re.findall(pattern, line)
    pos=(int(results[0][0]),int(results[0][1]))
    vel=(int(results[0][2]),int(results[0][3]))
    initial_positions[i]={'pos':pos, 'vel':vel}
    i+=1

# print(initial_positions)

grid=[]
grid_dict={}
row=0
no_rows=103
no_cols=101

for row in range(no_rows):
    temp_list=[]
    for col in range(no_cols):
        temp_list.append((col,row))
        grid_dict[(col,row)]=0
    grid.append(temp_list)

# print(grid_dict)

def movement(pos,vel):
    pos_x=pos[0]
    pos_y=pos[1]
    new_pos_x=pos_x+vel[0]
    if new_pos_x > no_cols-1:
        new_pos_x = new_pos_x - no_cols
    new_pos_y=pos_y+vel[1]
    if new_pos_x < 0:
        new_pos_x = no_cols + new_pos_x
    if new_pos_y > no_rows-1:
        new_pos_y = new_pos_y - no_rows
    if new_pos_y < 0:
        new_pos_y = no_rows + new_pos_y
    return (new_pos_x,new_pos_y)

# for r in range(5):
#     print(initial_positions[1]['pos'])
#     new_pos = movement(initial_positions[1]['pos'],initial_positions[1]['vel'])
#     initial_positions[1]['pos']=new_pos

for r in range(100):
    # print(r)
    for v in initial_positions.values():
        # print(v['pos'])
        new_pos = movement(v['pos'],v['vel'])
        # print(new_pos)
        v['pos']=new_pos

print(initial_positions)

quad_dict={'tl':0,'tr':0,'bl':0,'br':0}

tlq=(0,(no_cols//2)-1,0,(no_rows//2)-1)
trq=((no_cols//2)+1,no_cols-1,0,(no_rows//2)-1)
blq=(0,(no_cols//2)-1,(no_rows//2)+1,no_rows-1)
brq=((no_cols//2)+1,no_cols-1,(no_rows//2)+1,no_rows-1)

def find_quad(pos):
    col=pos[0]
    row=pos[1]
    if col >= tlq[0] and col <= tlq[1] and row >= tlq[2] and row <= tlq[3]:
        return 'tl'
    elif col >= trq[0] and col <= trq[1] and row >= trq[2] and row <= trq[3]:
        return 'tr'
    elif col >= blq[0] and col <= blq[1] and row >= blq[2] and row <= blq[3]:
        return 'bl'
    elif col >= brq[0] and col <= brq[1] and row >= brq[2] and row <= brq[3]:
        return 'br'
    else:
        return None

for key,value in initial_positions.items():
    quad = find_quad(value['pos'])
    if quad:
        quad_dict[quad]=quad_dict[quad]+1

sum = quad_dict['tl'] * quad_dict['tr'] * quad_dict['bl'] * quad_dict['br']

print(f'Part 1: {sum}')