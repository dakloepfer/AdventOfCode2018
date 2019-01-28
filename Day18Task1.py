# I need to use a list of lists to store the states of the fields, since there are 3 possible
# states - if there had been only 2 it would have been possible to use the binary
# representation of a long integer
# Lists are faster than sets here because I am iterating over all fields often

# encode open ground as 0, lumberyards as 1, trees as 2

def getNeighbours(row, column):
    global current_area

    n_open = 0
    n_lumber = 0
    n_trees = 0

    min_row = max([row-1, 0])
    min_col = max([column-1, 0])
    max_row = min([row+1, len(current_area)-1])
    max_col = min([column+1, len(current_area[0])-1])

    for r in range(min_row, max_row+1):
        for c in range(min_col, max_col+1):
            if current_area[r][c] == 0: n_open += 1
            elif current_area[r][c] == 1: n_lumber += 1
            else: n_trees += 1

    if current_area[row][column] == 0: n_open -= 1
    elif current_area[row][column] == 1: n_lumber -= 1
    else: n_trees -= 1

    return n_open, n_lumber, n_trees

def computeNext(row, column):
    global current_area

    n_open, n_lumber, n_trees = getNeighbours(row, column)

    current_type = current_area[row][column]

    if current_type == 0 and n_trees >= 3:
        return 2
    elif current_type == 2 and n_lumber >= 3:
        return 1
    elif current_type == 1 and (n_lumber < 1 or n_trees < 1):
        return 0
    else:
        return current_type

def computeOneMinute():
    global current_area

    new_area = [[-1 for j in range(len(current_area[0]))] for i in range(len(current_area))]

    for r in range(len(current_area)):
        for c in range(len(current_area[0])):
            new_area[r][c] = computeNext(r, c)

    current_area = new_area

def calculateResourceValue():
    global current_area
    n_lumber = 0
    n_trees = 0

    for r in range(len(current_area)):
        for c in range(len(current_area[0])):
            if current_area[r][c] == 1: n_lumber += 1
            elif current_area[r][c] == 2: n_trees += 1
            else: continue 
    
    return n_lumber*n_trees



with open("/Users/DominikKloepfer/Documents/workspace/Personal_Projects/Advent of Code 2018/Day 18/day18_input1.txt") as input: 
    data = [line.strip() for line in input]

current_area = []

for l in data:
    current_row = []
    for c in l:
        if c == '.':
            current_row.append(0)
        elif c == '#':
            current_row.append(1)
        elif c == '|':
            current_row.append(2)
        else: print('Unknown symbol')
    
    current_area.append(current_row)

for m in range(10):
    computeOneMinute()
print('Resource Value after 10 minutes', calculateResourceValue())