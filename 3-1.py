money = [500,100,50,10]
count = 0

n = int(input("거스름돈을 입력하세요:"))
for coin in money:
    count += n // coin
    n %= coin

print(count)