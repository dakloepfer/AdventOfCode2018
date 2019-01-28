
class worker: 
    def __init__(self):
        self.current_task = ''
        self.finish_time = 0



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

workers = [worker() for w in range(0, 5)]

proper_time = -1
steps_to_do = len(steps)

while steps_to_do > 0:
    next_finish = 100000
    for worker in workers: 
        if worker.finish_time > proper_time and worker.finish_time < next_finish:
            next_finish = worker.finish_time
    proper_time = next_finish

    for worker in workers: 
        if worker.finish_time == proper_time and worker.current_task != '': 
            
            for successor in steps[worker.current_task][1]:
                steps[successor][0].remove(worker.current_task)
            steps_to_do -= 1

    i = 0
    while i < len(steps):
        step = sorted(steps.keys())[i]
        if steps[step][0] == [] and not all(worker.finish_time > proper_time for worker in workers):
            print(step, proper_time + 60 + i +1)
            # assign step
            for worker in workers:
                if worker.finish_time <= proper_time:
                    worker.current_task = step
                    worker.finish_time = proper_time + 60 + i+1
                    break

            steps[step][0] = ['Done']
            i = -1 # returns to beginning of steps
            
        i += 1

print(proper_time)