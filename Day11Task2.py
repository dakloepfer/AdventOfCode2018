# Grid Serial Number is 9445

from math import floor, inf
import time

def computeFuelLevels(grid_size_x, grid_size_y, grid_serial_number):

    grid = [[0 for i in range(0, grid_size_x)] for j in range(0, grid_size_y)]

    for y in range(1, grid_size_y+1):
        for x in range(1, grid_size_x+1):
            rack_id = x + 10
            power_level = ((rack_id * y) + grid_serial_number) * rack_id
            power_level = floor((power_level % 1000) / 100) - 5

            grid[y-1][x-1] = power_level

    return grid

def findMaxRectangle(grid, rectangle_size_x, rectangle_size_y):
    # do it in this way to increase speed
    rectangle_values = [[0 for i in range(0, len(grid[0])-rectangle_size_x+1)] for j in range(0, len(grid)-rectangle_size_y+1)]
    t1 = time.time()
    for y in range(0, len(rectangle_values)):
        for x in range(0, len(rectangle_values[0])):

            update_value = sum(grid[y][x:x+rectangle_size_x])
            for i in range(0, rectangle_size_y):
                if y >= i: rectangle_values[y-i][x] += update_value

    t2 = time.time()
    max_x_index = 0
    max_y_index = 0
    max_value = -inf
    

    for i in range(0, len(rectangle_values)):
        for j in range(0, len(rectangle_values[0])):
            if rectangle_values[i][j] > max_value:
                max_value = rectangle_values[i][j]
                max_y_index = i
                max_x_index = j
    print(rectangle_size_x, t2-t1, time.time()-t2)
    return [max_value, max_x_index+1, max_y_index+1]

grid_size_x = 300
grid_size_y = 300

grid_serial_number = 9445

fuel_levels = computeFuelLevels(grid_size_x, grid_size_y, grid_serial_number)

max_squares = [0 for s in range(0, grid_size_x)]
for size in range(1, grid_size_x + 1):
    max_squares[size-1] = findMaxRectangle(fuel_levels, size, size)

print(max(max_squares), max_squares.index(max(max_squares))+1)
