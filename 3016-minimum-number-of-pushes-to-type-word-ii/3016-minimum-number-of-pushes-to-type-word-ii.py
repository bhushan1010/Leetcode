class Solution:
    def minimumPushes(self, word: str) -> int:
        from collections import Counter
        freq = sorted(Counter(word).values(), reverse=True)
        total = 0
        for i, f in enumerate(freq):
            total += f * (i // 8 + 1)
        return total