
with open("/Users/DominikKloepfer/Documents/workspace/Personal_Projects/Advent of Code 2018/Day 2/day2_input1.txt") as input: 
    ids = [line.strip() for line in input]

n_containing_two = 0
n_containing_three = 0

current_id_letter_dict = {}

for id in ids:
    seen_two = False
    seen_three = False
    current_id_letter_dict.clear()

    for letter in id:
        if letter in current_id_letter_dict:
            current_id_letter_dict[letter] += 1
        else:
            current_id_letter_dict[letter] = 1

    for letter in current_id_letter_dict: 
        if current_id_letter_dict[letter] == 2 and not seen_two:
            n_containing_two += 1
            seen_two = True
        if current_id_letter_dict[letter] == 3 and not seen_three:
            n_containing_three += 1
            seen_three = True

print(n_containing_three * n_containing_two)
