# import copy

# h, w = list(map(int, input().split()))
# black_list = []
# white_list = []
# for i in range(h):
#   for j, val in enumerate(list(input())):
#     if val == "#":
#       black_list.append([i,j])
#     else:
#       white_list.append([i,j])
# max_val = 0
# for white in white_list:
#   min_val = w*h
#   for black in black_list:
#     diff = abs(white[0]-black[0]) + abs(white[1]-black[1])
#     if diff < min_val:
#       min_val = diff
#   if max_val < min_val:
#     max_val = min_val
# print(max_val)

import numpy


def main():
    height, width = map(int, input().split())
    max_value = height + width
    values = []

    for y in range(height):
        values.append([0 if v == '#' else max_value for v in input().strip()])

    values = numpy.array(values)

    for x in range(width - 1):
        a = values[:, x] + 1
        b = values[:, x + 1]
        values[:, x + 1] = numpy.minimum(values[:, x] + 1, values[:, x + 1])

    for x in range(width - 1, 0, -1):
        values[:, x - 1] = numpy.minimum(values[:, x] + 1, values[:, x - 1])

    for y in range(height - 1):
        values[y + 1, :] = numpy.minimum(values[y, :] + 1, values[y + 1, :])

    for y in range(height - 1, 0, -1):
        values[y - 1, :] = numpy.minimum(values[y, :] + 1, values[y - 1, :])

    print(numpy.max(values), flush=True)


if __name__ == '__main__':
    main()
