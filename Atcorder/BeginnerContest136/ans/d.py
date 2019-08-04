S = list(input().split('LR')) #map(lambda s:1 if s=='L' else -1, input().split())
lenS = len(S)
ret=""
for i in range(lenS):
  if lenS > 1:
    if i==0:
      S[i] = S[i]+'L'
    elif i==lenS-1:
      S[i] = 'R'+S[i]
    else:
      S[i] = 'R'+S[i]+'L'
  lenSi=len(S[i])
  r_count=S[i].count('R') 
  l_count=S[i].count('L')
  odd=(r_count+l_count) // 2
  even=odd
  if lenSi%2>0:
    odd += 1
  if r_count%2 > 0:
    r=odd
    l=even
  else:
    r=even
    l=odd
  tmp = [0]*lenSi
  tmp[r_count-1]=r
  tmp[r_count]=l
  ret += ' ' + ' '.join(str(e) for e in tmp)
print(ret)