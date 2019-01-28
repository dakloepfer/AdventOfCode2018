import re, copy
import time

def water_is_caught(y, x):
    global clay_squares
    global flowing_water
    global still_water

    current_y = y 
    current_x = x
    found_gap = False
    clay_to_the_left = None
    clay_to_the_right = None
    # check to the left
    while not (current_y, current_x) in clay_squares and not (current_y, current_x) in still_water:
        if (current_y+1, current_x) in clay_squares or (current_y+1, current_x) in still_water:
            current_x -= 1
        else: 
            found_gap = True
            break 
    
    if not found_gap:
        clay_to_the_left = current_x

        current_y = y 
        current_x = x+1
        # check to the right
        while not (current_y, current_x) in clay_squares and not (current_y, current_x) in still_water:
            if (current_y+1, current_x) in clay_squares or (current_y+1, current_x) in still_water:
                current_x += 1
            else: 
                found_gap = True
                break
        if not found_gap: clay_to_the_right = current_x

    return (not found_gap), clay_to_the_left, clay_to_the_right

with open("/Users/DominikKloepfer/Documents/workspace/Personal_Projects/Advent of Code 2018/Day 17/day17_input1.txt") as input: 
    data = [line.strip() for line in input]

clay_squares = set()

for v in data:
    vein = re.split('=|, |\.\.', v)
    if vein[0] == 'x':
        for d in range(int(vein[3]), int(vein[4])+1):
            clay_squares.add((d, int(vein[1]))) # store as row, column (y, x)
    elif vein[0] == 'y':
        for d in range(int(vein[3]), int(vein[4])+1):
            clay_squares.add((int(vein[1]), d)) # store as row, column (y, x)
    else: print('Something went wrong')

min_y = min(clay_squares)[0]
max_y = max(clay_squares)[0]
print(len(clay_squares))

flowing_water = set()
still_water = set()

flowing_water.add((min_y-1, 500))

changed_something = True
turn = 0
while changed_something:
    turn += 1
    if turn%200 == 0: print(turn, len(flowing_water), len(still_water))
    changed_something = False
    square_iteration = flowing_water.copy() # shallow copy is enough since only have immutable tuples in there

    for stream in square_iteration:
        square_below = (stream[0]+1, stream[1])
        square_left = (stream[0], stream[1]-1)
        square_right = (stream[0], stream[1]+1)
        
        # below is free
        if not square_below in clay_squares and not square_below in flowing_water and not square_below in still_water:
            if stream[0] < max_y:
                flowing_water.add(square_below)
                changed_something = True
        # right is free
        elif not square_right in clay_squares and not square_right in flowing_water and not square_right in still_water:
            if not square_below in flowing_water:
                flowing_water.add(square_right)
                changed_something = True
        # left is free
        elif not square_left in clay_squares and not square_left in flowing_water and not square_left in still_water:
            if not square_below in flowing_water:
                flowing_water.add(square_left)
                changed_something = True  
        # nothing is free
        else: 
            if not square_below in flowing_water:
                is_caught, clay_left, clay_right = water_is_caught(stream[0], stream[1])
                if is_caught:
                    for x in range(clay_left+1, clay_right):
                        still_water.add((stream[0], x))
                        if (stream[0], x) in flowing_water: flowing_water.remove((stream[0], x))
                    changed_something = True

flowing_water.remove((min_y-1, 500))
print('Number of squares reached:', len(flowing_water) + len(still_water))

# Task 2
print('Amount of water in aquifers:', len(still_water))