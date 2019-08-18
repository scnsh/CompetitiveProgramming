N = int(input())
V = list(map(int, input().split()))
V.sort()
v_sum = (V[0]+V[1]) / (2**(len(V)-1))
for i in range(2, len(V)):
  v_sum += V[i] / (2**(len(V)-i))
print(v_sum)