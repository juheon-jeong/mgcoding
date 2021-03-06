num = int(input())

d = [0] * 30001     # DP table

for i in range(2, num + 1):  # 문제가 1로 만드는 것이므로 0 1의 값은 신경 쓸 필요 없음.
    d[i] = d[i-1] + 1

    if i % 2 == 0:           # 2로 나누는 경우 횟수가 1 증가 하므로 이와 기존 값과 비교하여 최소값 고려
        d[i] = min(d[i], d[int(i/2)] + 1)
    if i % 3 == 0:           # 3로 나누는 경우 횟수가 1 증가 하므로 이와 기존 값과 비교하여 최소값 고려
        d[i] = min(d[i], d[int(i/3)] + 1)
    if i % 5 == 0:           # 5로 나누는 경우 횟수가 1 증가 하므로 이와 기존 값과 비교하여 최소값 고려
        d[i] = min(d[i], d[int(i/5)] + 1)

print(d[num])




