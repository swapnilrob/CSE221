import sys
from collections import deque

def knight_min_moves(n, x1, y1, x2, y2):
    moves = [(2, 1), (2, -1), (-2, 1), (-2, -1),
             (1, 2), (1, -2), (-1, 2), (-1, -2)]
    dist = [[-1] * (n + 1) for i in range(n + 1)]
    dist[x1][y1] = 0
    q = deque([(x1, y1)])

    while q:
        x, y = q.popleft()
        if (x, y) == (x2, y2):
            print(dist[x][y])
            return

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 1 <= nx <= n and 1 <= ny <= n and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

    print(-1)


input = sys.stdin.readline
n = int(input())
x1, y1, x2, y2 = map(int, input().split())
knight_min_moves(n, x1, y1, x2, y2)