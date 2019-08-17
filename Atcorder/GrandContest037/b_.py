import copy
N = int(input())
S = list(input())
length = len(S)
copyS = copy.deepcopy(S)

def find(start, current):
  global copyS
  candidate = 'RGB'.replace(current,'')
  copyS[start] = 'x'
  pos = [start]
  for j in range(max(length-start, start-0)):
    if length>(start+j) and copyS[start+j] in candidate:
      candidate = candidate.replace(copyS[start+j],'')
      copyS[start+j] = 'x'
      pos.append(start+j)
      if len(candidate) == 0: 
        break
    if (start-j)>0 and copyS[start-j] in candidate:
      candidate = candidate.replace(copyS[start-j],'')
      copyS[start-j] = 'x'
      pos.append(start-j)
      if len(candidate) == 0: 
        break
  return pos

for i in range(length):
  copyS = copy.deepcopy(S)
  diffs = 0
  for j in range(length):
    if copyS[j] != 'x':
      ret = find(j, copyS[j])
      diffs += max(ret)-min(ret)
      # print(copyS)
  print(diffs)