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

autocomplete = []
for line in data:
    stack = []
    corrupted = False
    for character in line:

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
                corrupted = True
                break

        if character == ']':
            if stack[-1] == '[':
                stack.pop()
            else:
                print(f'Found illegal {character}')
                corrupted = True
                break

        if character == '}':
            if stack[-1] == '{':
                stack.pop()
            else: 
                print(f'Found illegal {character}')
                corrupted = True
                break

        if character == '>':
            if stack[-1] == '<':
                stack.pop()
            else:
                print(f'Found illegal {character}')
                corrupted = True
                break
    if not corrupted:
        autocomplete.append(line)

completed = []
for line in autocomplete:
    stack = []
    for character in line:

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
        if character == ']':
            if stack[-1] == '[':
                stack.pop()
        if character == '}':
            if stack[-1] == '{':
                stack.pop()
        if character == '>':
            if stack[-1] == '<':
                stack.pop()
    completed.append(line)
    
    
