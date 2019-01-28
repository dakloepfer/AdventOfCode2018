def addr(command):
    global register_state
    output = register_state.copy()
    output[command[2]] = register_state[command[0]] + register_state[command[1]]

    register_state =  output

def addi(command):
    global register_state
    output = register_state.copy()
    output[command[2]] = register_state[command[0]] + command[1]

    register_state =  output

def mulr(command):
    global register_state
    output = register_state.copy()
    output[command[2]] = register_state[command[0]] * register_state[command[1]]

    register_state =  output

def muli(command):
    global register_state
    output = register_state.copy()
    output[command[2]] = register_state[command[0]] * command[1]

    register_state =  output

def banr(command):
    global register_state
    output = register_state.copy()
    output[command[2]] = register_state[command[0]] & register_state[command[1]]

    register_state =  output

def bani(command):
    global register_state
    output = register_state.copy()
    output[command[2]] = register_state[command[0]] & command[1]

    register_state =  output

def borr(command):
    global register_state
    output = register_state.copy()
    output[command[2]] = register_state[command[0]] | register_state[command[1]]

    register_state =  output

def bori(command):
    global register_state
    output = register_state.copy()
    output[command[2]] = register_state[command[0]] | command[1]

    register_state =  output

def setr(command):
    global register_state
    output = register_state.copy()
    output[command[2]] = register_state[command[0]]

    register_state =  output

def seti(command):
    global register_state
    output = register_state.copy()
    output[command[2]] = command[0]

    register_state =  output

def gtir(command):
    global register_state
    output = register_state.copy()
    if command[0] > register_state[command[1]]:
        output[command[2]] = 1
    else:
        output[command[2]] = 0

    register_state =  output

def gtri(command):
    global register_state
    output = register_state.copy()
    if register_state[command[0]] > command[1]:
        output[command[2]] = 1
    else:
        output[command[2]] = 0

    register_state =  output
  
def gtrr(command):
    global register_state
    output = register_state.copy()
    if register_state[command[0]] > register_state[command[1]]:
        output[command[2]] = 1
    else:
        output[command[2]] = 0

    register_state =  output

def eqir(command):
    global register_state
    output = register_state.copy()
    if command[0] == register_state[command[1]]:
        output[command[2]] = 1
    else:
        output[command[2]] = 0

    register_state =  output

def eqri(command):
    global register_state
    output = register_state.copy()
    if register_state[command[0]] == command[1]:
        output[command[2]] = 1
    else:
        output[command[2]] = 0

    register_state =  output
  
def eqrr(command):
    global register_state
    output = register_state.copy()
    if register_state[command[0]] == register_state[command[1]]:
        output[command[2]] = 1
    else:
        output[command[2]] = 0

    register_state =  output

def ip(command):
    global instruction_pointer

    instruction_pointer = command[0]

operations = {
    "addr": addr,
    "addi": addi,
    "mulr": mulr,
    "muli": muli,
    "banr": banr, 
    "bani": bani,
    "borr": borr,
    "bori": bori,
    "setr": setr,
    "seti": seti,
    "gtir": gtir,
    "gtri": gtri,
    "gtrr": gtrr,
    "eqir": eqir,
    "eqri": eqri,
    "eqrr": eqrr
}

with open("/Users/DominikKloepfer/Documents/workspace/Personal_Projects/Advent of Code 2018/Day 21/day21_input1.txt") as input: 
    data = [line.strip() for line in input]

commands = []

instruction_pointer = 5
ip_value = 0

for c in data:
    command = c.split(' ')

    if command[0][0] == '#': 
        ip([int(command[1])])
    else:
        commands.append((command[0], [int(command[i]) for i in range(1, len(command))]))


register_state = [14535837, 0, 0, 0, 0, 0]

turn = 0
while ip_value < len(commands) and ip_value > -1:
    register_state[instruction_pointer] = ip_value

    current_command = commands[ip_value]
    operations[current_command[0]](current_command[1])
    

    
    ip_value = register_state[instruction_pointer] + 1 

    # command 28 is the only one involving the value of register0 - for it to do something different
    # this must evaluate to true (usually it is false) - so print out register1 the first time this 
    # command is reached
    if ip_value == 28: 
        print(register_state) 
        break

    turn += 1
    if turn % 1000 == 0: print(turn)

print(register_state)

