input_file = 'input/day7.txt'

from itertools import permutations, product

# Read in all the data and strip out any whitespace at the end of lines
all_lines = [line.rstrip('\n') for line in open(input_file)]

# print(all_lines)

all_results=[]
all_numbers=[]

for line in all_lines:
    result, numbers = line.split(": ")
    all_results.append(int(result))
    all_numbers.append(numbers)

# print(all_results)
# print(all_numbers)

all_number_lists=[]

for set_of_numbers in all_numbers:
    output=set_of_numbers.split()
    all_number_lists.append(output)

print(all_number_lists)

def calculator2(numbers,operators):
    expression=''
    for i in range(len(numbers)-1):
        expression = expression + f'{numbers[i]}{operators[i]}'
    expression = expression+f'{numbers[-1]}'
    print(expression)
    result=eval(expression)
    return result

def calculator(numbers,operators):
    sum=numbers[0]
    # print(sum)
    if len(operators)>1:
        for i in range(len(operators)):
            # print(f'Operators[i]: {operators[i]}')
            # print(f'Numbers[i+1]: {numbers[i+1]}')
            expression=f'{sum}{operators[i]}{numbers[i+1]}'
            # print(expression)
            sum=eval(expression)
            # print(sum)
    else:
        expression=f'{sum}{operators[-1]}{numbers[-1]}'
        sum=eval(expression)
    return sum

def calculator3(numbers,operators):
    sum=numbers[0]
    # print(sum)
    if len(operators)>1:
        for i in range(len(operators)):
            if operators[i] == '|':
                sum=int(f'{sum}{numbers[i+1]}')
                # print(f'Operators[i]: {operators[i]}')
                # print(f'Numbers[i+1]: {numbers[i+1]}')
            else:
                expression=f'{sum}{operators[i]}{numbers[i+1]}'
                # print(expression)
                sum=eval(expression)
                # print(sum)
    else:
        if operators[-1] == '|':
            sum=int(f'{sum}{numbers[-1]}')
        else:
            expression=f'{sum}{operators[-1]}{numbers[-1]}'
            sum=eval(expression)
    return sum

def operators(number,width):
    list_of_binary = ['{:{width}b}'.format(i,width=width) for i in range(number)]
    # print(list_of_binary)
    letters="01"
    cipher="+*"
    dict_cipher = str.maketrans(letters,cipher)
    operator_combos=[]
    for entry in list_of_binary:
        operator_combos.append((entry.translate(dict_cipher)))
    return operator_combos

def to_base3(n):
    if n == 0:
        return '0'
    digits = []
    while n:
        digits.append(str(n % 3))
        n //= 3
    return ''.join(reversed(digits))

def operators3(number,width):
    list_of_binary=[]
    for i in range(number):
        list_of_binary.append(to_base3(i).zfill(width))  # Pad to width 4
    # print(list_of_binary)
    letters="012"
    cipher="+*|"
    dict_cipher = str.maketrans(letters,cipher)
    operator_combos=[]
    for entry in list_of_binary:
        operator_combos.append((entry.translate(dict_cipher)))
    return operator_combos

# list_of_operators = ['+','*']
test_sum=0
j=0
correct=[]
for entry in all_number_lists:
    # print(entry)
    number_of_operators=2 ** (len(entry)-1) # For Part 1
    # print(number_of_operators)
    width=f'0{len(entry)-1}' # For Part 1
    operator_combos = operators(number_of_operators,width)
    # print(operator_combos)
    for combo in operator_combos:
        result = calculator(entry,combo)
        # print(f'Does {result} match {all_results[j]}?')
        if result == all_results[j]:
            # print(f'Result is correct!')
            test_sum=test_sum+result
            correct.append(j)
            break
    j+=1

print(f'Part 1: {test_sum}')

# Part 2

test_sum_pt2=0
j=0
for entry in all_number_lists:
    if j not in correct:
        # print(entry)
        number_of_operators=3 ** (len(entry)-1)
        # print(number_of_operators)
        width=len(entry)-1
        operator_combos = operators3(number_of_operators,width)
        # print(operator_combos)
        for combo in operator_combos:
            result = calculator3(entry,combo)
            # print(f'Does {result} match {all_results[j]}?')
            if result == all_results[j]:
                # print(f'Result is correct!')
                test_sum_pt2=test_sum_pt2+result
                break
    j+=1

final_result=test_sum+test_sum_pt2
print(f'Part 2: {final_result}')
