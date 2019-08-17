import sys
sys.setrecursionlimit(1000000)

Y, X = map(int, input().split())

DX = [0, 1, 0, -1]
DY = [1, 0, -1, 0]

maps = [list(input()) for _ in range(Y)]
for y in range(Y):
  for x in range(X):
    if maps[y][x] == 's':
      start = (x,y)
    elif maps[y][x] == 'g':
      goal = (x,y)

def search(x, y):
  if (x, y) == goal:
    print('Yes')
    exit()
  for i in range(4):
    dx = DX[i]
    dy = DY[i]
    if X > x+dx > -1 and Y > y+dy > -1:
      if maps[y+dy][x+dx] != '#':
        maps[y+dy][x+dx] = '#'
        search(x+dx, y+dy)


search(start[0], start[1])
print('No')