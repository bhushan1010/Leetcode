from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        V = set(nums)
        nbits = 11
        W = 1 << nbits

        masks0 = []
        for i in range(nbits):
            block = 1 << i
            full = block << 1
            one_block = (1 << block) - 1
            m = 0
            pos = 0
            while pos < W:
                m |= one_block << pos
                pos += full
            masks0.append(m)

        def xor_shift(T: int, a: int) -> int:
            for i in range(nbits):
                if a & (1 << i):
                    shift = 1 << i
                    mask0 = masks0[i]
                    mask1 = mask0 << shift
                    low = T & mask0
                    high = T & mask1
                    T = (low << shift) | (high >> shift)
            return T

        S = 0
        for v in V:
            S |= 1 << v

        S2 = 0
        for a in V:
            S2 |= xor_shift(S, a)

        S3 = 0
        for a in V:
            S3 |= xor_shift(S2, a)

        return bin(S3).count('1')