N = int(input())
A = list(map(int, input().split()))
a_all = 1
a_sum = 0
for i in A:
    a_all *= i
for i in A:
    a_sum = a_sum + a_all / i
print(a_all/a_sum)
