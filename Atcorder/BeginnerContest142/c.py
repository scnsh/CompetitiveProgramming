N = int(input())
h_list = list(map(int, input().split()))
h_list2 = [0]*N
for i in range(N):
    h_list2[h_list[i]-1] = i+1
print(" ".join(map(str, h_list2)))

