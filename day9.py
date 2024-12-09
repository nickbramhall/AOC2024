input_file = 'input/day9.txt'

# Read in all the data and strip out any whitespace at the end of lines
all_lines = [line.rstrip('\n') for line in open(input_file)]

# print(all_lines)

i=0
index=0
output=''

for c in all_lines[0]:
    # print(c)
    if i % 2 ==0:
        # Number is a file
        # print(f'File. Index: {index}. Repeats: {c}')
        output=output+(int(c)*str(index))
        index+=1
    else:
        # print('Space')
        output=output+(int(c)*'.')
    i+=1

print(output)

def change_letter(string, letter, index):  # note string is actually a bad name for a variable
    return string[:index] + letter + string[index+1:]

space = True

while space is True:
    last_char=output[-1]
    if last_char=='.':
        output=output[:-1]
    else:
        search=output.find('.')
        # print(search)
        output=change_letter(output, last_char, search)
        output=output[:-1]
    # print(output)
    if '.' not in output:
        space = False
    # space = False

print(output)

i=0
sum=0
for c in output:
    # print(c)
    sum= sum + (int(c)*i)
    i+=1

print(sum)
