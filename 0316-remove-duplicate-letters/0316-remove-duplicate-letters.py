class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurrence = {c: i for i, c in enumerate(s)}
        stack = []
        seen = set()
        for i, c in enumerate(s):
            if c in seen:
                continue
            while stack and stack[-1] > c and i < last_occurrence[stack[-1]]:
                seen.remove(stack.pop())
            stack.append(c)
            seen.add(c)
        return ''.join(stack)