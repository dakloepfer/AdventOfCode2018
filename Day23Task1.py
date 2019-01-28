
import re

def getDistance(coords1, coords2):
    return abs(coords1[0]-coords2[0]) + abs(coords1[1]-coords2[1]) + abs(coords1[2]-coords2[2])

with open("/Users/DominikKloepfer/Documents/workspace/Personal_Projects/Advent of Code 2018/Day 23/day23_input1.txt") as input: 
    data = [line.strip() for line in input]

nanobots = []

for l in data:
    bot = re.split('<|,|>|r=', l)
    bot = [int(bot[6]), int(bot[1]), int(bot[2]), int(bot[3])]
    nanobots.append(bot)

nanobots.sort(reverse=True)

max_radius_nanobot = nanobots[0]
max_radius = max_radius_nanobot[0]

n_in_range = 0

for bot in nanobots:
    if getDistance(max_radius_nanobot[1:], bot[1:]) <= max_radius:
        n_in_range += 1

print('Number of nanobots in range of most powerful bot:', n_in_range)