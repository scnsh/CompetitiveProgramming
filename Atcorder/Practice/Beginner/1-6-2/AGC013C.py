N, L, T = map(int, input().split())
ants = []
touch = 0  # すべての蟻が0を通る合計数

for i in range(N):
    x, w = map(int, input().split())
    if w == 1:  # 時計回り
        touch += (x + T) // L  # 0を通る回数
        x1 = (x + T) % L       # 最終的な座標
    else:
        touch += (x - T) // L  # 0を通る回数
        x1 = (x - T) % L
    ants.append(x1)
touch = touch % N  # 0にいた蟻のindex
ants.sort()
ants = ants[touch:]+ants[:touch]

print(" ".join(map(str, ants)))

