'''
Challenge: https://adventofcode.com/2021/day/9
By Daniel Lopez Gala with ❤️
'''

# Heightmap of the floor of the nearby caves.
# low points: Lower than any of its adjacent locations.
# risk level = 1 + height

# basin: area that flow to a single low point.
# size of a basin: number of locations within the basin.

data = open('input.txt', 'r').readlines()

# Cave is a matrix with the values.
cave = []
for line in data:
    cave.append([])
    for n in line.strip():
        cave[-1].append(n)

heights = {}
with open('input.txt') as f:
    for x, row in enumerate(f):
        for y, each in enumerate(row.strip()):
            heights[(x, y)] = int(each)


def getNeighbours(i, j, m, n):
    adjacent_indices = []
    if i > 0:
        adjacent_indices.append((i-1, j))
    if i+1 < m:
        adjacent_indices.append((i+1, j))
    if j > 0:
        adjacent_indices.append((i, j-1))
    if j+1 < n:
        adjacent_indices.append((i, j+1))
    return adjacent_indices

def isLowPoint(i, j, cave):
    low = True
    neighbours = getNeighbours(i, j, len(cave), len(cave))
    for neigh in neighbours:
        x = neigh[0]
        y = neigh[1]
        if(cave[x][y] <= cave[i][j]):
            low = False
    return low

def getLowPoints(cave):
    lowpoints = []
    for i in range(len(cave)):
        for j in range(len(cave)):
            if(isLowPoint(i, j, cave)): lowpoints.append([i, j])
    return lowpoints

usedpositions = []
def getBasinsSize(low, cave, used, heights):
    # Starts in 1 because of the low point.
    size = 1

    for adjacent in getNeighbours(low[0], low[1], len(cave), len(cave)):
        if adjacent not in used:
            used.append(adjacent)
            curr = (adjacent[0], adjacent[1])
            if(heights[curr] != 9):
                size += getBasinsSize(adjacent, cave, used, heights)
    return size

basins = []
lowpoints = getLowPoints(cave)
for low in lowpoints:
    usedpositions.append(low)
    basins.append(getBasinsSize(low, cave, usedpositions, heights) - 1)

basins.sort(reverse=True)
print("Mult:", basins[0] * basins[1] * basins[2])
