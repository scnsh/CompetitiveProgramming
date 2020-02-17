# https://snuke.hatenablog.com/entry/2014/12/03/214243

N = int(input())
S = input()

r=0
i=j=0
while j < N:
    t = S[i:j]
    if t in S[j:]:
        r = max(r, j-i)
        j += 1
    else:
        i += 1
print(r)
