import re
from statistics import mean 

def getDistance(coords1, coords2):
    return abs(coords1[0]-coords2[0]) + abs(coords1[1]-coords2[1]) + abs(coords1[2]-coords2[2])

with open("/Users/DominikKloepfer/Documents/workspace/Personal_Projects/Advent of Code 2018/Day 23/day23_input1.txt") as input: 
    data = [line.strip() for line in input]

nanobots = []

for l in data:
    bot = re.split('<|,|>|r=', l)
    bot = [int(bot[6]), int(bot[1]), int(bot[2]), int(bot[3])]
    nanobots.append(bot)

# This algorithm is correct, but takes far too long as can be seen by the rough calculation of 
# the order of the number of points to test around even one nanobot: 
# n_points ~ mean(radii)*mean(radii)*mean(radii) ~ 4E23

max_x = max(nanobots, key=lambda x: x[1])[1]
min_x = min(nanobots, key=lambda x: x[1])[1]
max_y = max(nanobots, key=lambda x: x[2])[2]
min_y = min(nanobots, key=lambda x: x[2])[2]
max_z = max(nanobots, key=lambda x: x[3])[3]
min_z = min(nanobots, key=lambda x: x[3])[3]

print(max_x - min_x, max_y - min_y, max_z - min_z)
radii = [bot[0] for bot in nanobots]

print(mean(radii))    
print(mean(radii) * mean(radii) * 1000)

checked_points = set()
max_number_in_range = 0
points_with_max_in_range = set()
point = 0
for bot in nanobots:
    radius = bot[0]
    x_pos = bot[1]
    y_pos = bot[2]
    z_pos = bot[3]

    for x in range(x_pos - radius, x_pos + radius +1):
        for y in range(y_pos - radius + x, y_pos + radius + 1 - x):
            for z in range(z_pos - radius + x + y, z_pos + radius + 1 - x - y):
                point += 1
                if point%10000 == 0: print(point)
                if (x, y, z) in checked_points: continue
                
                checked_points.add((x, y, z))
                n_in_range = 0
                for bot2 in nanobots: 
                    if getDistance([x, y, z], bot2[1:]) <= bot2[0]:
                        n_in_range += 1
                if n_in_range > max_number_in_range: 
                    max_number_in_range = n_in_range
                    points_with_max_in_range = set((x, y, z))
                elif n_in_range == max_number_in_range:
                    points_with_max_in_range.add((x, y, z))

print('all points with the maximum bots in range:',points_with_max_in_range)
max_in_range_distances = [getDistance([0,0,0], coords) for coords in points_with_max_in_range]
print('minimum distance from origin:', min(max_in_range_distances))