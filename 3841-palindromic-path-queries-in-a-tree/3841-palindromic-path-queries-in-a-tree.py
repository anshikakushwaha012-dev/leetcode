class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        from collections import defaultdict
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        tin = [0] * n
        tout = [0] * n
        parent = [-1] * n
        depth = [0] * n
        order = []
        stack = [(0, -1, 0)]
        while stack:
            u, p, state = stack.pop()
            if state == 0:
                tin[u] = len(order)
                order.append(u)
                stack.append((u, p, 1))
                for v in reversed(adj[u]):
                    if v != p:
                        parent[v] = u
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = len(order)
        LOG = n.bit_length()
        up = [parent[:]]
        up[0][0] = 0
        for j in range(1, LOG):
            prev = up[-1]
            up.append([prev[prev[i]] for i in range(n)])
        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            bit = 0
            while diff:
                if diff & 1:
                    u = up[bit][u]
                diff >>= 1
                bit += 1
            if u == v:
                return u
            for j in range(LOG - 1, -1, -1):
                if up[j][u] != up[j][v]:
                    u = up[j][u]
                    v = up[j][v]
            return parent[u]
        bit = [0] * (n + 1)
        def add(i, val):
            i += 1
            while i <= n:
                bit[i] ^= val
                i += i & -i
        def prefix(i):
            result = 0
            while i > 0:
                result ^= bit[i]
                i -= i & -i
            return result
        def range_xor(left, right):
            return prefix(right) ^ prefix(left)
        chars = [1 << (ord(c) - ord('a')) for c in s]
        for u in range(n):
            add(tin[u], chars[u])
            add(tout[u], chars[u])
        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                new_mask = 1 << (ord(c) - ord('a'))
                delta = chars[u] ^ new_mask
                if delta:
                    add(tin[u], delta)
                    add(tout[u], delta)
                    chars[u] = new_mask
            else:
                u = int(parts[1])
                v = int(parts[2])
                w = lca(u, v)
                mask_u = range_xor(0, tin[u] + 1)
                mask_v = range_xor(0, tin[v] + 1)
                mask_w = chars[w]
                mask = mask_u ^ mask_v ^ mask_w
                ans.append((mask & (mask - 1)) == 0)
        return ans