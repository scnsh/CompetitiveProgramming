s  = input()
a = int(s[:2])
b = int(s[2:])
is_MMxx = is_xxMM = False
if 13 > a > 0:
  is_MMxx = True
if 13 > b > 0:
  is_xxMM = True
if is_MMxx and is_xxMM:
  print("AMBIGUOUS")
elif is_MMxx:
  print("MMYY")
elif is_xxMM:
  print("YYMM")
else:
  print("NA")