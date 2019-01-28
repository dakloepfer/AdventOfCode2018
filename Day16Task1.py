
def addr(initial_registers, command):
    output = initial_registers.copy()
    output[command[3]] = initial_registers[command[1]] + initial_registers[command[2]]

    return output

def addi(initial_registers, command):
    output = initial_registers.copy()
    output[command[3]] = initial_registers[command[1]] + command[2]

    return output

def mulr(initial_registers, command):
    output = initial_registers.copy()
    output[command[3]] = initial_registers[command[1]] * initial_registers[command[2]]

    return output

def muli(initial_registers, command):
    output = initial_registers.copy()
    output[command[3]] = initial_registers[command[1]] * command[2]

    return output

def banr(initial_registers, command):
    output = initial_registers.copy()
    output[command[3]] = initial_registers[command[1]] & initial_registers[command[2]]

    return output

def bani(initial_registers, command):
    output = initial_registers.copy()
    output[command[3]] = initial_registers[command[1]] & command[2]

    return output

def borr(initial_registers, command):
    output = initial_registers.copy()
    output[command[3]] = initial_registers[command[1]] | initial_registers[command[2]]

    return output

def bori(initial_registers, command):
    output = initial_registers.copy()
    output[command[3]] = initial_registers[command[1]] | command[2]

    return output

def setr(initial_registers, command):
    output = initial_registers.copy()
    output[command[3]] = initial_registers[command[1]]

    return output

def seti(initial_registers, command):
    output = initial_registers.copy()
    output[command[3]] = command[1]

    return output

def gtir(initial_registers, command):
    output = initial_registers.copy()
    if command[1] > initial_registers[command[2]]:
        output[command[3]] = 1
    else:
        output[command[3]] = 0

    return output

def gtri(initial_registers, command):
    output = initial_registers.copy()
    if initial_registers[command[1]] > command[2]:
        output[command[3]] = 1
    else:
        output[command[3]] = 0

    return output
  
def gtrr(initial_registers, command):
    output = initial_registers.copy()
    if initial_registers[command[1]] > initial_registers[command[2]]:
        output[command[3]] = 1
    else:
        output[command[3]] = 0

    return output

def eqir(initial_registers, command):
    output = initial_registers.copy()
    if command[1] == initial_registers[command[2]]:
        output[command[3]] = 1
    else:
        output[command[3]] = 0

    return output

def eqri(initial_registers, command):
    output = initial_registers.copy()
    if initial_registers[command[1]] == command[2]:
        output[command[3]] = 1
    else:
        output[command[3]] = 0

    return output
  
def eqrr(initial_registers, command):
    output = initial_registers.copy()
    if initial_registers[command[1]] == initial_registers[command[2]]:
        output[command[3]] = 1
    else:
        output[command[3]] = 0

    return output
  
operations = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

with open("/Users/DominikKloepfer/Documents/workspace/Personal_Projects/Advent of Code 2018/Day 16/day16_input1.txt") as input: 
    data = [line.strip() for line in input]

samples = []
i = 0
while i < len(data):
    sample = []
    if len(data[i]) == 0: i+=1
    elif data[i][0] == 'B':
        initial_state = data[i].replace(']', '').replace(', ', '').split('[')
        initial_state = [int(i) for i in initial_state[1]]
        sample.append(initial_state)

        command = data[i+1].strip().split(' ')
        command = [int(c) for c in command]
        sample.append(command)

        output_state = data[i+2].replace(']', '').replace(', ', '').split('[')
        output_state = [int(o) for o in output_state[1]]

        sample.append(output_state)

        i += 3
        samples.append(sample)
    else: i+=1

print(samples[0:3])
number_more_than_three = 0

for sample in samples:
    outputs = [fn(sample[0], sample[1]) == sample[2] for fn in operations]
    if sum(outputs) >= 3: number_more_than_three += 1
    
print(number_more_than_three)