input_file = 'input/day9.txt'

# Read in all the data and strip out any whitespace at the end of lines
all_lines = [line.rstrip('\n') for line in open(input_file)]

print(all_lines)

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

print(output)

space = True

while space is True:
    last_char=output[-1]
    if last_char=='.':
        output=output[:-1]
    else:
        search=output.index('.')
        # print(search)
        output[search]=last_char
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

# Part 2

output=[]
index=0

for c in all_lines[0]:
    # print(c)
    if c == '0':
        print('It is zero')
    elif i % 2 == 0:
        # Number is a file
        # print(f'File. Index: {index}. Repeats: {c}')
        if c != '0':
            output.append(int(c)*str(index))
        index+=1
    else:
        # print('Space')
        output.append(int(c)*'.')
    i+=1

# print(output)

space = True

search_list=output.copy()

search_list.reverse()

print(f'Output Before: {output}')
# print(f'Search list: {search_list}')

for search_entry in search_list:
    if '.' not in search_entry:
        #print(f'Searching to move {search_entry}')
        search_length=len(search_entry)
        if search_length > 0:
            k=0
            for entry in output:
                if entry == search_entry:
                    break
                if '.' in entry:
                    #print(f'Search found {entry} with length {len(entry)} at position {k}')
                    if len(entry) >= search_length:
                        # print(f'String to insert: {string_to_insert}')
                        ## Place the new entry followed by any padding
                        output[k]=search_entry
                        padding = len(entry) - search_length
                        if padding > 0:
                            padding_to_insert = padding * '.'
                            output.insert(k+1,padding_to_insert)
                        # Then we remove the old entry and replace it with . of the same length
                        # print(output)
                        output.reverse()
                        location=output.index(search_entry)
                        #print(f'The old output was found at location {location}')
                        output.remove(search_entry)
                        padding_to_insert = len(search_entry) * '.'
                        output.insert(location,padding_to_insert)
                        output.reverse()
                        #print(output)
                        break
                        # output=output[:-1]
                k+=1
    # j=0
        for j in range(len(output)-3):
            print(f'Testing: {output[j]}, {output[j+1]} and {output[j+2]}')
            if '.' in output[j] and '.' in output[j+1] and '.' in output[j+2]:
                combined_entry =  output[j] + output[j+1] + output[j+2]
                #print(f'Combined entry: {combined_entry}')
                output[j] = combined_entry
                #print(output)
                output.pop(j+1)
                #print(output)
                output.pop(j+1)
                #print(output)
    #print(output)

print(f'Output After: {output}')

output_str=''

for item in output:
    output_str=output_str+item

i=0
sum=0
for c in output_str:
    # print(c)
    if c != '.':
        sum= sum + (int(c)*i)
    i+=1

print(sum)


# while space is True:
#     last_char=output[-1]
#     print(last_char)
#     if '.' in last_char:
#         print('Empty space')
#         output=output[:-1]
#     else:
#         search_length=len(last_char)
#         print(search_length)
#         if search_length > 0:
#             k=0
#             for entry in output:
#                 if '.' in entry:
#                     print(f'Search found {entry}')
#                     if len(entry) > search_length:
#                        padding = len(entry) - search_length
#                        string_to_insert = last_char + (padding*'.')
#                        output[k]=string_to_insert
#                        output=output[:-1]
#                 k+=1
#     # print(output)
#     if '.' not in output:
#         space = False
#     # space = False


