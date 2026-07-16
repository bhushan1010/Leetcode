from math import gcd
from itertools import accumulate

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        
        running_max = accumulate(nums, max)
        
        prefixGcd = [gcd(a, b) for a, b in zip(nums, running_max)]
        
        prefixGcd.sort()
        
        total = 0
        _gcd = gcd
        left, right = 0, n - 1
        while left < right:
            total += _gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1
        
        return total