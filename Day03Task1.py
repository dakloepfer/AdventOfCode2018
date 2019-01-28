import re

with open("/Users/DominikKloepfer/Documents/workspace/Personal_Projects/Advent of Code 2018/Day 3/day3_input1.txt") as input: 
    claims = [line.strip() for line in input]

# make claims into list containing lists of integers [left, top, width, height]
for c in range(0, len(claims)): 
    claim = re.split(' |,|: |x', claims[c])
    claims[c] = [int(claim[2]), int(claim[3]), int(claim[4]), int(claim[5])]


## do a quick and dirty algorithm, most likely not optimal: run through every square and check if it is used more than once
## but speed is not an issue here (aside from the speed with which I complete this challenge)
max_x = 0
max_y = 0
for c in claims: 
    if max_x<c[0] + c[2]:
        max_x = c[0]+c[2]    
    if max_y<c[1] + c[3]:
        max_y = c[1]+c[3]

fabric_dict = {i: 0 for i in range(0, (max_x+1)*(max_y+1))} # index the squares going from 0 to max_x*max_y
n_overused = 0

for claim in claims:
    for i in range(claim[1], claim[1]+claim[3]):
        for j in range(claim[0], claim[0] + claim[2]):
            if fabric_dict[i*max_x + j] == 1:
                n_overused += 1
            fabric_dict[i*max_x + j] += 1
            
print(n_overused)