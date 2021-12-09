'''
Challenge: https://adventofcode.com/2021/day/9
By Daniel Lopez Gala with ❤️
'''

# Heightmap of the floor of the nearby caves.
# low points: Lower than any of its adjacent locations.

# risk level = 1 + height

data = open('input.txt', 'r').readlines()

# Cave is a matrix with the values.
cave = []
for line in data:
    cave.append([])
    for n in line.strip():
        cave[-1].append(n)


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

def getRiskLevel(x, y, cave):
    return int(cave[x][y]) + 1
    
def getSumRiskLevels(lowpoints, cave):
    addition = 0
    for lowpoint in lowpoints:
        x = lowpoint[0]
        y = lowpoint[1]
        addition += getRiskLevel(x, y, cave)
    return addition


print(f"Sum of risk level of the low points is: {getSumRiskLevels(getLowPoints(cave), cave)}")