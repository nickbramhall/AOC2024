input_file = 'input/day12-sample.txt'

# Read in all the data and strip out any whitespace at the end of lines
all_lines = [line.rstrip('\n') for line in open(input_file)]

# print(all_lines)

grid=[]
to_visit=[]
row=0

for line in all_lines:
    temp_list=[]
    col=0
    for c in line:
        temp_list.append(c)
        to_visit.append((row,col))
        col+=1
    grid.append(temp_list)
    row+=1

# print(grid)
# print(to_visit)

no_rows=len(grid)
no_cols=len(grid[0])

print(f'Grid is {no_rows} rows by {no_cols} cols')

moves=['up','down','left','right']

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

start=(0,0)

region_search=[]

region_dict={}

i=0

while to_visit:
    #Start with the next region in the list of those still to visit
    region_search.append(to_visit[0])
    # print(f'Next search starts at: {to_visit[0]}')
    #Reset the perimeter and area counters
    region_perimeter=0
    region_area=0
    searched=[]
    #Search until there is no more of the same region to visit
    while region_search:
        current_plot=region_search.pop(0)
        # searched.append(current_plot)
        # print(f'Searching {current_plot}')
        current_region=grid[current_plot[0]][current_plot[1]]
        # print(f'This region contains a: {current_region}')
        for direction in moves:
            # print(f'Try {direction}')
            new_row,new_col=movement(current_plot[0],current_plot[1],direction)
            if new_row >= 0 and new_row < no_rows and new_col >=0 and new_col < no_cols:
                # print('In bounds')
                new_region=grid[new_row][new_col]
                if current_region == new_region:
                    # print('Region is the same!')
                    if (new_row,new_col) not in searched and (new_row,new_col) not in region_search:
                        region_search.append((new_row,new_col))
                else:
                    # print('New region')
                    region_perimeter+=1
            else:
                # print('Out of bounds')
                region_perimeter+=1
        searched.append((current_plot[0],current_plot[1]))
        # region_search.append(current_plot)
        # print(f'We have now searched {searched} and we still have to check: {region_search}')
        region_area+=1
        # print(f'To visit: {to_visit}')
        # print(f'Removing: {(current_plot[0],current_plot[1])} from to_visit')
        to_visit.remove((current_plot[0],current_plot[1]))
    region_dict[i]={'region':current_region, 'area': region_area, 'perimeter': region_perimeter, 'cells': searched}
    
    i+=1

print(region_dict)

sum=0

for k,v in region_dict.items():
    calculation=v['area']*v['perimeter']
    sum=sum+calculation

print(sum)

# Part 2

def check_for_corners(region,cell):
    # Try up
    for direction in moves:
        new_row,new_col=movement(cell[0],cell[1],direction)
        if new_row >= 0 and new_row < no_rows and new_col >=0 and new_col < no_cols:
            inbounds=True
            if new_region=grid[new_row][new_col] == region:
                sameregion=True
            


for k,v in region_dict.items():
    for cell in v['cells']:
        print(cell)
