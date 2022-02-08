'''
Challenge: https://adventofcode.com/2021/day/14
By Daniel Lopez Gala with ❤️
'''

from re import findall
from collections import Counter


steps = 40


def polymerization(data, steps):

    # Template to polymer.
    template, rules = data.split('\n\n')
    # Create a dictionary with the pairs.
    rules = dict(findall('(\w\w) -> (\w)', rules))
    # Pair counter
    count = Counter(map(''.join, zip(template, template[1:])))
    

    for each in range(steps):
        for key, num in count.copy().items():
            # Char to be add between first and second (value in dict)
            toadd = rules[key]

            # The count of the current pair is decreased, as it is destroyed and replaced with two new ones.
            count[key] -= num

            # The key in the dictionary is the first and the second
            first, second = key

            # Update counts of the two created pairs.
            count[first + toadd] += num
            count[toadd + second] += num
    
    temp_res = Counter([template[0], template[-1]])
    for each, num in count.items():
        first = each[0]
        second = each[1]
        temp_res[first] += num
        temp_res[second] += num

    (_, most), *_, (_, least) = temp_res.most_common()
    return (most - least)//2


result = polymerization(open('input.txt').read(), steps)
print(result)
