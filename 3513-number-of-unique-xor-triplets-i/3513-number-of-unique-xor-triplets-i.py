class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n >= 3:
            bits = n.bit_length()
            return 1 << bits
        seen = set()
        for i in range(n):
            for j in range(i, n):
                for k in range(j, n):
                    seen.add(nums[i] ^ nums[j] ^ nums[k])
        return len(seen)