# n,m을 공백을 이용해 입력 받기
n, m = map(int, input().split())

# 행렬 한줄씩 입력받아 확인
answer = 0
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 데이터에서 가장 작은 수
    min_data = min(data)
    # 가장 작은 수들 중에서 가장 큰 수 찾기
    answer = max(answer, min_data)

print(answer)