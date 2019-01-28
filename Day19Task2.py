
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

with open("/Users/DominikKloepfer/Documents/workspace/Personal_Projects/Advent of Code 2018/Day 19/day19_input1.txt") as input: 
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

register_state = [1, 0, 0, 0, 0, 0]

turn = 0
while ip_value < len(commands) and ip_value > -1:
    register_state[instruction_pointer] = ip_value

    current_command = commands[ip_value]
    operations[current_command[0]](current_command[1])
    
    
    print(ip_value, register_state, current_command)
    ip_value = register_state[instruction_pointer] + 1 

    if turn > 50: break # tells prints out the beginning of the computation
    turn += 1
print(register_state)

# By investigating the commands in the loop the computation gets caught in, one can see that
# the value in register5 gets added to register0 if register5 * register2 = register4 = 10551378
# Then the value in register5 gets incremented by 1 and it again loops through increasing values of 
# register2 until that is larger than the value in register4. 
# If the value in register5 is larger than the value in register4, we square the value in register3,
# which has the effect of halting the program (register3 is then at like 14)
# ==> register 0 contains sum of all factors of 10551378 when the program halts

final_reg0_value = 0
large_number = register_state[4]
for val in range(1, large_number+1):
    if large_number % val == 0:
        final_reg0_value += val
        print(val)
print('Register 0 ends with sum of all factors of %d: reg0 = %d' %(large_number, final_reg0_value))