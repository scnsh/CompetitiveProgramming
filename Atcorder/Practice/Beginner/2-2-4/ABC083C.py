X, Y = map(int, input().split())

count = 0
while X <= Y:
    count += 1
    Y = Y // 2
print(count)
# max_count = 0
# for x in range(X, Y+1):
#     count = 0
#     val = x
#     while val <= Y:
#         count += 1
#         val *= 2
#     if max_count < count:
#         max_count = count
# print(max_count)
