'''
Challenge: https://adventofcode.com/2021/day/8
By Daniel Lopez Gala with ❤️
'''

# Seven-segment displays. (a-g).
# Ten unique signal patterns.
# Four digit output value. --> Which pattern corresponds to which digit?

'''
We can count how many times number with unique number of segments appear.
0:  6 segments
1:  2 segments <--
2:  5 segments
3:  5 segments
4:  4 segments <--
5:  5 segments
6:  6 segments
7:  3 segments <--
8:  7 segments <--
9:  6 segments
'''

f = open('input.txt', 'r')
lines = f.readlines()

times = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for line in lines:
    patterns = line.strip().split('|')[0]
    digits = line.strip().split('|')[1]
    for digit in digits.split(' '):
        if(len(digit) == 2): times[1] += 1
        if(len(digit) == 4): times[4] += 1
        if(len(digit) == 3): times[7] += 1
        if(len(digit) == 7): times[8] += 1


print(f"The number of times that digits 1, 4, 7 or 8 appear is: {sum(times)}")