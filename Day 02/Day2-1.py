'''
Challenge: https://adventofcode.com/2021/day/2
By Daniel Lopez Gala with ❤️
'''

# down adds and up decreases
depth = 0

# forward adds
horizontal = 0

f = open("input.txt", "r")
lines = f.readlines()

for line in lines:
    text = line.split(' ')[0]
    number = line.split(' ')[1]
    if(text == 'forward'):
        horizontal += int(number)
    if(text == 'down'):
        depth += int(number)
    if(text == 'up'):
        depth -= int(number)

print("Depth: " + str(depth))
print("Horizontal: " + str(horizontal))
print("Multiplication: " + str(depth * horizontal))