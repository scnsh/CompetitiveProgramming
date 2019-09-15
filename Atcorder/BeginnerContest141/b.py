S = list(input())
for i in range(len(S)):
    if (i+1)%2 == 0:
        if S[i]=='R':
            print("No")
            exit(0)
    if (i+1)%2 != 0:
        if S[i]=="L":
            print("No")
            exit(0)
print("Yes")
