from collections import deque
import copy

maze = [list(input()) for _ in range(10)]
copied_maze = copy.deepcopy(maze)

def dfs(x, y):
  dq = deque()
  dq.append([x, y])
  copied_maze[x][y] = 'o'
  while len(dq) > 0:
    x,y = dq.pop()
    for dx, dy in [[1,0], [0,1], [-1,0], [0,-1]]:
      nx, ny = [x+dx, y+dy]
      if 0 <= nx < 10 and 0 <= ny < 10 and copied_maze[nx][ny] != 'x':
        dq.append([nx,ny])
        copied_maze[nx][ny] = "x"

def check(maze):
  for line in maze:
    if 'o' in line:
      return False
  return True

for x in range(10):
  for y in range(10):
    if maze[x][y] == 'x':
      copied_maze = copy.deepcopy(maze)
      dfs(x,y)
      if check(copied_maze):
        print('YES')
        exit()
print('NO')
