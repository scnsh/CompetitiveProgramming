strN = input()
keta, N = len(strN), int(strN)
if keta > 1:
  amari = N - (10**(keta-1))
  count = 0
  for i in range(1, keta):
    if i%2!=0:
      if i==1:
        count += 9
      else:
        count += (10**i) - (10**(i-1))  
  if keta%2!=0:
    count += amari+1
  print(count)
else:
  print(N)