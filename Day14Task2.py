# Need number of recipes left of the first occurrence of sublist 509671
import time

def addNewRecipes(recipe_scores, elf1, elf2):
    elf1_score = recipe_scores[elf1]
    elf2_score = recipe_scores[elf2]
    total_score = elf1_score + elf2_score # maximum of 18

    if total_score < 10: recipe_scores.append(total_score)
    else: 
        recipe_scores.append(1)
        recipe_scores.append(total_score-10)
    
    elf1 = (elf1 + 1 + elf1_score) % len(recipe_scores)
    elf2 = (elf2 + 1 + elf2_score) % len(recipe_scores)

    return recipe_scores, elf1, elf2

input = '074501'

recipe_scores = [3, 7]
elf1 = 0
elf2 = 1

pattern = [int(digit) for digit in input]
t1 = time.time()

while True:
    recipe_scores, elf1, elf2 = addNewRecipes(recipe_scores, elf1, elf2)

    if recipe_scores[-len(pattern):] == pattern:
        print(len(recipe_scores)-len(pattern))
        break
    elif recipe_scores[-len(pattern)-1:-1] == pattern:
        print(len(recipe_scores)-len(pattern)-1)
        break

    if len(recipe_scores) %100000 == 0: print(len(recipe_scores))

print(time.time()-t1)
