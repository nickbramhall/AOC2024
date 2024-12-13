import re
import itertools
from functools import lru_cache 
   
input_file = 'input/day13.txt'

# Read in all the data and strip out any whitespace at the end of lines
all_lines = [line.rstrip('\n') for line in open(input_file)]

# print(all_lines)

games=[]

for i in range(0, len(all_lines), 4): 
    games.append(all_lines[i:i + 4])

print(f'Number of games: {len(games)}')

pattern=r"X\+(\d+), Y\+(\d+)"
pattern2=r"X\=(\d+), Y\=(\d+)"

game_results=[]

@lru_cache(maxsize = 128)
def sum_numbers(entry, prize_x, prize_y, buttona_x, buttonb_x, buttona_y, buttonb_y):
    sum = entry[0]+entry[1]
    if sum == prize_x:
        a_presses=entry[0] // buttona_x
        b_presses=entry[1] // buttonb_x
        y_total = (a_presses * buttona_y) + (b_presses * buttonb_y)
        if y_total == prize_y:
            cost=a_presses*3 + b_presses
            return (cost,a_presses,b_presses)
    else:
        return None

for game in games:
    list_a_x=[]
    list_a_y=[]
    list_b_x=[]
    list_b_y=[]

    print(game)
    buttona = re.findall(pattern, game[0])
    buttona_x=int(buttona[0][0])
    buttona_y=int(buttona[0][1])
    buttonb = re.findall(pattern, game[1])
    buttonb_x=int(buttonb[0][0])
    buttonb_y=int(buttonb[0][1])
    prize = re.findall(pattern2, game[2])
    prize_x=int(prize[0][0])
    prize_y=int(prize[0][1])

    for i in range(1,100,1):
        list_a_x.append(buttona_x*i)
        list_a_y.append(buttona_y*i)
        list_b_x.append(buttonb_x*i)
        list_b_y.append(buttonb_y*i)

    combinations_x = list(itertools.product(list_a_x, list_b_x))
    # print(combinations_x)

    results=(1000000000,0,0)

    for entry in combinations_x:
        sum = sum_numbers(entry, prize_x, prize_y, buttona_x, buttonb_x, buttona_y, buttonb_y)
        if sum:
            # print(f'Cost is: {sum[0]}')
            if sum[0] < results[0]:
                results=sum
                # results.add(sum)
    # print(results)
    if results[0] != 1000000000:
        game_results.append(results)
        # print(game_results)

money=0

for result in game_results:
    if result:
        # print(result[0])
        money = money + result[0]

print(money)

## Part 2

# Super helpful reddit post about linear algebra and Cramer's Rule
# https://www.reddit.com/r/adventofcode/comments/1hd7irq/2024_day_13_an_explanation_of_the_mathematics/
# https://en.wikipedia.org/wiki/Cramer%27s_rule

# A = (p_x*b_y - prize_y*b_x) / (a_x*b_y - a_y*b_x)
# B = (a_x*p_y - a_y*p_x) / (a_x*b_y - a_y*b_x)

# A = the number of times we press the A button
# B = the number of times we press the B button
# (a_x, a_y) = claw's movement from pressing A
# (b_x, b_y) = claw's movement from pressing B

def cramer(offset, prize_x, prize_y, buttona_x, buttonb_x, buttona_y, buttonb_y):
    prize_x = prize_x + offset
    prize_y = prize_y + offset
    a_presses = ((prize_x*buttonb_y) - (prize_y*buttonb_x)) // ((buttona_x * buttonb_y) - (buttona_y * buttonb_x))
    b_presses = ((buttona_x*prize_y) - (buttona_y * prize_x)) // ((buttona_x * buttonb_y) - (buttona_y * buttonb_x))
    if (a_presses * buttona_x) + (b_presses * buttonb_x) == prize_x and (a_presses * buttona_y) + (b_presses * buttonb_y) == prize_y:
        cost = 3*a_presses + b_presses
        return cost
    else:
        return None

total_pt1=0
total_pt2=0

for game in games:
    print(game)
    buttona = re.findall(pattern, game[0])
    buttona_x=int(buttona[0][0])
    buttona_y=int(buttona[0][1])
    buttonb = re.findall(pattern, game[1])
    buttonb_x=int(buttonb[0][0])
    buttonb_y=int(buttonb[0][1])
    prize = re.findall(pattern2, game[2])
    prize_x=int(prize[0][0])
    prize_y=int(prize[0][1])
    cost_pt1 = cramer(0, prize_x, prize_y, buttona_x, buttonb_x, buttona_y, buttonb_y)
    cost_pt2 = cramer(10000000000000, prize_x, prize_y, buttona_x, buttonb_x, buttona_y, buttonb_y)
    if cost_pt1:
        total_pt1=total_pt1+cost_pt1
    if cost_pt2:
        total_pt2=total_pt2+cost_pt2

print(f'Part 1: {total_pt1}')
print(f'Part 2: {total_pt2}')