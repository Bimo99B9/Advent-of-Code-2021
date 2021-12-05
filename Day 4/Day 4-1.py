'''
Challenge: https://adventofcode.com/2021/day/4
By Daniel Lopez Gala with ❤️
'''

import re

# Marks the boards removing the "n" number.
def markBoards(boards, n):
    for board in boards:
        for i, row in enumerate(board):
            # board[i] = [x if x != n else None for x in row]

            for x in row:
                if(x != n):
                    board[i] = x
                else:
                    board[i] = None
    return boards

with open('input.txt', 'r') as f:
    parts = f.read().strip().split('\n\n')

numbers = [int(x) for x in parts[0].split(',')]

boards = []
for each in parts[1:]:
    boards.append([])
    for line in each.split('\n'):
        boards[-1].append([int(x) for x in re.findall(r'\d\d?', line)])

print(boards)
