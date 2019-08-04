import re

S = re.split('[BC]', input().replace("BC","D"))

# def change(s, i):
#   global tmp
#   if s[i:i+2] == "AD":
#     s = s[:i] + "DA" + s[i+2:]
#     if i > 0 and S[i-1] == "A":
#       s, tmp = change(s, i-1)
#       return s, 1+tmp
#     return s, 1+tmp
#   return s, 0

def solve(s):
  ans = tmp = 0
  for char in s:
    if char == "A":
      tmp += 1
    else:
      ans += tmp
  return ans
  
ans = 0
for ele in S:
  ans += solve(ele)
print(ans)