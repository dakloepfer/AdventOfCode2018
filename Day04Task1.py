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
        if not awake: # I don't care what happens to the guard after 1am, so stop counting then
            print('Guard did not wake up')
            sleep_patterns[current_guard] += datetime.datetime(log[0].year, log[1].month, log[2].day, 1, 0) - log[0]

        current_guard = int(log[1].split(' ')[1][1::])
        if not current_guard in sleep_patterns:
            sleep_patterns[current_guard] = 0
    elif log[1][0] == 'f':
        if not awake: raise Exception('Fell asleep while sleeping - is now one level closer to limbo') 
        awake = False
    else: 
        if awake: 
            print(logs[l-1])
            print(log)
            raise Exception('Guard has awoken from being awake - he now sees the truth')
       
        awake = True
        time_asleep = log[0] - logs[l-1][0]
        sleep_patterns[current_guard] +=  time_asleep.days * 24 * 60 + time_asleep.seconds / 60
        
max_sleep = -1
sleepiest_guard = 0
for guard  in sleep_patterns:
    if sleep_patterns[guard] > max_sleep:
        max_sleep = sleep_patterns[guard]
        sleepiest_guard = guard

# repeat some of the same code so I only need to do this computation for the sleepiest guard

awake = True
current_guard = 0
sleepy_minutes = [0 for i in range(0, 60)]

for l in range(0, len(logs)):
    log = logs[l]

    if log[1][6] == '#':
        if not awake and current_guard == sleepiest_guard: 
            print('Guard did not wake up')
            for m in range(logs[l-1][0].minute, 60):
                sleepy_minutes[m] += 1

        current_guard = int(log[1].split(' ')[1][1::])

    elif log[1][0] == 'f' and current_guard == sleepiest_guard:
        if not awake: raise Exception('Fell asleep while sleeping - is now one level closer to limbo') 
        awake = False
    elif current_guard == sleepiest_guard: 
        if awake: 
            print(logs[l-1])
            print(log)
            raise Exception('Guard has awoken from being awake - he now sees the truth')
       
        awake = True
        for m in range(logs[l-1][0].minute, log[0].minute):
            sleepy_minutes[m] += 1

print(sleepiest_guard)
print(sleepy_minutes.index(max(sleepy_minutes)))
print(sleepiest_guard * sleepy_minutes.index(max(sleepy_minutes)))