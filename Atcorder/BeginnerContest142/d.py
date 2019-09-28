A, B = map(int, input().split())
if A == B == 1:
    print(1)
    exit(0)


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return set([val[0] for val in arr])

print(len(factorization(A) & factorization(B))+1)
