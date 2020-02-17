from collections import deque

N = int(input())
A = [0] + list(deque(map(int, input().split())) for i in range(N))
cnt, cur, days = 0, [0]*(N+1), [0]*(N+1)
q = deque(list(range(1, N+1)))
while q:
    x = q.popleft()
    if not A[x]:
        continue
    y = A[x].popleft()
    if cur[y] == x:
        cnt += 1
        days[x] = days[y] = max(days[x], days[y]) + 1
        cur[x], cur[y] = 0, 0
        q.append(x), q.append(y)
    else:
        cur[x] = y
flg = cnt == N * (N - 1) // 2
print(max(days) if flg else -1)
