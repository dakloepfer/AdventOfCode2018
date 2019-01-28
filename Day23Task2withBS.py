import re

#### The BS stands for 'Binary Search'

with open("/Users/DominikKloepfer/Documents/workspace/Personal_Projects/Advent of Code 2018/Day 23/day23_input1.txt") as input: 
    data = [line.strip() for line in input]

nanobots = []

for l in data:
    bot = re.split('<|,|>|r=', l)
    bot = [int(bot[6]), int(bot[1]), int(bot[2]), int(bot[3])]
    nanobots.append(bot)

# This isn't working for every input but only if the nanobot cubes are is sufficiently overlapping
# The algorithm counts the number of bots in range of increasingly fine-grained test points and 
# restricts itself to the cube around the test point with the most bots in range.
# This assumes that the cube around the test point with the most bots in range also contains the
# correct global maximum, which is more likely if the range cubes around each bot heavily overlap.
# For my input this gives the correct answer, if we want to be more certain we can do a ternary 
# subdivision instead of a binary one or zoom into the two (not one) test point cubes 
# with the most bots in range.

xs = [x[1] for x in nanobots] + [0]
ys = [x[2] for x in nanobots] + [0]
zs = [x[3] for x in nanobots] + [0]
size = 1
while size < max(xs) - min(xs):
    size *= 2
while True:
    print(size)
    target_count = 0
    best_point = None
    best_val = None
    for x in range(min(xs), max(xs) + 1, size):
        for y in range(min(ys), max(ys) + 1, size):
            for z in range(min(zs), max(zs) + 1, size):
                count = 0
                for radius, bx, by, bz in nanobots:
                    if size == 1:
                        calc = abs(x - bx) + abs(y - by) + abs(z - bz)
                        if calc <= radius:
                            count += 1
                    else:
                        calc = abs(x // size - bx // size) + abs(y // size - by // size) + abs(z // size - bz // size)
                        if calc - 1 <= radius // size:
                            count += 1
                if count > target_count:
                    target_count = count
                    best_val = abs(x) + abs(y) + abs(z)
                    best_point = (x, y, z)
                elif count == target_count:
                    if best_val is None or abs(x) + abs(y) + abs(z) < best_val:
                        best_val = abs(x) + abs(y) + abs(z)
                        best_point = (x, y, z)
    if size == 1:
        print("The max count I found was: " + str(target_count))
        print(best_val)
        break
    else:
        xs = [best_point[0] - size, best_point[0] + size]
        ys = [best_point[1] - size, best_point[1] + size]
        zs = [best_point[2] - size, best_point[2] + size]
        size = size // 2