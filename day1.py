input_file = 'input/day1.txt'

# Read in all the data and strip out any whitespace at the end of lines
all_lines = [line.rstrip('\n') for line in open(input_file)]

# print(all_lines)

list1=[]
list2=[]

for line in all_lines:
    output=line.split()
    list1.append(int(output[0]))
    list2.append(int(output[1]))

list1=sorted(list1)
list2=sorted(list2)

# print(list1)
# print(list2)

i = 0
total_distance = 0

for i in range(len(list1)):
    distance = list2[i] - list1[i]
    print(f'Distance between {list2[i]} and {list1[i]} is {distance}')
    total_distance = total_distance + abs(distance)

print(f'Part 1: Total distance is: {total_distance}')

## Part 2

total_similarity = 0

for number in list1:
    number_of_appearances = list2.count(number)
    print(f'The number {number} appears {number_of_appearances} times')
    total_similarity = total_similarity + (number * number_of_appearances)

print(f'Part 2: Total similarity is: {total_similarity}')