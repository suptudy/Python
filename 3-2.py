# N, M, K를 공백으로 구분하여 입력 받기
n, m, k = map(int, input().split())
print("입력값 확인",n,m,k)

# data들을 공백으로 구분하여 리스트로 입력 받기
data = list(map(int, input().split()))

# data 정렬 (내림차순)
data.sort(reverse=True)
print(data)

# 가장 큰 값 구하기 : sort된 data에서 첫번째, 두번째 값만 필요
sum = 0 # 초기화
first = data[0]
second = data[1]

# first k번, second 1번 반복됨을 이용
while m>0:
    for i in range(k):
        m -= 1
        sum += first
    sum += second
    m -= 1
    print("중간결과", sum)
