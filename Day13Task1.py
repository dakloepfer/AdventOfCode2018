# In this task speed probably isn't too much of an issue

# carts are a list of lists, each list is [y, x, direction facing, number of intersections seen]
# direction_facing is 0 for left, 1 for up, 2 for right, 3 for down

# store the tracks as a list of lists where for each coordinate we store '-', '|', '+', '/' or '\'

from operator import itemgetter

def moveCarts(carts, tracks):
    for c in range(0, len(carts)):
        cart = carts[c]
        # move cart
        if cart[2] == 0:
            cart[1] -= 1
        elif cart[2] == 2:
            cart[1] += 1
        elif cart[2] == 1:
            cart[0] -= 1
        elif cart[2] == 3:
            cart[0] += 1

        row = cart[0]
        column = cart[1]
        track = tracks[row][column]
        if track == '/': 
            if cart[2] % 2 == 1: cart[2] = (cart[2] +1) % 4
            else: cart[2] = (cart[2] -1) % 4 
        elif track == '\\': 
            if cart[2] % 2 == 1: cart[2] = (cart[2] -1) % 4
            else: cart[2] = (cart[2] +1) % 4 
        elif track == '+': 
            if cart[3] == 0: cart[2] = (cart[2] -1) % 4
            elif cart[3] == 2: cart[2] = (cart[2] +1) % 4
            cart[3] = (cart[3] +1) % 3

        carts[c] = cart
        
        # check for collision
        for c2 in range(0, len(carts)):
            if c2 == c: continue
            
            if cart[0] == carts[c2][0] and cart[1] == carts[c2][1]:
                print('Collision!')
                print('x', cart[1], 'y', cart[0])
                return []

    return sorted(carts, key=itemgetter(0,1))

with open("/Users/DominikKloepfer/Documents/workspace/Personal_Projects/Advent of Code 2018/Day 13/day13_input1.txt") as input: 
    data = [line.replace('\n', '') for line in input]

carts = []
tracks = []

for r in range(0, len(data)):
    row = []
    for c in range(0, len(data[r])):
        if data[r][c] == '<': 
            row.append('-') # luckily initially tracks are neither on intersections nor curves
            carts.append([r, c, 0, 0])
        elif data[r][c] == '>':
            row.append('-')
            carts.append([r, c, 2, 0])
        elif data[r][c] == '^':
            row.append('|')
            carts.append([r, c, 1, 0])
        elif data[r][c] == 'v': 
            row.append('|')
            carts.append([r, c, 3, 0])
        else:
            row.append(data[r][c])

    tracks.append(row)

i = 0
while not carts == []:
    carts = moveCarts(carts, tracks)
    i+=1
print(i)
