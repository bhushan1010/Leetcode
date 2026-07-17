from typing import List
from bisect import bisect_right

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        maxVal = max(nums)
        cnt = [0] * (maxVal + 1)
        for x in nums:
            cnt[x] += 1
        multiples_count = [0] * (maxVal + 1)
        for d in range(1, maxVal + 1):
            s = 0
            for m in range(d, maxVal + 1, d):
                s += cnt[m]
            multiples_count[d] = s
        exact = [0] * (maxVal + 1)
        for d in range(maxVal, 0, -1):
            c = multiples_count[d]
            total = c * (c - 1) // 2
            for m in range(2 * d, maxVal + 1, d):
                total -= exact[m]
            exact[d] = total
        values = []
        prefix = []
        running = 0
        for d in range(1, maxVal + 1):
            if exact[d] > 0:
                running += exact[d]
                prefix.append(running)
                values.append(d)
        answer = []
        for q in queries:
            idx = bisect_right(prefix, q)
            answer.append(values[idx])
        return answer