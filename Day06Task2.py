from math import ceil, floor

with open("/Users/DominikKloepfer/Documents/workspace/Personal_Projects/Advent of Code 2018/Day 6/day6_input1.txt") as input: 
    coordinates = [[int(c) for c in line.strip().split(', ')] for line in input]

# do a naive algorithm by going through every point within a rectangle that should include all positives 
max_x = -10000
min_x = 10000000
max_y = -10000
min_y = 1000000
for c in coordinates: 
    if c[0] > max_x:
        max_x = c[0]
    if c[0] < min_x:
        min_x = c[0]
    if c[1] > max_y:
        max_y = c[1]
    if c[1] < min_y:
        min_y = c[1]

# these should be enough for the input given 
# some more complicated tighter bounds can be computed but this should be enough
upper_x = ceil((10000) / len(coordinates)) + max_x
lower_x = floor((-10000)/ len(coordinates)) - min_x
upper_y = ceil((10000)/len(coordinates)) + max_y
lower_y = floor((-10000)/len(coordinates)) - min_y
print(upper_x, upper_y, lower_x, lower_y)

area = 0
for x in range(lower_x, upper_x+1):
    for y in range(lower_y, upper_y+1):
        i = 0
        total_distance = 0
        while total_distance <= 10000 and i < len(coordinates):
            c = coordinates[i]
            total_distance += abs(c[0]-x) + abs(c[1]-y)
            i  += 1
        if total_distance <= 10000:
            area += 1

print(area)


