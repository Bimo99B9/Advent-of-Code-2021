'''
Challenge: https://adventofcode.com/2021/day/11
By Daniel Lopez Gala with ❤️
'''

global flashes
flashes = 0

def getNeighbours(i, j, m, n):
    adjacent_indices = []

    # Top
    if i > 0:
        adjacent_indices.append((i-1, j))
    # Bottom
    if i+1 < m:
        adjacent_indices.append((i+1, j))
    # Left
    if j > 0:
        adjacent_indices.append((i, j-1))
    # Right
    if j+1 < n:
        adjacent_indices.append((i, j+1))

    # Top-left
    if i > 0 and j > 0:
        adjacent_indices.append((i-1, j-1))
    # Top-right
    if i > 0 and j+1 < n:
        adjacent_indices.append((i-1, j+1))
    # Bottom-left
    if i+1 < m and j > 0:
        adjacent_indices.append((i+1, j-1))
    # Bottom-right
    if i+1 <  m and j+1 < n:
        adjacent_indices.append((i+1, j+1))

    return adjacent_indices

def flash(cavern, flashed, i, j):
    if cavern[i][j] > 9 and not flashed[i][j]:
        flashed[i][j] = True
        cavern[i][j] = 0
        global flashes
        flashes += 1
        for neigh in getNeighbours(i, j, len(cavern), len(cavern)):
            cavern[neigh[0]][neigh[1]] += 1
        for neigh in getNeighbours(i, j, len(cavern), len(cavern)):
            flash(cavern, flashed, neigh[0], neigh[1])
    #print(f'Number of flashes: {flashes}')
    return flashes

def computeStep(cavern, n):
    for step in range(n):
        print(f'Step {step + 1}')

        flashed = []
        for line in data:
            flashed.append([])
            for n in line.strip():
                flashed[-1].append(False)

        for i, row in enumerate(cavern):
            for j, column in enumerate(row):
                cavern[i][j] += 1

        for i, row in enumerate(cavern):
            for j, column in enumerate(row):
                if not flashed[i][j]:
                    flash(cavern, flashed, i, j)

        
        for i, row in enumerate(flashed):
            for j, column in enumerate(row):
                if flashed[i][j] == True:
                    cavern[i][j] = 0

        allflashed = True
        for i, row in enumerate(cavern):
            for j, column in enumerate(row):
                if cavern[i][j] != 0:
                    allflashed = False

        if allflashed == True:
            print(f'The first step when all flash is: {step + 1}')
            return step + 1
        
        print(cavern)


data = open('input.txt', 'r').readlines()

cavern = []
for line in data:
    cavern.append([])
    for n in line.strip():
        cavern[-1].append(int(n))

print('Original cavern')
print(cavern)

print(computeStep(cavern, 10000))
print(f'Number of flashes: {flashes}')