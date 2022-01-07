'''
Challenge: https://adventofcode.com/2021/day/13
By Daniel Lopez Gala with ❤️
'''

data = []
instructions = []
secondpart = False
for line in open('input.txt', 'r').readlines():
    if secondpart:
        instructions.append(line.rstrip().split(' ')[2])
    if line == '\n':
        secondpart = True
    if not secondpart:
        p2, p1 = line.split(',')
        data.append((int(p1), int(p2)))


maxrows = 0
maxcolumns = 0
for each in data:
    if each[0] > maxrows:
        maxrows = each[0]
    if each[1] > maxcolumns:
        maxcolumns = each[1]

print(f'Rows: {maxrows}, Columns: {maxcolumns}')
print(f'Instructions: {instructions}')

paper = [[False for x in range(maxcolumns + 1)] for y in range(maxrows + 1)]

for each in data:
    x, y = each[0], each[1]
    paper[x][y] = True


def foldY(paper, y):
    newrows = y
    newpaper = [[False for x in range(len(paper[0]))] for y in range(newrows)]
    for i, row in enumerate(newpaper):
        for j, column in enumerate(row):
            if paper[i][j] == True:
                newpaper[i][j] = True

    for j in range(len(paper[0])):
        tomirror = []
        for i in range(y, len(paper)):
            tomirror.append(paper[i][j])
        tomirror.reverse()
        '''
        1 (2 3 4) | 5 6 7
        (7 6 5)

        (1 2) | 3 4 5 6 7
        (7 6) 5 4 3
        '''
        l = []
        for i in range(min(y, len(tomirror))):
            l.append(i)
        l.reverse()
        for i in l:
            if(tomirror[i] == True):
                newpaper[i][j] = True
    return newpaper


def foldX(paper, x):
    newcolumns = len(paper[0]) - x - 1
    newpaper = [[False for x in range(newcolumns)] for y in range(len(paper))]
    for i, row in enumerate(newpaper):
        for j, column in enumerate(row):
            if paper[i][j] == True:
                newpaper[i][j] = True

    for i in range(len(paper)):
        tomirror = []
        for j in range(x, len(paper[0])):
            tomirror.append(paper[i][j])
        tomirror.reverse()
        l = []
        for j, x in enumerate(newpaper[i]):
            l.append(j)
        l.reverse()
        for j in l:
            if(tomirror[j] == True):
                newpaper[i][j] = True
    return newpaper


for each in instructions:
    ins, n = each.split('=')
    if(ins == 'x'):
        paper = foldX(paper, int(n))
    if(ins == 'y'):
        paper = foldY(paper, int(n))

solution = []
for i, row in enumerate(paper):
    string = ""
    for j, column in enumerate(row):
        if paper[i][j] == True:
            string += "#"
        else:
            string += " "
    solution.append(string)

print(len(paper))
print(len(paper[0]))

for each in solution:
    print(each)
