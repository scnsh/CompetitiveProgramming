N = int(input())
A_list = list(map(int, input().split()))
sorted_A_list = sorted(A_list)
if sorted_A_list[-1] < 0:
  base = sorted_A_list[-1] - sorted_A_list[i]
else:
  base = sorted_A_list[-1] - sorted_A_list[i]
elif sorted_A_list[-1] < 0:
  base = sorted_A_list[i] - sorted_A_list[i]

for i in range(N/2):
  if sorted_A_list[i] < 0:
    minus = sorted_A_list[i] - sorted_A_list[N-i] 