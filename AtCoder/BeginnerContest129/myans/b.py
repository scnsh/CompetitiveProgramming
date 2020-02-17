N = int(input())
W = list(map(int, input().split()))

l = W[0]
r = sum(W[1:])
diff = abs(l - r)
for i in range(1, N):
    l += W[i]
    r -= W[i]
    new_diff = abs(l - r)
    if new_diff < diff:
        diff = new_diff
print(diff)
