n, k = map(int, input().split())
count = 0
for i in range(1, n+1):
    if i+k <= n+1:
        count += 1
print(count)
