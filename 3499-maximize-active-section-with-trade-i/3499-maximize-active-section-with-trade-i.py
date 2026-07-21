class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        t = '1' + s + '1'
        n = len(t)
        runs = []
        i = 0
        while i < n:
            j = i
            while j < n and t[j] == t[i]:
                j += 1
            runs.append((t[i], j - i))
            i = j
        total_ones = s.count('1')
        m = len(runs)
        max_zero = 0
        min_one = float('inf')
        best_merge = 0
        for idx in range(m):
            ch, length = runs[idx]
            if ch == '0':
                if length > max_zero:
                    max_zero = length
            else:
                if 0 < idx < m - 1:
                    if length < min_one:
                        min_one = length
                    left_zero = runs[idx - 1][1]
                    right_zero = runs[idx + 1][1]
                    merge_gain = left_zero + right_zero
                    if merge_gain > best_merge:
                        best_merge = merge_gain
        best_independent = 0
        if min_one != float('inf') and max_zero > 0:
            best_independent = max_zero - min_one
        best_gain = max(0, best_independent, best_merge)
        return total_ones + best_gain