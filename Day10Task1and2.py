# OCR libraries do not perform well on the kind of low resolution 'images the points create and doing a lot of 
# preprocessing would be quite complicated, so I'll just print them out at each second and read the message myself

import re
import time

def computeNextState(point_states):
    for point in point_states:
        point[0] += point[2]
        point[1] += point[3]
    return point_states

def printImage(point_states, second):
    max_x = max(point_states)[0]
    min_x = min(point_states)[0]
    max_y = max(point_states, key=lambda x: x[1])[1]
    min_y = min(point_states, key=lambda x: x[1])[1]

    # states = sorted(point_states, key=lambda x: (x[1], x[0]) )
    
    if max_x - min_x < 200:
        strings = ["." * (max_x-min_x +1)for l in range(min_y, max_y+1)]

        for state in point_states:
            strings[state[1]-min_y] = strings[state[1]-min_y][0:state[0]-min_x] + '#' + strings[state[1]-min_y][state[0]+1-min_x:]

        print('second', second) # needed for Task 2
        for line in strings:
            print(line)
        input('Press ENTER to continue')

with open("/Users/DominikKloepfer/Documents/workspace/Personal_Projects/Advent of Code 2018/Day 10/day10_input1.txt") as data: 
    point_states = [line.strip() for line in data]

for p in range(0, len(point_states)):
    point = re.split('<|, |>', point_states[p])
    point_states[p] = [int(point[1].strip()), int(point[2].strip()), int(point[4].strip()), int(point[5].strip())]

second = 0
while True: # need to stop computation manually
    second += 1
    point_states = computeNextState(point_states)

    printImage(point_states, second)
