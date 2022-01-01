'''
Challenge: https://adventofcode.com/2021/day/1
By Daniel Lopez Gala with ❤️
'''

counter = 0
numberlines = 0
numberlines2 = 0
sums = []

f = open("input.txt", "r")
lines = f.readlines()
for i in range(len(lines) - 2):
    num = int(lines[i]) + int(lines[i + 1]) + int(lines[i + 2])
    sums.append(num)

for i in range(len(sums) - 1):
    if(int(sums[i]) < int(sums[i + 1])):
        counter += 1

print(counter)
f.close()
