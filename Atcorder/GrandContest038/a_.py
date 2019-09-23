H, W, A, B = map(int, input().split())
mat=[[0]*W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if i >= B and A > j:
            mat[i][j] = 1
        elif i < B and j >= A:
            mat[i][j] = 1
    print("".join(map(str, mat[i])))
