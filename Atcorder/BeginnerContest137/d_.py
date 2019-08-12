import heapq

N, M = map(int, input().split())
jobs = [[] for i in range(M)]

for i in range(N):
  a, b = map(int, input().split())
  if a > M:
    continue
  jobs[M-a].append(b)
sum_salary = 0
h=[]
for i in range(M-1, -1, -1):
  for b in jobs[i]:
    heapq.heappush(h,-b)
  if(len(h)!=0):
    a = -heapq.heappop(h)
    sum_salary += a
print(sum_salary)