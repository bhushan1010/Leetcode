from typing import List
from bisect import bisect_left, bisect_right
class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        positions = []
        digits = []
        for i, ch in enumerate(s):
            d = int(ch)
            if d != 0:
                positions.append(i)
                digits.append(d)
        n = len(digits)
        P = [0] * (n + 1)   # value of concatenation mod MOD
        S = [0] * (n + 1)   # sum of digits mod MOD
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            P[i] = (P[i-1] * 10 + digits[i-1]) % MOD
            S[i] = (S[i-1] + digits[i-1]) % MOD
            pow10[i] = (pow10[i-1] * 10) % MOD
        answer = []
        for l, r in queries:
            a = bisect_left(positions, l)
            b = bisect_right(positions, r)
            count = b - a
            if count == 0:
                answer.append(0)
                continue
            x = (P[b] - P[a] * pow10[count]) % MOD
            total_sum = (S[b] - S[a]) % MOD
            ans = (x * total_sum) % MOD
            answer.append(ans)
        return answer