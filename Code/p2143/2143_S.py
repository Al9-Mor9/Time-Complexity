from collections import Counter
 
T = int(input()) 
n = int(input()) 
A = list(map(int,input().split())) 
m = int(input()) 
B = list(map(int,input().split())) 
 
answer = 0 # 정답 0으로 세팅
cnt = Counter() # 카운터 함수 cnt로 정의

 
for s in range(n):
    for e in range(s,n):
        cnt[sum(A[s:e+1])] += 1 # 배열 A의 모든 부배열의 합을 카운터에 개수로 센다
# print(cnt)
# > Counter({1: 2, 4: 2, 3: 2, 5: 1, 7: 1, 6: 1, 2: 1})

for s in range(m):
    for e in range(s,m):
        t = T - sum(B[s:e+1])
        answer += cnt[t]
# 위와 마찬가지로 배열 B의 모든 부배열의 합을 T에서 빼고
# 그 값이 cnt에 존재한다면 answer의 값을 1씩 추가
# 값이 없으면 0
print(answer)
