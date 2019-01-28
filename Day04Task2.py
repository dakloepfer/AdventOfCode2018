from dateutil.parser import parse as parsedate
import datetime

with open("/Users/DominikKloepfer/Documents/workspace/Personal_Projects/Advent of Code 2018/Day 4/day4_input1.txt") as input: 
    rawlogs = [line.strip() for line in input]

logs = []

for l in range(0, len(rawlogs)): 
    logs.append([parsedate(rawlogs[l][1:17]), rawlogs[l][19::]])

def getDate(tupel):
    return tupel[0]

logs.sort(key=getDate)
sleep_patterns = {}
awake = True
current_guard = 0

for l in range(0, len(logs)):
    log = logs[l]

    if log[1][6] == '#':
        if not awake: 
            print('Guard did not wake up')
            for m in range(logs[l-1][0].minute, 60): # I don't care what happens to the guard after 1am, so stop counting then
                sleep_patterns[current_guard][m] += 1

        current_guard = int(log[1].split(' ')[1][1::])
        if not current_guard in sleep_patterns:
            sleep_patterns[current_guard] = [0 for i in range(0, 60)]
    elif log[1][0] == 'f':
        if not awake: raise Exception('Fell asleep while sleeping - is now one level closer to limbo') 
        awake = False
    else: 
        if awake: 
            print(logs[l-1])
            print(log)
            raise Exception('Guard has awoken from being awake - he now sees the truth')
       
        awake = True
        for m in range(logs[l-1][0].minute, log[0].minute):
            sleep_patterns[current_guard][m] += 1

sleepiest_guard = 0
max_number_of_sleeps = -1
for guard in sleep_patterns:
    guard_max = max(sleep_patterns[guard])
    if guard_max > max_number_of_sleeps:
        sleepiest_guard = guard
        max_number_of_sleeps = guard_max

print(sleepiest_guard)
print(sleep_patterns[sleepiest_guard].index(max_number_of_sleeps))
print(sleepiest_guard * sleep_patterns[sleepiest_guard].index(max_number_of_sleeps))