'''
Challenge: https://adventofcode.com/2021/day/1
'''

counter = 0
f = open("input.txt", "r")
lines = f.readlines()

numberlines = len(lines)

for i in range(numberlines - 1):
    if(int(lines[i]) < int(lines[i + 1])):
        counter += 1
print(counter)
f.close()
