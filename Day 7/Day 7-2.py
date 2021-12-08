'''
Challenge: https://adventofcode.com/2021/day/7
By Daniel Lopez Gala with ❤️
'''

import sys

# Crab submarines can only ove horizontally.
# Horizontal position of each crab: Input.
# Find optimal movement to align. (Less movements -> Cheapest fuel).

# Each 1 step, costs 1 more than the last. First step 1, second step costs 2...

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
        # Calculate the cost of each crab for moving from crab to i.
        for crab in crabs:
            numbers = [i + 1 for i in range(abs(i - crab))]
            fuel += sum(numbers)
            # print(f"For crab: {crab} to: {i}, range: {len(numbers)}, numbers: {numbers}, and cost: {sum(numbers)}")
        print(f"Fuel for moving to: {i} is: {fuel}")
        if(fuel < optimum):
            optimum = fuel
    return optimum


print(computeCheapest(crabs))
