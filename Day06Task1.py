
with open("/Users/DominikKloepfer/Documents/workspace/Personal_Projects/Advent of Code 2018/Day 6/day6_input1.txt") as input: 
    coordinates = [[int(c) for c in line.strip().split(', ')] for line in input]


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

coordinate_areas = {i: 0 for i in range(0, len(coordinates))}
coordinate_areas[-1] = 0

for x in range(min_x, max_x+1):
    for y in range(min_y, max_y+1):
        min_distance = 100000000
        corresponding_coordinate = -1
        for i in range(0, len(coordinates)):
            c = coordinates[i]
            if abs(c[0]-x) + abs(c[1]-y) < min_distance:
                min_distance = abs(c[0]-x) + abs(c[1]-y)
                corresponding_coordinate = i
            elif abs(c[0]-x) + abs(c[1]-y) == min_distance:
                corresponding_coordinate = -1
        coordinate_areas[corresponding_coordinate] += 1

# now delete all the infinte areas by considering the border of the (min_x, min_y, max_x, max_y) rectangle
for x in range(min_x-1, max_x+2):
    for y in [min_y-1, max_y +2]:
        min_distance = 100000000
        corresponding_coordinate = -1
        for i in coordinate_areas:
            c = coordinates[i]
            if abs(c[0]-x) + abs(c[1]-y) < min_distance:
                min_distance = abs(c[0]-x) + abs(c[1]-y)
                corresponding_coordinate = i
            elif abs(c[0]-x) + abs(c[1]-y) == min_distance:
                corresponding_coordinate = -1
        coordinate_areas[corresponding_coordinate] = -1


for y in range(min_y-1, max_y+2):
    for x in [min_x-1, max_x +2]:
        min_distance = 100000000
        corresponding_coordinate = -1
        for i in coordinate_areas:
            c = coordinates[i]
            if abs(c[0]-x) + abs(c[1]-y) < min_distance:
                min_distance = abs(c[0]-x) + abs(c[1]-y)
                corresponding_coordinate = i
            elif abs(c[0]-x) + abs(c[1]-y) == min_distance:
                corresponding_coordinate = -1
        coordinate_areas[corresponding_coordinate] = -1

max_area = -1

for i in coordinate_areas:
    if coordinate_areas[i] > max_area:
        max_area = coordinate_areas[i]

print(max_area)