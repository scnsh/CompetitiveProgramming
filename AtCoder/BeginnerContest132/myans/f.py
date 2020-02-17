N, K = map(int, input().split())


def permutations_count(n, r):
    return math.factorial(n) // math.factorial(n - r)


permutations_count(K)
print(K)
