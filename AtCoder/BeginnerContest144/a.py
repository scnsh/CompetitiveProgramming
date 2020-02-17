A, B = map(int, input().split())

if A > 9 or B > 9:
    print(-1)
    exit(0)
print(A*B)