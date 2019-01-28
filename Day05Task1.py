
with open("/Users/DominikKloepfer/Documents/workspace/Personal_Projects/Advent of Code 2018/Day 5/day5_input1.txt") as input: 
    polymer = [line.strip() for line in input][0]

print(len(polymer))

i = 0
while i < len(polymer)-1:
    if polymer[i].lower() == polymer[i+1].lower() and polymer[i] != polymer[i+1]:
        polymer= polymer[0:i] + polymer[i+2::]
        if i > 0:
            i -= 1
        continue

    i += 1

print(len(polymer))
