N = int(input())
S = input()
new_S = ""

last_s = ""
for s in S:
    if s is not last_s:
        new_S += s
    last_s = s
print(len(new_S))
