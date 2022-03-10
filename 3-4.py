# n, k 입력
n, k = map(int, input().split())

# n이 k로 나머지 없이 나눠지는지 여부 확인에 따라 계속 반복
cnt = 0
while(n > 1) :
    if n%k == 0 :
        n = n/k
        cnt += 1
    else :
        n = n-1
        cnt += 1

print(cnt)