
# target coordinates are required to be always >= 0, 
# otherwise cannot evaluate geologic index from the last rule
target_row = 796
target_column = 14

cave_depth = 5355

erosion_levels = []
total_risk_level = 0

# have to do some modulo computation when computing to avoid too large numbers
for row in range(0, target_row+1):
    erosion_row = []
    for column in range(0, target_column+1):
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
        total_risk_level += erosion_level % 3
    erosion_levels.append(erosion_row)

print('Total risk level is:', total_risk_level)