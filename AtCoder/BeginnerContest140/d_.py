N, K = map(int, input().split())
S = list(input())
Y = 0
if N == 1:
    print(0)
    exit(0)

if S[0] == 'L':
    Y += 1
if S[N-1] == 'R':
    Y += 1

count = 0
X = 0
for i in range(N-1):
    if S[i] == 'R' and S[i+1] == 'L':
        X += 1
    if S[i] == S[i+1]:
        count += 1

count += K*2
print(min(N-1, count))

