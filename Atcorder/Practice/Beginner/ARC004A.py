import math

N = int(input())
xys = []
max_dist = 0
for _ in range(N):
  new_xy = list(map(int, input().split()))
  for xy in xys:
    dist = (xy[0] - new_xy[0])**2 + ((xy[1] - new_xy[1])**2)
    if max_dist < dist:
      max_dist = dist
  xys.append(new_xy)
print(math.sqrt(max_dist))