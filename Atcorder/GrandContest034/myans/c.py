N, X = map(int, input().split())

data = []
for _ in range(N):
    b, l, u = map(int, input().split())
    if len(data) == 0:
        data.append([X-b, l, u])
    else:
        if u > data[0][2]:
            data[0:0] = [[X-b, l, u]]
        else:
            data[1:1] = [[X-b, l, u]]
print(data)
