from collections import deque
from typing import List


class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])

        litter = {}
        start = None
        count = 0

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i, j)

                elif classroom[i][j] == 'L':
                    litter[(i, j)] = count
                    count += 1

        target = (1 << count) - 1

        queue = deque()
        queue.append((start[0], start[1], energy, 0, 0))

        best = [[[-1] * (1 << count) for _ in range(n)] for _ in range(m)]
        best[start[0]][start[1]][0] = energy

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            r, c, remaining, mask, moves = queue.popleft()

            if mask == target:
                return moves

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                if classroom[nr][nc] == 'X':
                    continue

                new_energy = remaining - 1

                if new_energy < 0:
                    continue

                new_mask = mask

                if (nr, nc) in litter:
                    new_mask |= 1 << litter[(nr, nc)]

                if classroom[nr][nc] == 'R':
                    new_energy = energy

                if best[nr][nc][new_mask] >= new_energy:
                    continue

                best[nr][nc][new_mask] = new_energy

                queue.append(
                    (nr, nc, new_energy, new_mask, moves + 1)
                )

        return -1