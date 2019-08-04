import copy

S = list(input().split('LR')) #map(lambda s:1 if s=='L' else -1, input().split())
lenS = len(S)
ret=""
for i in range(lenS):
  if i==0:
    S[i] = S[i]+'L'
  elif i==lenS-1:
    S[i] = 'R'+S[i]
  else:
    S[i] = 'R'+S[i]+'L'
  max_len=max(S[i].find('L'), S[i].rfind('R'))+1
  if max_len%2>0:
    max_len+=1
  lenSi=len(S[i])
  tmp = [1]*lenSi
  for _ in range(max_len):
    new_tmp = [0]*lenSi
    for j in range(lenSi):
      if S[i][j] == 'R':
        new_tmp[j+1] += tmp[j]
      else:
        new_tmp[j-1] += tmp[j]
    tmp = copy.deepcopy(new_tmp)
  ret += ' ' + ' '.join(str(e) for e in tmp)
print(ret)
