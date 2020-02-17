from collections import deque
import copy

H, W = map(int, input().split())
s = (0, 0)
g = (H-1, W-1)
maze = [list(input()) for line in range(H)]
copied_maze = copy.deepcopy(maze)


def search(x, y):
    dq = deque()
    dq.append([x, y])
    copied_maze[x][y] = 0
    while len(dq) > 0:
        x, y = dq.popleft()
        if x == g[0] and y == g[1]:
            break
        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nx, ny = [x+dx, y+dy]
            if 0 <= nx < H and 0 <= ny < W and copied_maze[nx][ny] != '#' and type(copied_maze[nx][ny]) is str:
                dq.append([nx, ny])
                copied_maze[nx][ny] = copied_maze[x][y]+1


search(s[0], s[1])
x, y = g
cost = copied_maze[g[0]][g[1]]
if type(cost) is str:
    print(-1)
    exit()
path = {s, g}
for i in range(copied_maze[g[0]][g[1]]):
    for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        nx, ny = [x+dx, y+dy]
        if 0 <= nx < H and 0 <= ny < W and copied_maze[nx][ny] == cost - 1:
            path.add((nx, ny))
            x, y = nx, ny
            cost -= 1
            break
count = 0
for i in range(H):
    for j in range(W):
        if maze[i][j] == '.' and (i, j) not in path:
            count += 1
print(count)
