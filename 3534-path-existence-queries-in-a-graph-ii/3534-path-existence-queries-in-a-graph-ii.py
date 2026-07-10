class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        order = sorted(range(n), key=lambda i: nums[i])
        rank = [0] * n
        sorted_vals = [nums[i] for i in order]
        for pos, idx in enumerate(order):
            rank[idx] = pos
        
        comp = [0] * n
        comp_start = 0
        for pos in range(n):
            if pos > 0 and sorted_vals[pos] - sorted_vals[pos - 1] > maxDiff:
                comp_start = pos
            comp[pos] = comp_start
        
        reach = [0] * n
        j = 0
        for i in range(n):
            if j < i:
                j = i
            while j + 1 < n and sorted_vals[j + 1] - sorted_vals[i] <= maxDiff:
                j += 1
            reach[i] = j
        
        LOG = max(1, n.bit_length())
        up = [[0] * n for _ in range(LOG)]
        up[0] = reach
        for k in range(1, LOG):
            prev = up[k - 1]
            cur = up[k]
            for i in range(n):
                cur[i] = prev[prev[i]]
        
        answer = []
        for u, v in queries:
            l, r = rank[u], rank[v]
            if l > r:
                l, r = r, l
            if comp[l] != comp[r]:
                answer.append(-1)
                continue
            if l == r:
                answer.append(0)
                continue
            steps = 0
            cur = l
            for k in range(LOG - 1, -1, -1):
                if up[k][cur] < r:
                    cur = up[k][cur]
                    steps += (1 << k)
            steps += 1
            answer.append(steps)
        
        return answer