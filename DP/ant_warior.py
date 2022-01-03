n = int(input())

space = list(map(int, input().split()))  # 입력값을 리스트 배열로 저장

d = [0] * 100           # 식량창고 개수가 최대 100개 이므로 DP table 초기화

d[0] = space[0]
d[1] = max(d[0], space[1])      # 0번쨰 index 값과 비교하여 최대값으로 저장

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + space[i])       # i-1번째 값, i-2번째 값 + 현재 식량창고값 을 비교하여 더 큰 값을 저장.

print(d[n-1])

