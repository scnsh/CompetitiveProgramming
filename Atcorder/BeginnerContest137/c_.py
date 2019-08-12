N = int(input())
words_dict = {}
count = 0
for i in range(N):
  ss = input()
  ss = "".join(sorted(ss))
  words_dict.setdefault(ss, 0)
  count += words_dict[ss]
  words_dict[ss] += 1
print(count)