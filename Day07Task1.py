
with open("/Users/DominikKloepfer/Documents/workspace/Personal_Projects/Advent of Code 2018/Day 7/day7_input1.txt") as input: 
    conditions = [line.strip().split(' ') for line in input]

steps = {} # each key has value [[predecessors], [successors]]

for condition in conditions:
    if not condition[1] in steps: 
        steps[condition[1]] = [[], [condition[7]]]
    else: 
        steps[condition[1]][1].append(condition[7])

    if not condition[7] in steps:
        steps[condition[7]] = [[condition[1]], []]
    else:
        steps[condition[7]][0].append(condition[1])

order_of_steps = ''

while len(steps) > 0:
    for step in sorted(steps.keys()):
        if steps[step][0] == []:
            order_of_steps += step
            for successor in steps[step][1]:
                steps[successor][0].remove(step)
            del steps[step]
            break

print(order_of_steps)