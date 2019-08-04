S = input()
is_no = False
for s in S:
  if S.count(s) != 2:
    is_no = True
    break
if is_no:
  print("No")
else:
  print("Yes")
