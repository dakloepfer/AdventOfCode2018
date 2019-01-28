# Need scores of the 10 recipes immediately after recipe 509671

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


recipe_scores = [3, 7]
elf1 = 0
elf2 = 1

scores_from_recipe = 509671

while len(recipe_scores) < scores_from_recipe + 10: 
    recipe_scores, elf1, elf2 = addNewRecipes(recipe_scores, elf1, elf2)

print(recipe_scores[scores_from_recipe:scores_from_recipe+10])