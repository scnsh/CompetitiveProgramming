import heapq

N, M = map(int, input().split())
A = [-int(x) for x in input().split()]
heapq.heapify(A)
for i in range(M):
    x = heapq.heappop(A)
    x = int(x / 2)
    heapq.heappush(A, x)  # pop minimum
print(-sum(A))
