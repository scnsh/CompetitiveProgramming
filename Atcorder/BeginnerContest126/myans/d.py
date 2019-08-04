n = int(input())
even_list = []
odd_list = []
for _ in range(n):
  u, v, w = map(int, input().split())
  if w % 2 > 0:
    odd_list.add({u,v})
  else:
    even_list.add({u,v})

ga = []
for pair in even_list:
  if pair.key not in ga:
    ga.add(pair.key)
  if pair.value not in ga:
    ga.add(pair.value)
for pair in odd_list:
  if pair.key in ga:
    