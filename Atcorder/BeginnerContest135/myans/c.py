n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b = sorted(b, reverse=True)

c = [0]*n
count = 0
for i in range(n):
    index = n-1
    for j in range(n):
        if a[index] + a[index+1] < a[j] + a[j+1] and c[j] == 0:
            index = j
    c[index] = b[i]
for i in range(n, 0, -1):
    tmp = c[i-1]
    new_a = a[i] - min(a[i], c[i-1])
    c[i-1] = c[i-1] - a[i] if c[i-1] - a[i] > 0 else 0
    new_a_1 = a[i-1] - min(a[i-1], c[i-1])
    c[i-1] = c[i-1] - a[i-1] if c[i-1] - a[i-1] > 0 else 0
    a[i-1], a[i] = new_a_1, new_a

    count += tmp - c[i-1]
print(count)

# # c = [0]*n
# count = 0
# for i in range(n):
#   index = 0
#   for j in range(n):
#     # if a[j] + a[j+1] <= b[i]:
#     if a[index] + a[index+1] < a[j] + a[j+1]:
#       index = j
#   b_org = b[i]
#   if a[index] > a[index+1]:
#     new_a = 0 if b[i] > a[index] else a[index] - b[i]
#     b[i] = b[i] - a[index] if b[i] >= a[index] else 0
#     new_a_1 = 0 if b[i]-a[index] > a[index+1] else a[index+1] - b[i]
#     b[i] = b[i] - a[index+1] if b[i] >= a[index+1] else 0
#     a[index], a[index+1] = new_a, new_a_1
#   else:
#     new_a_1 = 0 if b[i] > a[index+1] else a[index+1] - b[i]
#     b[i] = b[i] - a[index+1] if b[i] >= a[index+1] else 0
#     new_a = 0 if b[i]-a[index+1] > a[index] else a[index] - (b[i] - a[index+1])
#     b[i] = b[i] - a[index] if b[i] >= a[index] else 0
#     a[index], a[index+1] = new_a, new_a_1
#   count += b_org - b[i]
# print(count)
