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

fishes = []
data = open('input.txt', 'r').readlines()[0].strip().split(',')
for each in data:
    fishes.append(int(each))

def computeDay(fishes, day, maxday):
    print(f"Day: {day}, number of lanternfishes: {len(fishes)}")
    # print(f"Fishes: {fishes}")
    if(day == maxday):
        return fishes
    else:
        result = fishes
        for i, fish in enumerate(fishes):
            if(fish) == 0:
                result[i] = 6
                result.append(9)
            else:
                result[i] -= 1
        computeDay(result, day + 1, maxday)

### Check algorithm with the example in the web.
# example = [3, 4, 3, 1, 2]      
# computeDay(example, 0, 5)

computeDay(fishes, 0, 256)
