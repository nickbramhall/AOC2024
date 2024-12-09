input_file = 'input/day9.txt'

# Read in all the data and strip out any whitespace at the end of lines
all_lines = [line.rstrip('\n') for line in open(input_file)]

# print(all_lines)

i=0
index=0
output=[]

for c in all_lines[0]:
    # print(c)
    if i % 2 ==0:
        # Number is a file
        # print(f'File. Index: {index}. Repeats: {c}')
        for j in range(int(c)):
            output.append(str(index))
        index+=1
    else:
        # print('Space')
        for j in range(int(c)):
            output.append('.')
    i+=1

# print(output)

space = True

while space is True:
    if '.' not in output:
        space = False
        break
    last_char=output[-1]
    if last_char=='.':
        output=output[:-1]
    else:
        search=output.index('.')
        # print(search)
        output[search]=last_char
        output=output[:-1]
    # print(output)
    
    # space = False

# print(f'Output is: {output}')

i=0
sum=0
for c in output:
    # print(c)
    sum= sum + (int(c)*i)
    i+=1

print(f'Part 1: {sum}')

##### Part 2 #####

i=0
output=[]
index=0
search_terms=[]

for c in all_lines[0]:
    # print(c)
    if c == '0':
        # print('It is zero')
        pass
    elif i % 2 == 0:
        # Number is a file
        # print(f'File. Index: {index}. Repeats: {c}')
        if c != '0':
            output.append((index,int(c)))
        search_terms.append((index,int(c)))
        index+=1
    else:
        # print('Space')
        output.append(('X',int(c)))
    i+=1

# print(output)

search_terms.reverse()

# print(search_terms)

for search in search_terms:
    # print(f'Checking {search}')
    j=0
    for entry in output:
        if entry == search:
            break
        # print(f'Testing {entry}')
        if entry[0] == 'X' and entry[1] >= search[1]:
            # print('Found a space!')
            # First remove the index
            location=output.index(search)
            output.remove(search)
            # Replace the removed tuple with 'X' tuple of the same length
            padding_to_insert = ('X', search[1])
            output.insert(location,padding_to_insert)
            # Tidy up any duplicated 'X' groupings
            before=''
            after=''
            try:
                before = output[location-1][0]
            except:
                # print("An exception occurred")
                pass
            try:
                after = output[location+1][0]
            except:
                # print("An exception occurred")
                pass
            if before == 'X' and after == 'X':
                # print('We need to sort out the X!')
                output[location-1]=('X',output[location+1][1]+output[location][1]+output[location-1][1])
                output.pop(location)
                output.pop(location)
            # Add the index into the new location
            output[j]=search
            # Add any padding after the index
            padding = entry[1] - search[1]
            if padding > 0:
                padding_to_insert = ('X', padding)
                output.insert(j+1,padding_to_insert)
            # Tidy up any duplicate padding
            # print(output)
            break
        j+=1

output_lst=[]

for entry in output:
    for i in range(entry[1]):
        output_lst.append(entry[0])

i=0
sum=0
for c in output_lst:
    # print(c)
    if c != 'X':
        sum = sum + (int(c)*i)
    i+=1

print(f'Part 2: {sum}')