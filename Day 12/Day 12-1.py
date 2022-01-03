'''
Challenge: https://adventofcode.com/2021/day/12
By Daniel Lopez Gala with ❤️
'''

M = {}
solution = []

def computePath(cave):
    global current
    for each in cave:
        if each in current and each.islower():
            continue
        elif each == 'end':
            current.append(each)
            solution.append(current[:])
            current.pop()
        else:
            current.append(each)
            computePath(M[each])
    current.pop()

data = []
for line in open('input.txt', 'r').readlines():
    node1, node2 = line.rstrip().split('-')
    data.append((node1, node2))

for a in data:
    if a[0] not in M:
        M[a[0]] = []
    M[a[0]].append(a[1])
    if a[1] not in M:
        M[a[1]] = []
    M[a[1]].append(a[0])

current = ["start"]
computePath(M["start"])

print(len(solution))


