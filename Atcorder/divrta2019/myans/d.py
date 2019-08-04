count = 0
n = int(input())
for m in range(1, int(n**0.5)+1):
  if n % m == 0 and m < (n//m - 1):
      count += n//m-1
print(count)