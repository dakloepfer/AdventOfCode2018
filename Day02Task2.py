import sys

with open("/Users/DominikKloepfer/Documents/workspace/Personal_Projects/Advent of Code 2018/Day 2/day2_input1.txt") as input: 
    ids = [line.strip() for line in input]

# I'm just gonna brute force it
difference_index = -1
for i in range(0, len(ids)):
    for j in range(i+1, len(ids)):
        n_diff = 0
        for k in range(0, len(ids[i])):

            if ids[i][k] != ids[j][k]:
                n_diff += 1
                difference_index = k

        if n_diff == 1: 
            print(ids[i], ids[j])
            print(difference_index)
            print(ids[i][0:difference_index] + ids[i][difference_index+1::])
            sys.exit()
    
