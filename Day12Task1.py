import time
def computeNextState(state, rules, leftindex):
    new_state = [s for s in state]
    for i in range(2, len(state)-2):
        pattern = state[i-2] + state[i-1] + state[i] + state[i+1] + state[i+2]

        if pattern in rules:
            if rules[pattern]:
                new_state[i] = '#'
            else: 
                new_state[i] = '.'
        else: 
            new_state[i] = '.'


    if new_state.index('#') < 5:
        leftindex -= (5-new_state.index('#'))
        new_state = ['.' for i in range(0, 5-new_state.index('#'))] + new_state
    if new_state[::-1].index('#') < 5: # a bit wasteful but the list should not be too long so it should be fine
        new_state = new_state + ['.' for i in range(0, 5-new_state[::-1].index('#'))]

    return new_state, leftindex
    

with open("/Users/DominikKloepfer/Documents/workspace/Personal_Projects/Advent of Code 2018/Day 12/day12_input1.txt") as input: 
    data = [line for line in input]
    initial_state_raw = data[0]
    rules_raw = data[2:]

initial_state = '.....' + initial_state_raw.strip().split(' ')[2] + '.....'
initial_state = list(initial_state)
leftindex = -5
#initial_state = [True if pot == '#' else False for pot in initial_state_raw]


rules = {}
for rule_raw in rules_raw:
    rule = rule_raw.strip().split(' ')
    if rule[2] == '#':
        rules[rule[0]] = True
    else:
        rules[rule[0]] = False

state = initial_state
t1 = time.time()
for i in range(0, 2000):
    state, leftindex = computeNextState(state, rules, leftindex)

print(time.time()-t1)

sum = 0
for i in range(0, len(state)):
    if state[i] == '#':
        sum += i+leftindex

print(sum)

