class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        rank = [0] * n
        
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            if rank[rx] < rank[ry]:
                rx, ry = ry, rx
            parent[ry] = rx
            if rank[rx] == rank[ry]:
                rank[rx] += 1
        
        for a, b in edges:
            union(a, b)
        
        vertex_count = [0] * n
        edge_count = [0] * n
        
        for i in range(n):
            root = find(i)
            vertex_count[root] += 1
        
        for a, b in edges:
            root = find(a)
            edge_count[root] += 1
        
        count = 0
        for i in range(n):
            if find(i) == i:
                v = vertex_count[i]
                e = edge_count[i]
                if e == v * (v - 1) // 2:
                    count += 1
        
        return count