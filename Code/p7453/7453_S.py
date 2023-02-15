n = int(input())

answer = 0
A, B, C, D = [], [], [], []
for i in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

ab = dict()
for a in A:
    for b in B:
        sum_num = a + b
        if sum_num not in ab.keys():
            ab[sum_num] = 1
        else:
            ab[sum_num] += 1
# 배열 A와 배열 B를 더해 나올 수 있는 모든 값들을 딕셔너리 형식으로 정리

for c in C:
    for d in D:
        sum_num = -1 * (c + d)
        if sum_num in ab.keys():
            answer += ab[sum_num]
# 배열 C와 배열 D를 더해 나올 수 있는 모든 값들 중에 -를 붙인 값이
# 위의 딕셔너리에 존재한다면, 그것이 0이 되는 경우
print(answer)


