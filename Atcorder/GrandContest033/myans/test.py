# a, b, t = map(int, input().split())
# print(t // a * b)

# n = int(input())
# v = map(int, input().split())
# c = map(int, input().split())
# max_val = 0
# for _v, _c in zip(v, c):
#   if _v - _c > 0:
#     max_val += _v - _c
# print(max_val)

# def gcd(a, b):
#   if b == 0:
#     return a
#   ret = gcd(b, a%b)
#   return ret

# n = int(input())
# a = list(map(int, input().split()))
# l = [0 for i in range(n)]
# r = l[:]

# for i in range(1, n):
#   l[i] = gcd(l[i-1], a[i-1])
#   r[-i-1] = gcd(r[-i], a[-i])
# ans = 0
# for i in range(n):
#   ans = max(ans, gcd(l[i], r[i]))
# print(ans)

n = int(input())
a = list(map(int, input().split()))

abs_a = list(map(abs, a[:]))
s = sum(abs_a[:])
m = len([i for i in a if i < 0])
if m % 2 == 0:
  print(s)
else:
  print(s - 2 * min(abs_a))