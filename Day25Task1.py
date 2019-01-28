
def depth_first_search(starting_point):
    global remaining_points
    explore_order = []
    explore_order.append(starting_point)

    while len(explore_order) > 0:
        v = explore_order.pop()
        remaining_points.remove(v)

        for point in remaining_points:
            if point not in explore_order and sum([abs(v[i]-point[i]) for i in range(len(point))]) <= 3:
                explore_order.append(point)



with open("/Users/DominikKloepfer/Documents/workspace/Personal_Projects/Advent of Code 2018/Day 25/day25_input1.txt") as input: 
    data = [line.strip().split(',') for line in input]

remaining_points = [[int(coord) for coord in point] for point in data]

n_constellations = 0

while len(remaining_points) > 0:
    depth_first_search(remaining_points[0])
    n_constellations += 1

print(n_constellations)
