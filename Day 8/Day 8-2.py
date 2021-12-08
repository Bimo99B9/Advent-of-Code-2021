'''
Challenge: https://adventofcode.com/2021/day/8
By Daniel Lopez Gala with ❤️
'''

import re

# Seven-segment displays. (a-g).
# Ten unique signal patterns.
# Four digit output value. --> Which pattern corresponds to which digit?

'''
We can count how many times number with unique number of segments appear.
0:          6 segments
1:  2 segments <--
2:      5 segments
3:      5 segments
4:  4 segments <--
5:      5 segments
6:          6 segments
7:  3 segments <--
8:  7 segments <--
9:          6 segments
'''

f = open('input.txt', 'r')
lines = f.readlines()

'''
Given a composition of segments, returns 
the number made of the provided encoded digits.
'''
def crackNumber(segm, nums):
    zero = "".join(sorted(segm['a']+segm['b']+segm['c']+segm['e']+segm['f']+segm['g']))
    one = "".join(sorted(segm['c']+segm['f']))
    two = "".join(sorted(segm['a']+segm['c']+segm['d']+segm['e']+segm['g']))
    three = "".join(sorted(segm['a']+segm['c']+segm['d']+segm['f']+segm['g']))
    four = "".join(sorted(segm['b']+segm['c']+segm['d']+segm['f']))
    five = "".join(sorted(segm['a']+segm['b']+segm['d']+segm['f']+segm['g']))
    six = "".join(sorted(segm['a']+segm['b']+segm['d']+segm['e']+segm['f']+segm['g']))
    seven = "".join(sorted(segm['a']+segm['c']+segm['f']))
    eight = "".join(sorted(segm['a']+segm['b']+segm['c']+segm['d']+segm['e']+segm['f']+segm['g']))
    nine = "".join(sorted(segm['a']+segm['b']+segm['c']+segm['d']+segm['f']+segm['g']))
    number = ""
    for num in nums:
        if(zero == "".join(sorted(num))): 
            number += '0'
        if(one == "".join(sorted(num))):
            number += '1'
        if(two == "".join(sorted(num))):
            number += '2'
        if(three == "".join(sorted(num))):
            number += '3'
        if(four == "".join(sorted(num))):
            number += '4'
        if(five == "".join(sorted(num))):
            number += '5'
        if(six == "".join(sorted(num))):
            number += '6'
        if(seven == "".join(sorted(num))):
            number += '7'
        if(eight == "".join(sorted(num))):
            number += '8'
        if(nine == "".join(sorted(num))):
            number += '9'
    return number
        
        
addition = 0
for line in lines:
    segments: dict = {
        'a': None,
        'b': None,
        'c': None,
        'd': None,
        'e': None,
        'f': None,
        'g': None,
    }
    patterns = line.strip().split('|')[0].split(' ')
    for each in patterns:
        pattern = "".join(sorted(each))
        if len(pattern) == 2: ONE = pattern
        if len(pattern) == 4: FOUR = pattern
        if len(pattern) == 3: SEVEN = pattern
        if len(pattern) == 7: EIGHT = pattern

    #### MAP SEGMENTS

    # (1): A = 7 - 1
    tmp = ""
    for c in SEVEN:
        if c not in ONE:
            tmp += c
    segments['a'] = tmp

    # (2): C, F = 1
    segments['c'] = ONE
    segments['f'] = ONE

    # (3): Save commons characters in patterns with length = 5, and substract A from them.
    fivelen = []
    for each in patterns:
        pattern = "".join(sorted(each))
        if(len(pattern) == 5):
            fivelen.append(pattern)
    tmp = "".join(set(fivelen[0]).intersection(fivelen[1]))
    common = "".join(set(tmp).intersection(fivelen[2]))
    result = ""
    for c in common:
        if(c != segments['a']):
            result += c
    
    # (4): B, D = 4 - 1
    tmp = ""
    for c in FOUR:
        if c not in ONE:
            tmp += c
    segments['b'] = tmp
    segments['d'] = tmp

    # (5): D = Comunes en result y D.
    segments['d'] = "".join(set(segments['d']).intersection(set(result)))
    
    # (6): B = B - D
    tmp = ""
    for c in segments['b']:
        if c not in segments['d']:
            segments['b'] = c
    
    # (7): G = (8 - 1 - A - B) común con result.
    tmp = ""
    for c in EIGHT:
        if c not in ONE and c not in segments['a'] and c not in segments['b'] and c not in segments['d']:
            tmp += c
    segments['g'] = "".join(set(result).intersection(set(tmp)))
  
    # (8): E = (8 - 1 - A - B) - G
    for c in tmp:
        if c not in segments['g']:
            segments['e'] = c
    
    # (9): C = From 1, appears in 8 patterns.
    for c in ONE:
        counter = 0
        for pattern in patterns:
            if(c in pattern): counter += 1
        if(counter == 8): segments['c'] = c

    # (10): F = 1 - C
    tmp = ""
    for c in ONE:
        if c not in segments['c']:
            segments['f'] = c
    

    #### CRACK THE NUMBER WITH THE SEGMENTS.

    digits = line.strip().split('|')[1].strip().split(' ')
    number = crackNumber(segments, digits)
    addition += int(number)

print(f"The addition of all the numbers is: {addition}")

# Test:
# segments: dict = {
#     'a': ['d'],
#     'b': ['e'],
#     'c': ['a'],
#     'd': ['f'],
#     'e': ['g'],
#     'f': ['b'],
#     'g': ['c'],
# }
# nums = ['cdfeb', 'fcadb', 'cdfeb', 'cdbaf']
# print(crackNumber(segments, nums))
