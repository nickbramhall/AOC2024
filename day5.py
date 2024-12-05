input_file = 'input/day5.txt'

rules, pages = [part.splitlines() for part in open(input_file).read().split("\n\n")]

list1=[]
list2=[]
list3=[]

for line in rules:
    output=line.split("|")
    list1.append(int(output[0]))
    list2.append(int(output[1]))

for line in pages:
    output=line.split(",")
    # print(output)
    temp_list=[]
    for entry in output:
        temp_list.append(int(entry))
    list3.append(temp_list)

answer=0
incorrects=[]

for entry in list3:
    # loop through the list of instructions (list1 and list2)
    for i in range(len(list1)):
        # Check if both rule numbers are in the list?
        if list1[i] in entry and list2[i] in entry:
            # This rule applies to the list so check it
            rules_followed=True
            # Get the position within the list of pages of the two pages we are checking
            j=0
            for page in entry:
                if page == list1[i]:
                    page1_position=j
                if page == list2[i]:
                    page2_position=j
                j+=1
            # print(f'Page 1 found at {page1_position} - Page 2 found at {page2_position}')
            # Check if page1 appears before page2
            if page1_position < page2_position:
                # print(f'These pages are correct!')
                continue
            # If page1 is after page2 then the rule is broken and we can exit the loop
            else:
                rules_followed=False
                break
        else:
            continue
    if rules_followed == True:
        # print(f'All rules have been followed!')
        # print(entry)
        middle = len(entry) // 2
        answer =answer + entry[middle]
    else:
        incorrects.append(entry)

print(f'Part 1: {answer}')

# Part 2

# print(incorrects)
answer=0

for entry in incorrects:
    change_made=True
    while change_made is True:
        change_made=False
        for i in range(len(list1)):
            if list1[i] in entry and list2[i] in entry:
                j=0
                for page in entry:
                    if page == list1[i]:
                        page1_position=j
                    if page == list2[i]:
                        page2_position=j
                    j+=1
                # print(f'Page 1 found at {page1_position} - Page 2 found at {page2_position}')
                if page1_position < page2_position:
                    # print(f'These pages are correct!')
                    continue
                else:
                    # Swap the pages
                    entry[page1_position]=list2[i]
                    entry[page2_position]=list1[i]
                    change_made=True
            else:
                continue
    # print(f'Corrected entry: {entry}')
    middle = len(entry) // 2
    answer = answer + entry[middle]

print(f'Part 2: {answer}')