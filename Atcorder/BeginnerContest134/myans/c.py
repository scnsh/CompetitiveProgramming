N = int(input())
A = MAX = [0]*N
max_1 = max_2 = index = 0
for i in range(N):
  A[i] = int(input())
  if A[i] >= max_1:
    max_2 = max_1
    max_1 = A[i]
  elif A[i] > max_2:
    max_2 = A[i]
for i in range(N):
  if A[i] == max_1:
    print(max_2)
  else:
    print(max_1)
#   if max_1 > A[i] or max_1 == A[i] and index != i:
#     if A[i] > max_2:
#       max_2 = A[i]
#     MAX[i] = max_1
#   else:
#     index = i
#     max_2 = max_1
#     max_1 = A[i]
# for i in range(N)[::-1]:
#   if max_1 > A[i]:
#     MAX[i] = max_1
#   elif max_1 == A[i] and index != i:
#     MAX[i] = max_2
# print(MAX)