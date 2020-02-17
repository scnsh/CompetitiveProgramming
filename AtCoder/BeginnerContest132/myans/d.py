import math

N, K = map(int, input().split())


def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


def permutations_count(n, r):
    return math.factorial(n) // math.factorial(n - r)


for i in range(1, K+1):
    if N - K + 1 < i:
        print(0)
    else:
        print((combinations_count(N-K+1, i) *
               combinations_count(K-1, i-1)) % (10**9 + 7))
