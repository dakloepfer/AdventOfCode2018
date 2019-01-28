
import math
import time
import heapq

def calculate_types(target_row, target_column, cave_depth):
    rock_types = []
    erosion_levels = []

    # have to do some modulo computation when computing to avoid too large numbers
    for row in range(0, target_row+100):
        erosion_row = []
        type_row = []
        for column in range(0, target_column +100): # is hopefully enough
            if (row, column) == (0, 0):
                erosion_level = (0 + cave_depth) % 20183
                erosion_row.append(erosion_level)
            elif (row, column) == (target_row, target_column):
                erosion_level = (0 + cave_depth) % 20183
                erosion_row.append(erosion_level)
            elif row == 0:
                erosion_level = ((column * 16807) % 20183 + cave_depth % 20183) % 20183
                erosion_row.append(erosion_level)
            elif column == 0:
                erosion_level = ((row * 48271) % 20183 + cave_depth % 20183) % 20183
                erosion_row.append(erosion_level)
            else:
                erosion_level = ((erosion_row[-1] % 20183) * (erosion_levels[row-1][column] % 20183) + cave_depth % 20183) % 20183
                erosion_row.append(erosion_level)
            type_row.append(erosion_level % 3)
        erosion_levels.append(erosion_row)
        rock_types.append(type_row)

    return rock_types

def HeapAndDictDijkstra(start_coords, target_coords, rock_types):

    t1 = time.time()
    vertices = []
    vertex_dict = {}
    final_distances = {}
    entry_number = 0
    # encode tools as torch = 1, climbing gear = 2, neither = 0
    for row, row_values in enumerate(rock_types):
        for column, rock_type in enumerate(row_values):
            if (row, column) == start_coords: 
                to_append = [0, entry_number, row, column, 1, True]
                vertices.append(to_append)
                vertex_dict[(row, column, 1)] = to_append
            elif rock_type == 0: # rocky
                to_append1 = [math.inf, entry_number, row, column, 1, True]
                vertices.append(to_append1)
                vertex_dict[(row, column, 1)] = to_append1
                to_append2 = [math.inf, entry_number, row, column, 2, True]
                vertices.append(to_append2)
                vertex_dict[(row, column, 2)] = to_append2
            elif rock_type == 1: # wet
                to_append1 = [math.inf, entry_number, row, column, 0, True]
                vertices.append(to_append1)
                vertex_dict[(row, column, 0)] = to_append1
                to_append2 = [math.inf, entry_number, row, column, 2, True]
                vertices.append(to_append2)
                vertex_dict[(row, column, 2)] = to_append2
            else: # narrow
                to_append1 = [math.inf, entry_number, row, column, 1, True]
                vertices.append(to_append1)
                vertex_dict[(row, column, 1)] = to_append1
                to_append2 = [math.inf, entry_number, row, column, 0, True]
                vertices.append(to_append2)
                vertex_dict[(row, column, 0)] = to_append2
            entry_number += 1

    t2 = time.time()
    total_vertices = len(vertices)
    while len(final_distances) < total_vertices:
         
        u = heapq.heappop(vertices)
        while not u[5]: u = heapq.heappop(vertices)

        final_distances[(u[2], u[3], u[4])] = u[0]

        if (u[2], u[3]) == target_coords and u[4] == 1:
            break

        u_neighbour_coords = [(u[2]-1, u[3]), (u[2]+1, u[3]), (u[2], u[3]-1), (u[2], u[3]+1)]
        u_neighbours = []
        for u_neigh in u_neighbour_coords:
            if u_neigh[0] < 0 or u_neigh[1]<0: continue
            if (u_neigh[0], u_neigh[1], 0) in vertex_dict:
                u_neighbours.append((u_neigh[0], u_neigh[1], 0))
            if (u_neigh[0], u_neigh[1], 1) in vertex_dict:
                u_neighbours.append((u_neigh[0], u_neigh[1], 1))
            if (u_neigh[0], u_neigh[1], 2) in vertex_dict:
                u_neighbours.append((u_neigh[0], u_neigh[1], 2))

        for u_neighbour in u_neighbours: 
            v = vertex_dict[u_neighbour]
            
            if v[4] == u[4]:
                alt = u[0] +1
            elif (u[2], u[3], v[4]) in vertex_dict: 
                alt = u[0] + 8
            else: 
                continue
            if alt < v[0]:
                v[5] = False
                new_v = [alt, v[1], v[2], v[3], v[4], True]
                heapq.heappush(vertices, new_v)
                vertex_dict[u_neighbour] = new_v

    return final_distances[(target_coords[0], target_coords[1], 1)]

target_row = 796
target_column = 14
cave_depth = 5355

rock_types = calculate_types(target_row, target_column, cave_depth)

min_distance = HeapAndDictDijkstra((0,0), (target_row, target_column), rock_types)

print('minimum time taken is', min_distance)
