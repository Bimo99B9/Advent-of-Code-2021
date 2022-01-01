'''
Challenge: https://adventofcode.com/2021/day/3
By Daniel Lopez Gala with ❤️
'''

# Gamma rate --> Most common bit in the numbers. (By columns).
# Epsilon rate --> Least common bit (Opposite of gamma rate)-
# Power consumption --> Gamma rate * Epsilon rate.

# Substracting 1 because of the line break
size = len(open("input.txt").readlines()[0]) - 1
counters_ones = [0] * size
counters_zeros = [0] * size

for line in open("input.txt"):
    for i in range(size):
        if(line[i] == "1"):
            counters_ones[i] = counters_ones[i] + 1
        else:
            counters_zeros[i] = counters_zeros[i] + 1

gamma, epsilon = "", ""
for i in range(size):
    if(counters_ones[i] > counters_zeros[i]):
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

print("Gamma: " + gamma)
print("Epsilon: " + epsilon)
print("Multiplication: " + str(int(gamma, 2) * int(epsilon, 2)))
