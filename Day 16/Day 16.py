'''
Challenge: https://adventofcode.com/2021/day/16
By Daniel Lopez Gala with ❤️ with the help of AoC reddit forum,
as I didn't even know how to program a class at the time I had to program this.
'''


import math
from functools import reduce

from numpy import True_

class Bits:
    def __init__(self, hexstream):
        self.bitstream = []
        for each in hexstream:
            self.bitstream.extend(bin(int(each, 16))[2:].zfill(4))
        # counter of bits read
        self.read = 0
        # sum of all packet versions
        self.vsum = 0

    def get_bits(self, n):
        # store the count of the bits 
        self.read += n
        # get the bits from the first to the nth one
        bits = self.bitstream[:n]
        # update the pending bits
        self.bitstream = self.bitstream[n:]
        # return the bits
        return bits
    
    def decode_bits(self, x):
        # transform to int the str that you get from join each element in x
        return int("".join([str(b) for b in x]), 2)

    def get_literal(self):
        n = []
        while True:
            last = self.decode_bits(self.get_bits(1)) == 0
            n.extend(self.get_bits(4))
            if last: break
        return self.decode_bits(n)

    def decode_packet(self):
        version = self.decode_bits(self.get_bits(3))
        idpacket = self.decode_bits(self.get_bits(3))
        self.vsum += version

        # Literal packet
        if idpacket == 4:
            value = self.get_literal()
        # Operator packet
        else:
            lengthtype = self.decode_bits(self.get_bits(1))
            v = []
            if lengthtype == 0:
                length = self.decode_bits(self.get_bits(15))
                pos = self.read
                while pos + length > self.read:
                    v.append(self.decode_packet())
            # Number of subpackets
            elif lengthtype == 1:
                subpackets = self.decode_bits(self.get_bits(11))
                for _ in range(subpackets):
                    v.append(self.decode_packet())
            
            if idpacket == 0:
                value = sum(v)
            elif idpacket == 1:
                value = reduce(lambda x, y: x*y, v)
            elif idpacket == 2:
                value = min(v)
            elif idpacket == 3:
                value = max(v)
            elif idpacket == 5:
                value = int(v[0] > v[1])
            elif idpacket == 6:
                value = int(v[0] < v[1])
            elif idpacket == 7:
                value = int(v[0] == v[1])
        return value


with open("input.txt") as f:
    for line in f:
        message = line.strip()
bits = Bits(message)
res = bits.decode_packet()
print(bits.vsum)
print(res)
