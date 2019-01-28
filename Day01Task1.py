
with open("/Users/DominikKloepfer/Documents/workspace/Personal_Projects/Advent of Code 2018/Day 1/day1_input1.txt") as input: 
    changes = [int(line.strip()) for line in input]

print(sum(changes))