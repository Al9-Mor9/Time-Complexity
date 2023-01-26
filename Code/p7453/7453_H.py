# ABCD 합이 0이려면 아무렇게나 2개씩 나눠도 합이 반대여야 한다
# 그래서 걍 ab, cd로 나눔
# pypy3로 돌리니까 정답 떴음
n = int(input())
A, B, C, D = [],[],[],[]
cnt = 0
for i in range(n):
    a,b,c,d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

dic = dict()
for i in A:
    for j in B:
        val = i + j
        if val in dic.keys():   # 키값에 ab 더한값 넣고 해당 키값이 있으면 value += 1
            dic[val] += 1
        else:
            dic[val] = 1        # 없으면 새로 만들고, value = 1
for i in C:
    for j in D:
        val = -(i + j)          # cd 더한값이 -ab와 같아야 총 합이 0임
        if val in dic.keys():
            cnt += dic[val]     # 그 값이 딕셔너리에 있으면 해당 키 값의 value 값만큼 cnt에 더함
print(cnt)