'''
Challenge: https://adventofcode.com/2021/day/5
By Daniel Lopez Gala with ❤️
'''

def parseData(line):
    left = line.split('->')[0]
    right = line.split('->')[1]
    x1 = int(left.split(',')[0].strip())
    y1 = int(left.split(',')[1].strip())
    x2 = int(right.split(',')[0].strip())
    y2 = int(right.split(',')[1].strip())
    return x1, y1, x2, y2

def getSize():
    size = 0
    for line in open('input.txt').readlines():
        x1, y1, x2, y2 = parseData(line)
        if(max(x1, y1, x2, y2) > size):
            size = max(x1, y1, x2, y2)
    return size + 1

size = getSize()
ocean = []
for i in range(size):
    ocean.append([])
    for j in range(size):
        ocean[i].append([])

for i in range(size):
    for j in range(size):
        ocean[i][j] = 0


def myrange(x, y):
    if (y > x):
        return range(x, y + 1)
    else:
        return range(x, y - 1, -1)


for line in open('input.txt').readlines():
    x1, y1, x2, y2 = parseData(line)
    if(x1 == x2):
        # Case vertical line.
        if(y2 > y1):
            for i in range(y2 - y1 + 1):
                ocean[x1][y1 + i] += 1
        if(y1 > y2):
            for i in range(y1 - y2 + 1):
                ocean[x1][y2 + i] += 1
    elif(y1 == y2):
        # Case horizontal line.
        if(x2 > x1):
            for i in range(x2 - x1 + 1):
                ocean[x1 + i][y1] += 1
        if(x1 > x2):
            for i in range(x1 - x2 + 1):
                ocean[x2 + i][y1] += 1
    else:
        # Case diagonal line.
        for i, j in zip(myrange(x1, x2), myrange(y1, y2)):
            ocean[i][j] += 1

counter = 0
for i in range(size):
    for j in range(size):
        if(ocean[i][j] > 1):
            counter += 1
print(f"The number of points where at least two lines overlap is: {counter}")
