N, M = map(int, input().split())
set_list = []
for i in range(M):
    x, y = map(int, input().split())
    set_list.append({x, y})
max_num = 1
for i in range(2**N):
    binary = format(i, 'b').zfill(N+2)[2:]
    group = []
    for j in range(N):
        if binary[j] == '1':
            group.append(j+1)
    failed = False
    for t in range(len(group)):
        for s in range(t+1, len(group)):
            if {group[t], group[s]} not in set_list:
                failed = True
                break
        if failed:
            break
    if not failed and max_num < len(group):
        max_num = len(group)
print(max_num)
