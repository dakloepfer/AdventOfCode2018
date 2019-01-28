
with open("/Users/DominikKloepfer/Documents/workspace/Personal_Projects/Advent of Code 2018/Day 1/day1_input1.txt") as input: 
    changes = [int(line.strip()) for line in input]

seen_frequencies = set([]) # creates an empty set

current_frequency = 0
current_index = 0

while not current_frequency in seen_frequencies: 
    # might run into subtle bug if two hashes are the same which is however very unlikely here
    # and lookup operations in sets are supposedly much faster
    seen_frequencies.add(current_frequency)
    current_frequency += changes[current_index]
    current_index = (current_index + 1) % len(changes)

print(current_frequency)