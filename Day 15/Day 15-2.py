'''
Challenge: https://adventofcode.com/2021/day/15
By Daniel Lopez Gala with ❤️
'''

# The cave is a matrix, the value is the risk level.
# Start in top left, to bottom right. Find a path with lowest total risk.
# You cannot move diagonally.

# Solution using Dijkstra.


'''
Dijkstra implementation.
'''

import math
from math import floor
from heapq import heappop, heappush
from collections import defaultdict

def get_adjacents(position, M):
    x, y = position
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    output = []

    for add_x, add_y in directions:
        adjacent_x = x + add_x
        adjacent_y = y + add_y

        if 0 <= adjacent_y < len(M) and 0 <= adjacent_x < len(M[adjacent_y]):
            output.append((adjacent_x, adjacent_y))
    
    return output


def get_risk(M):

    # Position which we want to find the best path to.
    destination = (len(M) - 1, len(M[0]) - 1)

    # Dijkstra dictionary initialized with infinite.
    cell_risks = defaultdict(lambda: math.inf)
    cell_risks[(0, 0)] = 0

    # Dijkstra queue of cells to visit.
    cell_visit_queue = []
    heappush(cell_visit_queue, (0, (0, 0)))

    # Set of unvisited cells.
    unvisited_cells = set()

    # Initialize empty unvisited cells.
    for y, row in enumerate(M):
        for x, cell in enumerate(row):
            unvisited_cells.add((x, y))

    while destination in unvisited_cells:
        current_risk, current = heappop(cell_visit_queue)

        if current not in unvisited_cells:
            continue   

        adjacents = get_adjacents(current, M)

        for adjacent in adjacents:
            if adjacent not in unvisited_cells:
                continue
            
            adjacent_risk = min(cell_risks[adjacent], cell_risks[current] + M[adjacent[1]][adjacent[0]])

            cell_risks[adjacent] = adjacent_risk
            heappush(cell_visit_queue, (adjacent_risk, adjacent))

        unvisited_cells.remove(current)

    return cell_risks[destination]

def compute_risk(width, height, r, x, y):
    new_x = floor(x / width)
    new_y = floor(y / height)
    return (r + new_x + new_y - 1) % 9 + 1


lines = open('input.txt', 'r').readlines()
M = [[int(pos) for pos in line.strip()] for line in lines]

t_width = len(M[0])
f_width = t_width * 5
t_height = len(M)
f_height = t_height * 5

f_M = [[] for y in range(f_height)]

for y in range(f_height):
    for x in range(f_width):
        f_M[y].append(compute_risk(t_width, t_height,
                      M[y % t_height][x % t_width], x, y))

print(get_risk(f_M))