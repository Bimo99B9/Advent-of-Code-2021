'''
Challenge: https://adventofcode.com/2021/day/10
By Daniel Lopez Gala with ❤️
'''

data = open('input.txt', 'r').readlines()
points = 0

def addPoints(character):
    if character == ')':
        return 3
    if character == ']':
        return 57
    if character == '}':
        return 1197
    if character == '>':
        return 25137

for line in data:
    stack = []
    for character in line:
    
        print(stack)

        if character == '(':
            stack.append('(')
        if character == '[':
            stack.append('[')
        if character == '{':
            stack.append('{')
        if character == '<':
            stack.append('<')
        

        if character == ')':
            if stack[-1] == '(':
                stack.pop()
            else: 
                print(f'Found illegal {character}')
                points += addPoints(character)
                break

        if character == ']':
            if stack[-1] == '[':
                stack.pop()
            else:
                print(f'Found illegal {character}')
                points += addPoints(character)
                break

        if character == '}':
            if stack[-1] == '{':
                stack.pop()
            else: 
                print(f'Found illegal {character}')
                points += addPoints(character)
                break

        if character == '>':
            if stack[-1] == '<':
                stack.pop()
            else:
                print(f'Found illegal {character}')
                points += addPoints(character)
                break

        

print(points)