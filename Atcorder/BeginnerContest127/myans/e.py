import itertools


def cost(c, N):


N, M, K = map(int, input().split())
comb = list(itertools.combinations(range(N*M), K))
sum = 0
print(comb)
for c in comb:
    sum += abs(c[0]//N - c[1]//N) + abs(c[0] % N - c[1] % N)
    print(c[0]//N, c[1]//N, c[0] % N, c[1] %
          N, abs(c[0]//N - c[1]//N) + abs(c[0] % N - c[1] % N))
print(sum)
