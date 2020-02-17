from collections import deque

H, W = map(int, input().split())
c = [list(input()) for _ in range(H)]
cnt = [[float('inf') for _ in range(W)] for _ in range(H)]
moves = ((1, 0), (-1, 0), (0, 1), (0, -1))

for i in range(H):
    for j in range(W):
        if c[i][j] == 's':
            sy, sx = i, j
            cnt[sy][sx] = 0
        if c[i][j] == 'g':
            gy, gx = i, j


def bfs():
    dq = deque([(sy, sx)])
    while dq:
        y, x = dq.popleft()
        for dy, dx in moves:
            ny, nx = (y + dy, x + dx)
            if 0 <= ny < H and 0 <= nx < W and cnt[ny][nx] == float('inf'):
                if c[ny][nx] == '.' or c[ny][nx] == 'g':
                    cnt[ny][nx] = cnt[y][x] + 0
                    dq.appendleft([ny, nx])
                else:
                    cnt[ny][nx] = cnt[y][x] + 1
                    dq.append([ny, nx])


bfs()
if cnt[gy][gx] <= 2:
    print('YES')
else:
    print('NO')
