import copy
s = input()
t = input()
if(set(t) - set(s)):
  print(-1)
  exit()

t_index = 0
s_index = 0
count = 0
copy_s = copy.deepcopy(s)
while len(t) > t_index:
  index = copy_s.find(t[t_index])
  if index >= 0:
    t_index+=1
    copy_s = copy_s[index+1:]
  else:
    copy_s = copy.deepcopy(s)    
    count += 1
print(count*len(s)+len(s)-len(copy_s))