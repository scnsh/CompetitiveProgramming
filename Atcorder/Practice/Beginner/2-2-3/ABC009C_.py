from collections import Counter

N, K = map(int, input().split())
S = list(input())
ordered_s = sorted(S)
candidate = ""

diff = 0
counter = Counter(S[:1])
counts = sum(counter.values())

for i in range(N):
    for c in ordered_s:
        diff1 = diff + (c != S[i])
        diff2 = counts - (counter[c] > 0)

        if diff1+diff2 <= K:
            candidate += c
            ordered_s.remove(c)
            diff = diff1
            counter = Counter(S[:i+2]) - Counter(candidate)
            counts = sum(counter.values())
            break
print(candidate)
