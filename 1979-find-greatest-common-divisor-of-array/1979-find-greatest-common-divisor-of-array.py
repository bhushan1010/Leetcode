class Solution:
    def findGCD(self, nums: List[int]) -> int:
        lo, hi = min(nums), max(nums)
        while lo:
            hi, lo = lo, hi % lo
        return hi