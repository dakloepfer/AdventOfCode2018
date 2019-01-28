# speed is not very much an issue in this challenge

import math
from operator import itemgetter, attrgetter
import sys

def adjacent_fields(row, column, vertices):
    # returns all available fields adjacent to field (row, column)
    adjacents = []
    for vertex in vertices:
        if row == vertex[0]:
            if column == vertex[1] +1: adjacents.append(vertex)
            elif column == vertex[1] -1: adjacents.append(vertex)
        elif column == vertex[1]:
            if row == vertex[0] +1: adjacents.append(vertex)
            elif row == vertex[0] -1: adjacents.append(vertex)

    return adjacents


class Combatant:

    def __init__(self, row, column, hp, attack_power, elf):

        self.row = row
        self.column = column
        self.hp = hp
        self.attack_power = attack_power
        self.elf = elf # True for elves, False for goblins

    def Dijkstra(self, free_fields):
        vertices_to_do = set()
        vertices_to_do.add((self.row, self.column, 0, None))
        vertices = []
        for field in free_fields:
            vertices_to_do.add((field[0], field[1], math.inf, None)) # row, column, distance, previous
        
        while len(vertices_to_do) > 0:
            u = sorted(sorted(vertices_to_do, key=itemgetter(2, 0, 1)), key=lambda x: x[2])[0]
            
            vertices.append(u)
            vertices_to_do.remove(u)

            for field in adjacent_fields(u[0], u[1], sorted(vertices_to_do, key=itemgetter(2, 0, 1))):
                alt = u[2] + 1
                if field[2] > alt:
                    vertices_to_do.remove(field)
                    vertices_to_do.add((field[0], field[1], alt, (u[0], u[1])))
            
        return vertices

    def get_enemies_in_range(self, enemies):
        result = []
        for enemy in enemies:
            if (abs(self.row - enemy.row) == 1 and self.column == enemy.column) or (self.row == enemy.row and abs(self.column - enemy.column) == 1):
                result.append(enemy)

        return result

    def fight(self, enemies, enemies_in_range, free_fields):
        attack_order = sorted(enemies_in_range, key= lambda enemy: enemy.hp)

        attack_index = enemies.index(attack_order[0])
        
        enemies[attack_index].hp -= self.attack_power
        if enemies[attack_index].hp <= 0:
            free_fields.append([enemies[attack_index].row, enemies[attack_index].column])
            enemies.pop(attack_index)
        
        return enemies, sorted(free_fields, key=itemgetter(0,1))

    def move(self, enemies, free_fields):

        vertices = sorted(self.Dijkstra(free_fields), key=itemgetter(2, 0, 1))
        fields_near_enemy = []
        for enemy in enemies:
            fields_near_enemy = fields_near_enemy + adjacent_fields(enemy.row, enemy.column, free_fields)

        if len(fields_near_enemy) == 0: return free_fields

        for vertex in vertices:
            for field in fields_near_enemy:

                if field[0] == vertex[0] and field[1] == vertex[1]:
                    v = vertex
                    previous = v[3]
                    if vertex[2] == math.inf:
                        return free_fields

                    while not (previous[0] == self.row and previous[1] == self.column):
                        for w in vertices:
                            if w[0:2] == previous:
                                v = w
                                break
                        previous = v[3]

                    free_fields.append([self.row, self.column])
                    self.row = v[0]
                    self.column = v[1]
                    free_fields.remove([v[0], v[1]])

                    return sorted(free_fields, key=itemgetter(0,1))
                

    def take_turn(self, enemies, free_fields):

        enemies_in_range = self.get_enemies_in_range(enemies)
        
        if not len(enemies_in_range) == 0:
            enemies, free_fields = self.fight(enemies, enemies_in_range, free_fields)
            return enemies, free_fields
        
        free_fields = self.move(enemies, free_fields)

        enemies_in_range = self.get_enemies_in_range(enemies)

        if not len(enemies_in_range) == 0:
            enemies, free_fields = self.fight(enemies, enemies_in_range, free_fields)
        
        return enemies, free_fields


def make_battle(data, elf_attack_power):

    print('elf attack power:', elf_attack_power)
    elves = []
    goblins = []
    free_fields = []

    for row in range(len(data)):
        for column in range(len(data[row])):
            if data[row][column] == '.':
                free_fields.append([row, column])
            elif data[row][column] == 'E':
                elves.append(Combatant(row, column, 200, elf_attack_power, True))
            elif data[row][column] == 'G':
                goblins.append(Combatant(row, column, 200, 3, False))

    all_combatants = sorted(elves + goblins, key=attrgetter('row', 'column'))
    
    n_elves = len(elves)

    turn = 0

    while len(elves) == n_elves:

        print(turn)
        all_combatants = sorted(all_combatants, key=attrgetter('row', 'column'))

        for c in range(len(all_combatants)):
            combatant = all_combatants[c]
            if combatant.hp <= 0: continue
            else:
                if combatant.elf:
                    goblins, free_fields = combatant.take_turn(goblins, free_fields)
                    goblins.sort(key=attrgetter('row', 'column'))
                else:
                    elves, free_fields = combatant.take_turn(elves, free_fields)
                    elves.sort(key=attrgetter('row', 'column'))



            if len(goblins) == 0:
                
                finished_turn = True
                for d in range(c+1, len(all_combatants)):
                    if all_combatants[d].hp > 0: 
                        finished_turn = False
                        break
                if finished_turn: turn += 1

                total_hp_left = sum([survivor.hp for survivor in elves])
                print('Outcome:', total_hp_left * turn)
                print('elf attack power:', elf_attack_power)
                for e in elves:
                    print('elf', e.row, e.column, e.hp)

                return True, total_hp_left * turn

        turn += 1

    return False, -1

with open("/Users/DominikKloepfer/Documents/workspace/Personal_Projects/Advent of Code 2018/Day 15/day15_input1.txt") as input: 
    data = [line.strip() for line in input]

max_elf_attack_power = 4 # should be enough
min_elf_attack_power = 3 # is not enough

# find upper bound

elves_survived = False
while not elves_survived:
    elves_survived, last_outcome = make_battle(data, max_elf_attack_power)
    if not elves_survived: 
        min_elf_attack_power = max_elf_attack_power
        max_elf_attack_power *= 2

# refine upper bound
last_max_outcome = 0
print('Refining upper bound')
while max_elf_attack_power - min_elf_attack_power > 1:
    elf_attack_power = int(math.ceil(max_elf_attack_power *0.5 + min_elf_attack_power * 0.5))
    if elf_attack_power == min_elf_attack_power:
        elf_attack_power += 1

    elves_survived, last_outcome = make_battle(data, elf_attack_power)
    if elves_survived:
        max_elf_attack_power = elf_attack_power
        last_max_outcome = last_outcome
    else:
        min_elf_attack_power = elf_attack_power

print('Attack power needed:', max_elf_attack_power)
print('Outcome for that power:', last_max_outcome)
