from string import ascii_lowercase

with open("/Users/DominikKloepfer/Documents/workspace/Personal_Projects/Advent of Code 2018/Day 5/day5_input1.txt") as input: 
    original_polymer = [line.strip() for line in input][0]

def react(polymer):
    i = 0
    while i < len(polymer)-1:
        if polymer[i].lower() == polymer[i+1].lower() and polymer[i] != polymer[i+1]:
            polymer= polymer[0:i] + polymer[i+2::]
            if i > 0:
                i -= 1
            continue

        i += 1
    return polymer

lengths_removed_one = {}
print(len(original_polymer))
for letter in ascii_lowercase:
    reduced_polymer = original_polymer.replace(letter, '').replace(letter.upper(), '')
    lengths_removed_one[letter] = len(react(reduced_polymer))

min_length = 1000000
best_letter_to_remove = ''

for l in lengths_removed_one:
    if lengths_removed_one[l] < min_length:
        min_length = lengths_removed_one[l]
        best_letter_to_remove = l

print(min_length)
print(best_letter_to_remove)
