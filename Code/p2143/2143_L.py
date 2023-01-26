import sys
sys.stdin = open("input.txt", "r")
#-----------------------------------
T = int(input())
n = int(input())
n_l = list(map(int, input().split()))
m = int(input())
m_l = list(map(int, input().split()))

cnt = 0
n_s, m_s = [], []

for i in range(n):
    s = n_l[i]
    n_s.append(s)
    for j in range(i + 1, n):
        s += n_l[j]
        n_s.append(s)

for i in range(m):
    s = m_l[i]
    m_s.append(s)
    for j in range(i + 1, m):
        s += m_l[j]
        m_s.append(s)

# n_s = [i for i in n_s if i < T]

dic = {}
for i in n_s:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in m_s:
    if T-i in dic:
        cnt += dic[T-i]

print(cnt)
