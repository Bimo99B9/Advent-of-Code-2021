'''
Challenge: https://adventofcode.com/2021/day/4
By Daniel Lopez Gala with ❤️
'''

import re

# Marks the boards removing the "n" number.
def markBoards(boards, n, winners):
    for b, board in enumerate(boards):
        for i, row in enumerate(board):
            for j in range(len(row)):
                if(row[j] == n and b not in winners):
                    row[j] = -1
    return boards

def getWinners(boards, numbers):
    winners = []
    winballs = []
    for number in numbers:
        boards = markBoards(boards, number, winners)
        # Check in rows.

        for i, board in enumerate(boards):
            for j, row in enumerate(board):
                winner = True
                for k in range(5):
                    if row[k] != -1:
                        winner = False
                if(winner and i not in winners):
                    winners.append(i)
                    winballs.append(number)
                    print(f"Board number {i} is winner at ball: {number}")
                    print(board)
        
        # Check in columns
        for i, board in enumerate(boards):
            # j is the column and k is the row. [j][k]
            for j in range(5):
                winner = True
                for k in range(5):
                    if board[k][j] != -1:
                        winner = False
                if(winner and i not in winners):
                    winners.append(i)
                    winballs.append(number)
                    print(f"Board number {i} is winner at ball: {number}")
                    print(board)
    return [winners, winballs]
                    

with open('input.txt', 'r') as f:
    parts = f.read().strip().split('\n\n')
numbers = [int(x) for x in parts[0].split(',')]
boards = []
for each in parts[1:]:
    boards.append([])
    for line in each.split('\n'):
        boards[-1].append([int(x) for x in re.findall(r'\d\d?', line)])

# markBoards(boards, numbers[0])
winners, winballs = getWinners(boards, numbers)

firstwinner = boards[winners[0]]
lastwinner = boards[winners[-1]]

firstanswer = 0
for row in firstwinner:
    for x in row:
        if(x != -1):
            firstanswer += x
firstanswer *= winballs[0]

secondanswer = 0
for row in lastwinner:
    for x in row:
        if(x != -1):
            secondanswer += x
secondanswer *= winballs[-1]

print(f"\n\nFirst winner: {firstwinner} with the ball: {winballs[0]} and the first answer is {firstanswer}")
print(f"Last winner: {lastwinner} with the ball: {winballs[-1]} and the second answer is {secondanswer}")