
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
  
functions = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

with open("/Users/DominikKloepfer/Documents/workspace/Personal_Projects/Advent of Code 2018/Day 16/day16_input2.txt") as input: 
    data = [line.strip() for line in input]

samples = [[] for i in range(16)]
line = 0
while line < len(data):
    if data[line] == '' and data[line+1] == '': break
    sample = []
    if len(data[line]) == 0: line+=1
    elif data[line][0] == 'B':
        initial_state = data[line].replace(']', '').replace(', ', '').split('[')
        initial_state = [int(i) for i in initial_state[1]]
        sample.append(initial_state)

        command = data[line+1].strip().split(' ')
        command = [int(c) for c in command]
        sample.append(command)

        output_state = data[line+2].replace(']', '').replace(', ', '').split('[')
        output_state = [int(o) for o in output_state[1]]

        sample.append(output_state)

        line += 3
        samples[command[0]].append(sample)
    else: line+=1

operations = [0 for j in range(len(functions))]
possible_functions = [0 for j in range(len(functions))]
for code in range(len(samples)):
    sample_results = []
    for sample in samples[code]:
        working_functions = []
        for fn in functions:

            if fn(sample[0], sample[1]) == sample[2]:
                working_functions.append(fn)
        sample_results.append(0)
        sample_results[-1] = working_functions
    

    correct_function = set(sample_results[0])
    for sr in sample_results:
        correct_function.intersection_update(sr)
    possible_functions[code] = list(correct_function)

operations_found = 0
while operations_found < len(operations):
    for code in range(len(operations)):
        if len(possible_functions[code]) == 1:
            operations[code] = possible_functions[code][0]
            operations_found += 1

            for pf in possible_functions:
                if operations[code] in pf:
                    pf = pf.remove(operations[code])
            
            break

register_state  = [0, 0, 0, 0]
while line < len(data):
    if data[line] == '': 
        line += 1 
        continue
    
    command = data[line].strip().split(' ')
    command = [int(c) for c in command]

    register_state = operations[command[0]](register_state, command)
    line += 1

print(register_state)