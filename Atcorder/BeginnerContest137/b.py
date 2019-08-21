K, X = map(int, input().split())
out_list = []
for i in range(X-(K-1), X+(K)):
    out_list.append(str(i))
print(" ".join(out_list))
