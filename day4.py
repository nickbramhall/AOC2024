input_file = 'input/day4.txt'

# Read in all the data and strip out any whitespace at the end of lines
all_lines = [line.rstrip('\n') for line in open(input_file)]

print(all_lines)

no_of_cols=len(all_lines[0])
no_of_rows=len(all_lines)

print(f'Grid is {no_of_cols} columns by {no_of_rows} rows')

# From a search point figure all valid search directions and gather the four characters in each direction
# then check if that == XMAS

all_lines_list=[]
for line in all_lines:
    line_list=[]
    line_list_check=[]
    for c in line:
        line_list.append(c)
    all_lines_list.append(line_list)

print(all_lines_list)

xmas_counter=0

for i in range(no_of_rows):
    for j in range(no_of_cols):
        print(f'{i},{j}')
        # Get l-r if valid
        if j < (no_of_cols - 3):
            char1=all_lines_list[i][j]
            char2=all_lines_list[i][j+1]
            char3=all_lines_list[i][j+2]
            char4=all_lines_list[i][j+3]
            chars=char1+char2+char3+char4
            # print(chars)
            if chars == 'XMAS':
                print('L-R Match found!')
                xmas_counter += 1
        # Get r-l if valid
        if j >= 3:
            chars = all_lines_list[i][j] + all_lines_list[i][j-1] + all_lines_list[i][j-2] + all_lines_list[i][j-3]
            # print(chars)
            if chars == 'XMAS':
                print('R-L Match found!')
                xmas_counter += 1
        # Get t-d if valid
        if i < (no_of_rows - 3):
            chars = all_lines_list[i][j] + all_lines_list[i+1][j] + all_lines_list[i+2][j] + all_lines_list[i+3][j]
            # print(chars)
            if chars == 'XMAS':
                print('T-D Match found!')
                xmas_counter += 1
        # Get d-t if valid
        if i >= 3:
            chars = all_lines_list[i][j] + all_lines_list[i-1][j] + all_lines_list[i-2][j] + all_lines_list[i-3][j]
            # print(chars)
            if chars == 'XMAS':
                print('D-T Match found!')
                xmas_counter += 1
        # Get diag-l-r if valid
        if j < (no_of_cols - 3) and i < (no_of_rows - 3):
            chars = all_lines_list[i][j] + all_lines_list[i+1][j+1] + all_lines_list[i+2][j+2] + all_lines_list[i+3][j+3]
            # print(chars)
            if chars == 'XMAS':
                print('DIAG-L-R Match found!')
                xmas_counter += 1
        # Get diag-r-l if valid
        if j >= 3 and i < (no_of_rows - 3):
            chars = all_lines_list[i][j] + all_lines_list[i+1][j-1] + all_lines_list[i+2][j-2] + all_lines_list[i+3][j-3]
            # print(chars)
            if chars == 'XMAS':
                print('DIAG-R-L Match found!')
                xmas_counter += 1
        # Get diag-r-l if valid
        if j < (no_of_cols - 3) and i >= 3:
            chars = all_lines_list[i][j] + all_lines_list[i-1][j+1] + all_lines_list[i-2][j+2] + all_lines_list[i-3][j+3]
            # print(chars)
            if chars == 'XMAS':
                print('DIAG-R-L Match found!')
                xmas_counter += 1
        # Get diag-r-l if valid
        if j >= 3 and i >= 3:
            chars = all_lines_list[i][j] + all_lines_list[i-1][j-1] + all_lines_list[i-2][j-2] + all_lines_list[i-3][j-3]
            # print(chars)
            if chars == 'XMAS':
                print('DIAG-R-L Match found!')
                xmas_counter += 1


print(f'Part 1: {xmas_counter}')

# Part 2

xmas_counter=0

for i in range(1,no_of_rows-1,1):
    for j in range(1,no_of_cols-1,1):
        print(f'{i},{j}')
        if all_lines_list[i][j] == 'A':
            check = all_lines_list[i-1][j-1] + all_lines_list[i-1][j+1] + all_lines_list[i+1][j-1] + all_lines_list[i+1][j+1]
            checklist=['MMSS','SMSM','MSMS','SSMM']
            if check in checklist:
                xmas_counter += 1

print(f'Part 2: {xmas_counter}')