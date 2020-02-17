m = int(input())
charge = 1000-m

coin_sum = 0
for coin in (500, 100, 50, 10, 5, 1):
    count = charge // coin
    charge = charge - coin*count
    coin_sum += count
print(coin_sum)
