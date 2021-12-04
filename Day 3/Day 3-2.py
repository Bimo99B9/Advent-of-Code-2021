'''
Challenge: https://adventofcode.com/2021/day/3
By Daniel Lopez Gala with ❤️
'''

# Oxygen generator --> Keep numbers with the most common value in the bit position.
    # If 0 and 1 equally common, keep 1.
# CO2 scrubber --> Keep numbers with the least common value in the bit position.
    # If 0 and 1 equally common, keep 0.

'''
Returns the most common bit in the bit position of the input.
'''
def mostCommonBit(input, bit):
    ones = 0
    for each in input:
        if (each[bit] == "1"):
            ones += 1
    zeros = len(input) - ones
    if(ones >= zeros):
        return 1
    else:
        return 0

'''
Returns the oxygen with recursion.
'''
def getOxygen(input, bit):
    if(len(input) == 1):
        return input[0]
    else:
        b = mostCommonBit(input, bit)
        result = []
        if b == 1:
            for each in input:
                if each[bit] == '1':
                    result.append(each)
            return getOxygen(result, bit+1)
        else:
            for data in input:
                if data[bit] == '0':
                    result.append(data)
            return getOxygen(result, bit+1)

'''
Returns the scrubber with recursion.
'''
def getScrubber(input, bit):
    if(len(input) == 1):
        return input[0]
    else:
        b = mostCommonBit(input, bit)
        result = []
        if b == 1:
            for each in input:
                if each[bit] == '0':
                    result.append(each)
            return getScrubber(result, bit+1)
        else:
            for data in input:
                if data[bit] == '1':
                    result.append(data)
            return getScrubber(result, bit+1)

data= open("input.txt").readlines()
oxygen = int(getOxygen(data, 0), 2)
scrubber = int(getScrubber(data, 0), 2)
print(f"Oxygen: {oxygen}")
print(f"Scrubber: {scrubber}")
print(f"Multiplication: {oxygen * scrubber}")
