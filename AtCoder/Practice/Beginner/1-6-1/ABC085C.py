N, Y = map(int, input().split())
out_x = out_y = out_z = -1
for x in range(N+1):
    for y in range(N+1):
        price = x * 10000 + y * 5000
        if price > Y:
            break
        price = price + (N-x-y) * 1000
        if price == Y:
            out_x = x
            out_y = y
            out_z = N-x-y
            break
    if out_x != -1:
        break
print("{0} {1} {2}".format(out_x, out_y, out_z))
