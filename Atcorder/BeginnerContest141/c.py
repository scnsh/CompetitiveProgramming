N, K, Q = map(int, input().split())
A =[0]*N
P = [K]*N
for i in range(Q):
    p = int(input())
    A[p-1]+=1

for i in range(N):
    if K - (Q-A[i]) > 0:
        print("Yes")
    else:
        print("No")

