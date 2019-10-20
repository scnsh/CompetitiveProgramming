N = int(input())
d_list = list(map(int, input().split()))

total = 0
for i in range(0, N):
    for j in range(i+1, N):
        total += d_list[i]*d_list[j]
print(total)
