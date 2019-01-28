from operator import attrgetter
import re
import copy

class Unit:

    def __init__(self, army, n_units, hp, attack_damage, initiative, attack_type, weaknesses, immunities):

        self.army = army
        self.n_units = n_units
        self.hp = hp
        self.attack_damage = attack_damage
        self.initiative = initiative
        self.attack_type = attack_type
        self.weaknesses = weaknesses
        self.immunities = immunities
        self.has_attacker = False
        self.enemy_unit_chosen = None
        self.damage_dealt_per_unit = 0

    def effective_power(self):
        return self.n_units * self.attack_damage

    def select_target(self, all_units):
        max_damage_dealt = 1
        enemy_unit_chosen = None

        for enemy in all_units:

            if enemy.has_attacker or self.army == enemy.army: # every unit gets at most one attacker
                continue
            elif self.attack_type in enemy.weaknesses: 
                damage_dealt = 2 * self.n_units * self.attack_damage
            elif self.attack_type in enemy.immunities:
                damage_dealt = 0
            else:
                damage_dealt = self.n_units * self.attack_damage
            
            if damage_dealt > max_damage_dealt:
                max_damage_dealt = damage_dealt
                if enemy_unit_chosen: enemy_unit_chosen.has_attacker = False
                enemy_unit_chosen = enemy
                enemy_unit_chosen.has_attacker = True

            elif damage_dealt == max_damage_dealt:
                if not enemy_unit_chosen:
                    max_damage_dealt = damage_dealt
                    enemy_unit_chosen = enemy
                    enemy_unit_chosen.has_attacker = True

                elif enemy_unit_chosen.effective_power() < enemy.effective_power():
                    max_damage_dealt = damage_dealt
                    enemy_unit_chosen.has_attacker = False
                    enemy_unit_chosen = enemy
                    enemy_unit_chosen.has_attacker = True

                elif enemy_unit_chosen.effective_power() == enemy.effective_power():
                    if enemy.initiative > enemy_unit_chosen.initiative:
                        max_damage_dealt = damage_dealt
                        enemy_unit_chosen.has_attacker = False
                        enemy_unit_chosen = enemy
                        enemy_unit_chosen.has_attacker = True

        max_damage_dealt_per_unit = max_damage_dealt // self.n_units
        self.enemy_unit_chosen = enemy_unit_chosen
        self.damage_dealt_per_unit = max_damage_dealt_per_unit

    def getAttacked(self, damage):
        self.n_units = max(0, self.n_units - damage // self.hp)

    def attack(self, all_units):
        if self.enemy_unit_chosen:
            self.enemy_unit_chosen.getAttacked(self.damage_dealt_per_unit * self.n_units)
            self.enemy_unit_chosen.has_attacker = False
        self.enemy_unit_chosen = None
        self.damage_dealt_per_unit = 0

def fight_battle(all_units, armies_remaining_units):
    fight_over = False
    old_all_units = []
    while not fight_over:
        all_units.sort(key=lambda unit: (unit.effective_power(), unit.initiative), reverse=True)
        if old_all_units == [unit.n_units for unit in all_units]:
            return 'Infection', None
        else: 
            old_all_units = [unit.n_units for unit in all_units]
            
        # target selection
        for unit in all_units:
            unit.select_target(all_units)

        all_units.sort(key=attrgetter('initiative'), reverse=True)
        # attack
        for unit in all_units:
            unit.attack(all_units)

        index = len(all_units)-1

        while index >= 0:
            unit = all_units[index]
            if unit.n_units <= 0:
                armies_remaining_units[unit.army] -= 1
                all_units.pop(index)
            index -= 1

        for army in armies_remaining_units:
            if armies_remaining_units[army] == 0:
                fight_over = True
                break

    units_remaining = sum([unit.n_units for unit in all_units])
    winning_army = all_units[0].army
    return winning_army, units_remaining

def boost_one_army(all_units, boost, army_to_boost):
    new_all_units = copy.deepcopy(all_units)
    for unit in new_all_units:
        if unit.army == army_to_boost:
            unit.attack_damage += boost
    return new_all_units

with open("/Users/DominikKloepfer/Documents/workspace/Personal_Projects/Advent of Code 2018/Day 24/day24_input1.txt") as input: 
    data = [line.strip() for line in input]

armies_remaining_units = {} # dictionary of remaining units for every army
all_units = []

current_army = None
for line in data: 
    if line == '': continue
    
    if line[-1] == ':':
        current_army = line[0:len(line)-1]
        armies_remaining_units[current_army] = 0
    else:
        line2 = re.split('\(|\)', line)
        if len(line2) == 1:
            weaknesses_immunities = []
            attack_data = line2[0].split(' ')[6:]
        else:
            weaknesses_immunities = line2[1].split(' ')
            attack_data = line2[2].split(' ')

        words = line.replace('(', '').replace(')', '').split(' ')
        n_units = int(words[0])
        hp = int(words[4])
        initiative = int(words[-1])
        
        

        attack_damage = int(attack_data[6])
        attack_type = attack_data[7]

        weaknesses = []
        immunities = []
        i = 0
        while i < len(weaknesses_immunities):
            if weaknesses_immunities[i] == 'to':
                if weaknesses_immunities[i-1] == 'weak':
                    j = i+1
                    while j < len(weaknesses_immunities):
                        if weaknesses_immunities[j][-1] == ',':
                            weaknesses.append(weaknesses_immunities[j][:-1])
                            j += 1
                        elif weaknesses_immunities[j][-1] == ';':
                            weaknesses.append(weaknesses_immunities[j][:-1])
                            i = j
                            break
                        else:
                            weaknesses.append(weaknesses_immunities[j])
                            i = j
                            break

                elif weaknesses_immunities[i-1] == 'immune':
                    j = i+1
                    while j < len(weaknesses_immunities):
                        if weaknesses_immunities[j][-1] == ',':
                            immunities.append(weaknesses_immunities[j][:-1])
                            j += 1
                        elif weaknesses_immunities[j][-1] == ';':
                            immunities.append(weaknesses_immunities[j][:-1])
                            i = j
                            break
                        else:
                            immunities.append(weaknesses_immunities[j])
                            i = j
                            break

            i += 1
        all_units.append(Unit(current_army, n_units, hp, attack_damage, initiative, attack_type, weaknesses, immunities))
        armies_remaining_units[current_army] += 1
        #print(current_army, n_units, hp, weaknesses, immunities, attack_damage, attack_type, initiative)

print('done parsing')

max_too_small_boost = 0
min_large_enough_boost = 1

winning_army = 'Infection'

while winning_army == 'Infection':
    print('min large enough boost', min_large_enough_boost)
    current_all_units = boost_one_army(all_units, min_large_enough_boost, 'Immune System')
    current_armies_remaining_units = copy.deepcopy(armies_remaining_units)
    winning_army, _ = fight_battle(current_all_units, current_armies_remaining_units)
    
    max_too_small_boost = min_large_enough_boost
    min_large_enough_boost *= 2

min_large_enough_boost //= 2
max_too_small_boost //= 2

while min_large_enough_boost - max_too_small_boost > 1:
    boost = max_too_small_boost + (min_large_enough_boost - max_too_small_boost) // 2
    print('boost', boost, 'higher boost', min_large_enough_boost, 'lower boost', max_too_small_boost)

    current_all_units = boost_one_army(all_units, boost, 'Immune System')
    current_armies_remaining_units = copy.deepcopy(armies_remaining_units)
    winning_army, remaining_units = fight_battle(current_all_units, current_armies_remaining_units)
    print('winner', winning_army)
    if winning_army == 'Immune System':
        min_large_enough_boost = boost
    else:
        max_too_small_boost = boost

all_units = boost_one_army(all_units, min_large_enough_boost, 'Immune System')
_, remaining_units = fight_battle(all_units, armies_remaining_units)

print('With a boost of %d, Immune System wins with %d units remaining' %(min_large_enough_boost, remaining_units))
