'''
Challenge: https://adventofcode.com/2021/day/14
By Daniel Lopez Gala with ❤️
'''

import collections

# Result = Polymer after repeating the pair insertion process a few times.

template = ""
rules = []
secondpart = False
for line in open('input.txt', 'r').readlines():
    if secondpart:
        rules.append(line.rstrip())
    if line == '\n':
        secondpart = True
    if not secondpart:
        template = line.rstrip()

steps = 10

def polymerization(template, rules):
    result = ""
    result += template[0]
    for i in range (len(template) - 1):
        first = template[i]
        second = template[i + 1]
        #print(f'First: {first} and second: {second}')
        found = False
        for rule in rules:
            left = rule.split('->')[0].strip()
            right = rule.split('->')[1].strip()
            #print(f'Left: {left}')
            #print(f'Right: {right}')
            if first + second == left:
                result += (right + second)
                #print(result)
                found = True
        if not found:
            result += (first + second)
            #print(result)
    return result

print(f'Original template: {template}')
for i in range(steps):
    template = polymerization(template, rules)
    #print(f'After step {i + 1}: {template}')


dict = {}
for character in template:
    if character in dict:
        dict[character] += 1
    else:
        dict[character] = 1
mostcommon = str(max(dict, key=dict.get))
nmost = 0
for each in template:
    if each == mostcommon:
        nmost += 1

dict = {}
for character in template:
    if character in dict:
        dict[character] += 1
    else:
        dict[character] = 1
leastcommon = str(min(dict, key=dict.get))
nleast = 0
for each in template:
    if each == leastcommon:
        nleast += 1

print(f'{nmost - nleast}')
