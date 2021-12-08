'''
Challenge: https://adventofcode.com/2021/day/7
By Daniel Lopez Gala with ❤️
'''

import sys

# Crab submarines can only ove horizontally.
# Horizontal position of each crab: Input.

# Find optimal movement to align. (Less movements -> Cheapest fuel).

crabs = []
data = open('input.txt', 'r').readlines()[0].strip().split(',')
for each in data:
    crabs.append(int(each))

def computeCheapest(crabs):
    minimum = min(crabs)
    maximum = max(crabs)
    optimum = sys.maxsize
    for i in range(minimum, maximum):
        fuel = 0
        for crab in crabs:
            fuel += abs(crab - i)
        print(f"Fuel for moving to: {i} is: {fuel}")
        if(fuel < optimum):
            optimum = fuel
    return optimum


print(computeCheapest(crabs))