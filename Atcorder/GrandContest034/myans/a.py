N, A, B, C, D = map(int, input().split())
S = "." + input() + "."

def move_b():
  i = B
  keep_next_to_lock = (S[i+1] == "#" or S[i-1] == "#")
  while i != D:
    if S[i+1] == ".":
      i += 1
      keep_next_to_lock = keep_next_to_lock & (S[i+1] == "#" or S[i-1] == "#")
    elif S[i+1] == "#" and S[i+2] ==".":
      i += 2
    else:
      return False
  return True and not (keep_next_to_lock and D < C)

def check_a_b():
  for i in range(A, B-1):
    if S[i+1] == "#" and S[i+2] == "#":
      return False
  return True

if move_b() and check_a_b():
  print('Yes')
else:
  print('No')
