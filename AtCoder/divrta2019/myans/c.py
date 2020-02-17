str_dict = [0, 0, 0]
val1 = 0
for i in range(int(input())):
    line = input()
    val1 += line.count('AB')
    if line[0] == 'B' and line[-1] == 'A':
        str_dict[2] += 1
    elif line[0] == 'B':
        str_dict[0] += 1
    elif line[-1] == 'A':
        str_dict[1] += 1
if str_dict[2] == 0:
    print(val1+min(str_dict[0], str_dict[1]))
else:
    if str_dict[0]+str_dict[1] > 0:
        print(val1+str_dict[2]+min(str_dict[0], str_dict[1]))
    else:
        print(val1+str_dict[2]-1)
