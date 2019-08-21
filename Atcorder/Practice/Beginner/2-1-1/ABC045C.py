S = input()
len_s = len(S)-1
count = 0
ss = []
for i in range(2**len_s):
    binary = format(i, 'b').zfill(len_s+2)[2:]
    tmp = [S[0]]
    for j in range(len(binary)):
        if binary[j] == '1':
            tmp.append(S[j+1])
        else:
            tmp[-1] = tmp[-1]+S[j+1]
    count += sum(int(i) for i in tmp)
print(count)
