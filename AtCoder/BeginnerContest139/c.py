N = int(input())
H = list(map(int, input().split()))

max_length = length = 0
for i in range(1, N):
    if H[i-1] >= H[i]:
        length += 1
    else:
        if max_length < length:
            max_length = length
        length = 0
print(max(max_length, length))
