inf = 10000
T = int(input())

for _ in range(T):
    line = input()
    idx = 0
    count = 0
    while True:
        if line[idx:].find('tokyo') == -1 and line[idx:].find('kyoto') == -1:
            break
        count += 1
        t = line[idx:].find('tokyo')
        k = line[idx:].find('kyoto')
        if t < k and t != -1:
            idx += t + 5
        elif t >= k != -1:
            idx += k + 5
        else:
            if t != -1:
                idx += t+5
            else:
                idx += k + 5
        if idx >= len(line):
            break
    print(count)
