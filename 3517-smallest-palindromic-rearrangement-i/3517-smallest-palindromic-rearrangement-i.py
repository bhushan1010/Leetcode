from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        cnt = Counter(s)
        half = []
        mid = ''
        for c in sorted(cnt.keys()):
            freq = cnt[c]
            if freq % 2 == 1:
                mid = c
            half.append(c * (freq // 2))
        half_str = ''.join(half)
        return half_str + mid + half_str[::-1]