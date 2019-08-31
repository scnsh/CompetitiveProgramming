S = input()
T = input()
s_list = []
for i in range(len(S)):
    if i+len(T) > len(S):
        break
    j=0
    for _ in range(len(T)):
        if S[i+j] == '?' or S[i+j] == T[j]:
            j+=1
            continue
        break
    if j==len(T):
        s_list.append(S[:i] + T + S[i+len(T):])
if len(s_list) > 0:
    s_list.sort()
    print(s_list[0].replace('?', 'a'))
else:
    print("UNRESTORABLE")


