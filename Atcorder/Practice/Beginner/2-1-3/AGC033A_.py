from collections import deque
import copy

def main():
  H, W = map(int, input().split())
  maps = [[j=="#" for j in input()] for i in range(H)]
  q = deque([(i, j) for i in range(H) for j in range(W) if maps[i][j]])
  count = 0
  while True:
    nq = deque()
    while q:
      x, y = q.popleft()
      if x > 0 and not maps[x-1][y]:
        maps[x-1][y] = True
        nq.append((x-1,y))
      if y > 0 and not maps[x][y-1]:
        maps[x][y-1] = True
        nq.append((x,y-1))
      if x < H-1 and not maps[x+1][y]:
        maps[x+1][y] = True
        nq.append((x+1,y))
      if y < W-1 and not maps[x][y+1]:
        maps[x][y+1] = True
        nq.append((x,y+1))
    if nq:
      q = copy.copy(nq)
    else:
        break
    count += 1
  print(count)

if __name__ == "__main__":
  main()