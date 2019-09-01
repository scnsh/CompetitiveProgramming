T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

for i in range(M):
    available = []
    for j in range(len(A)):
        if T >= B[i] - A[j] >= 0:
            available.append(j)
    if len(available) > 0:
        sold = available.pop(0)
        A.pop(sold)
    else:
        print('no')
        exit(0)
print('yes')
