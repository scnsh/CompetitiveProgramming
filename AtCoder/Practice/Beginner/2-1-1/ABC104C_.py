D, G = map(int, input().split())
c = [0]+[list(map(int, input().split())) for i in range(D)]


def f(t, s):
    if t == 0:
        return 10**9
    # 点数が高いものを解けるだけとく
    # 問題数or目標点数を満たす数
    l = min(s//(t*100), c[t][0])
    k = 100*t*l

    # ボーナスを加味
    if l == c[t][0]:
        k += c[t][1]
    # 目標まで足りていないならその下の点数について再帰
    if k < s:
        l += f(t-1, s-k)
    # その下の点数について再帰（ボーナスを加味するため）
    return min(l, f(t-1, s))


print(f(D, G))
