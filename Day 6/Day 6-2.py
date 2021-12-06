'''
Challenge: https://adventofcode.com/2021/day/6
By Daniel Lopez Gala with ❤️
'''

# Each lanternfish creates a new lanternfish once every 7 days. (Counter 0-6, resets to 6).
# Each lanternfish represented as the number of days until it creates a new lanternfish.
# 3 -> 2 -> 1 -> 0 -> 6 and creates [new Lanternfish]. -> 5 -> 4...
#                                                    8 -> 7 -> 6 ...
# Initial state: 3,4,3,1,2
# After  1 day:  2,3,2,0,1
# After  2 days: 1,2,1,6,0,8
# After  3 days: 0,1,0,5,6,7,8
# After  4 days: 6,0,6,4,5,6,7,8,8
# After  5 days: 5,6,5,3,4,5,6,7,7,8

from functools import lru_cache

fishes = []
data = open('input.txt', 'r').readlines()[0].strip().split(',')
for each in data:
    fishes.append(int(each))


# Optimal by splitting problems and adding the solutions.
@lru_cache(None)
def computeDay(fishes, day, pending):
    if(day == 0):
        return fishes
    if(pending == 0):
        justborn = computeDay(fishes, day - 1, 8)
        actual = computeDay(fishes, day - 1, 6)
        return justborn + actual
    return computeDay(fishes, day - 1, pending - 1)

answer = 0
for fish in fishes:
    answer += computeDay(1, 256, fish)
print(answer)