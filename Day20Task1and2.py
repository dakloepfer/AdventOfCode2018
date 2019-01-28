import math
# store rooms in a dictionary: key is a tuple with their coordinates, value is a set of tuples
# with the coordinates of rooms they lead to 

# probably best to solve the regex recursively - if I encounter an open parenthesis, find the 
# closing parenthesis and the | on the correct level (do that in the same pass probably) and 
# then loop through all the options - returning the coordinate each option ends on. 
# Put these ending coordinates in a set, loop through those and do all the remaining steps from 
# before

# at the very end run Dijkstra to find room furthest away

# Coordinates are (row, column)


def Dijkstra(map, starting_coords):
    distances = {}
    to_look_at = []
    for key in map:
        if key == starting_coords:
            to_look_at.append([starting_coords, 0])
        else:
            to_look_at.append([key, math.inf])

    while len(to_look_at) > 0:

        to_look_at.sort(key=lambda x: x[1], reverse=True)
        u = to_look_at.pop()
        distances[u[0]] = u[1]
        for neighbour in map[u[0]]:
            alt = u[1] + 1
            for n in to_look_at:
                if n[0] == neighbour:
                    if alt < n[1]:
                        n[1] = alt
                    else:
                        break

    return distances

def find_closing_paren(string, open_paren_index):
    index = open_paren_index+1
    option_delims = []
    
    net_open_parens = 1

    while net_open_parens > 0:
        if string[index] == '(':
            net_open_parens += 1
        elif string[index] == ')':
            net_open_parens -= 1
        elif string[index] == '|' and net_open_parens == 1:      
            option_delims.append(index)
        index += 1
    closing_paren = index-1

    return closing_paren, option_delims

def parse_regex(starting_coords, regex):
    global map
    # there might be multiple ending_coords depending on where any branches go to 
    # - might not be necessary for my input but is the more general solution
    ending_coords = set()
    current_coords = starting_coords
    new_coords = None

    for index, char in enumerate(regex):
        
        if char == '(':
            closing_paren, branch_delims = find_closing_paren(regex, index)
            branches = []
            branches.append(regex[index+1:branch_delims[0]])
            for j in range(0, len(branch_delims)-1):
                branches.append(regex[branch_delims[j]+1:branch_delims[j+1]])
            branches.append(regex[branch_delims[len(branch_delims)-1]+1:closing_paren])

            branch_ending_coords = set()
            for branch in branches:
                branch_ending_coords = branch_ending_coords | parse_regex(current_coords, branch)
            
            remaining_regex = regex[closing_paren+1:]
            for coord in branch_ending_coords:
                ending_coords = ending_coords | parse_regex(coord, remaining_regex)
            
            return ending_coords

        else:
            if char == 'N':
                new_coords = (current_coords[0]-1, current_coords[1])  
            elif char == 'S':
                new_coords = (current_coords[0]+1, current_coords[1])
            elif char == 'W':
                new_coords = (current_coords[0], current_coords[1]-1)
            elif char == 'E':
                new_coords = (current_coords[0], current_coords[1]+1)
            
            map[current_coords].add(new_coords)
            if new_coords in map:
                map[new_coords].add(current_coords)
            else:
                map[new_coords] = set()
                map[new_coords].add(current_coords)
        
            current_coords = new_coords

    ending_coords.add(current_coords)
        
    return ending_coords



with open("/Users/DominikKloepfer/Documents/workspace/Personal_Projects/Advent of Code 2018/Day 20/day20_input1.txt") as input: 
    regex = [line.strip() for line in input]

regex = regex[0]
regex = regex[1:len(regex)-1]
map = {}
map[(0,0)] = set()

parse_regex((0,0), regex)

distances = Dijkstra(map, (0,0))

# Task 1
max_d = 0
for d in distances: 
    if distances[d] > max_d: max_d = distances[d]

print('The most distant room is %d doors away' %(max_d))

# Task 2
n_at_least_1k = 0

for d in distances:
    if distances[d] >= 1000: n_at_least_1k += 1

print('There are %d rooms that are at least 1000 doors away' %(n_at_least_1k))

