from collections import Counter

def comb_capped(n, r, cap):
    if r < 0 or r > n:
        return 0
    r = min(r, n - r)
    if r == 0:
        return 1
    result = 1
    for i in range(1, r + 1):
        result = result * (n - r + i) // i
        if result > cap:
            return cap + 1
    return result

def perm_count(counts, remaining, cap):
    pos = remaining
    total = 1
    for c, v in counts.items():
        if v <= 0:
            continue
        cv = comb_capped(pos, v, cap)
        if cv > cap:
            return cap + 1
        total *= cv
        if total > cap:
            return cap + 1
        pos -= v
    return total

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = Counter(s)
        odd_char = ''
        half_counts = {}
        for c, v in freq.items():
            if v % 2 == 1:
                odd_char = c
            half_counts[c] = v // 2

        half_length = sum(half_counts.values())

        total = perm_count(half_counts, half_length, k)
        if total < k:
            return ""

        half_result = []
        counts = dict(half_counts)
        remaining_k = k
        for _ in range(half_length):
            for c in sorted(counts.keys()):
                if counts[c] <= 0:
                    continue
                counts[c] -= 1
                remaining = half_length - len(half_result) - 1
                cnt = perm_count(counts, remaining, remaining_k)
                if cnt >= remaining_k:
                    half_result.append(c)
                    break
                else:
                    remaining_k -= cnt
                    counts[c] += 1

        half_str = ''.join(half_result)
        return half_str + odd_char + half_str[::-1]