n = int(input())
p = list(map(int, input().split()))
index_list = []
value_list = []
for i in range(1, n+1):
    if i != p[i-1]:
        index_list.append(i)
        value_list.append(p[i-1])
if len(index_list) == 0:
    print("YES")
elif len(index_list) == 2 and value_list[0] == index_list[1] and value_list[1] == index_list[0]:
    print("YES")
else:
    print("NO")
