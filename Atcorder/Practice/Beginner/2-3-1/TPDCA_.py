N = int(input())
points = list(map(int, input().split()))
dp = [0] * (N+1)
ans = {0}

for i in range(N):
    tmp = set(map(lambda x: x+points[i], ans))
    ans |= tmp

print(len(ans))
