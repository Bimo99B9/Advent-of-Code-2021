'''
Challenge: https://adventofcode.com/2021/day/2
By Daniel Lopez Gala with ❤️
'''

# forwards adds X multiplied by aim
depth: int = 0

# forward adds X
horizontal: int = 0

# down increases aim by X
# up decreases aim by X
aim: int = 0

f = open("input.txt", "r")
lines = f.readlines()

for line in lines:
    text = line.split(' ')[0]
    number = int(line.split(' ')[1])
    if(text == 'forward'):
        horizontal += number
        depth += (number * aim)
    if(text == 'down'):
        aim += number
    if(text == 'up'):
        aim -= number

print("Depth: " + str(depth))
print("Horizontal: " + str(horizontal))
print("Aim: " + str(horizontal))
print("Multiplication: " + str(depth * horizontal))