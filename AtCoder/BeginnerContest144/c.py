N = int(input())


def make_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    divisors.sort()
    return divisors


divs = make_divisors(N)
if N // divs[len(divs) // 2] == divs[len(divs) // 2]:
    i = len(divs) // 2
else:
    i = len(divs) // 2 - 1
print(divs[i]-1 + N // divs[i]-1)
