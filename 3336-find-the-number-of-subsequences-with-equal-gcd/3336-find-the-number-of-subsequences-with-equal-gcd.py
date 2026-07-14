import math
from typing import List

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        maxv = 200
        
        dp = [[0] * (maxv + 1) for _ in range(maxv + 1)]
        dp[0][0] = 1
        
        gcd = math.gcd
        
        for x in nums:
            gx = [gcd(g, x) for g in range(maxv + 1)]
            new_dp = [row[:] for row in dp]
            for g1 in range(maxv + 1):
                row = dp[g1]
                new_row_g1_fixed = new_dp[g1]
                ng1 = gx[g1]
                target_row = new_dp[ng1]
                for g2 in range(maxv + 1):
                    c = row[g2]
                    if c == 0:
                        continue
                    target_row[g2] = (target_row[g2] + c) % MOD
                    ng2 = gx[g2]
                    new_row_g1_fixed[ng2] = (new_row_g1_fixed[ng2] + c) % MOD            
            dp = new_dp
        
        ans = 0
        for g in range(1, maxv + 1):
            ans = (ans + dp[g][g]) % MOD
        
        return ans