class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
        
        from functools import lru_cache
        
        @lru_cache(maxsize=None)
        def dp(i, m):
            if i >= n:
                return 0
            if i + 2 * m >= n:
                return suffix_sum[i]
            best = 0
            for x in range(1, 2 * m + 1):
                best = max(best, suffix_sum[i] - dp(i + x, max(m, x)))
            return best
        
        result = dp(0, 1)
        dp.cache_clear()
        return result