N, K = map(int, input().split())
h_list = list(map(int, input().split()))
h_list.sort()
for i in range(N):
    if h_list[i] >= K:
        print(N-i)
        exit(0)
print(0)
