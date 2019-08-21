# def conv(x):
#   if x == 'R':
#     return [0,1]
#   elif x == 'L':
#     return [0,-1]
#   elif x == 'U':
#     return [-1, 0]
#   elif x == 'D':
#     return [1,0]

# h, w, n = map(int, input().split())
# sr, sc = map(int, input().split())
# s = list(map(lambda x: conv(x), list(input())))
# t = list(map(lambda x: conv(x), list(input())))
# print(s)
# print(t)

# def takahashi(current_pos, index)
#     try_u = try_d = try_l = try_r = False
#     u = pos[0] < 0 for pos in s[index:]
#     if sum(u) + current_pos[0] > h:
#       try_u = True
#     d = pos[0] > 0 for pos in s[index:]
#     if sum(d) + current_pos[0] < 0:
#       try_d = True
#     l = pos[1] > 0 for pos in s[index:]
#     if sum(l) + current_pos[1] > w:
#       try_l = True
#     r = pos[1] < 0 for pos in s[index:]
#     if sum(u) + current_pos[1] < 0:
#       try_r = True
#     for i, pos in enumerate(s):
#       if try_u:
#         current_pos[i]

#   return offset

h, w, n = map(int, input().split())
sr, sc = map(int, input().split())
s = input()
t = input()
wr = sc
wl = sc
hu = sr
hd = sr


def taka(k, wr, wl, hu, hd):
    if k == 'U':
        hu -= 1
    if k == 'D':
        hd += 1
    if k == 'R':
        wr += 1
    if k == 'L':
        wl -= 1
    return wr, wl, hu, hd


def ao(k, wr, wl, hu, hd):
    if k == 'U':
        hd = max(1, hd-1)
    if k == 'D':
        hu = min(h, hu+1)
    if k == 'R':
        wl = min(w, wl+1)
    if k == 'L':
        wr = max(1, wr-1)
    return wr, wl, hu, hd


for i in range(n):
    wr, wl, hu, hd = taka(s[i], wr, wl, hu, hd)
    if wl == 0 or hu == 0 or hd == h+1 or wr == w+1:
        print('NO')
        exit()
    wr, wl, hu, hd = ao(t[i], wr, wl, hu, hd)
print('YES')
