from collections import deque
import copy

H, W = map(int, input().split())
s = list(map(int, input().split()))
g = list(map(int, input().split()))
maze = [list(input()) for line in range(H)]
copied_maze = copy.deepcopy(maze)


def search(x, y):
    dq = deque()
    dq.append([x, y])
    copied_maze[x][y] = 0
    while len(dq) > 0:
        x, y = dq.popleft()
        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nx, ny = [x+dx, y+dy]
            if 0 <= nx < H and 0 <= ny < W and copied_maze[nx][ny] != '#' and type(copied_maze[nx][ny]) is str:
                dq.append([nx, ny])
                copied_maze[nx][ny] = copied_maze[x][y]+1


search(s[0]-1, s[1]-1)
print(copied_maze[g[0]-1][g[1]-1])
