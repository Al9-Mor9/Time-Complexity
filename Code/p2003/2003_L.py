#import sys
#sys.stdin = open("input.txt", "r")

n, m = map(int,input().split())
a_n = list(map(int, input().split()))
p1, p2 = 0, 0
cnt = 0

while p1 <= p2 & \
        p2 <= n:
        s = sum(a_n[p1:p2])
        if s == m:
            cnt += 1
            p1 += 1
            p2 += 1
        elif s < m:
            p2 += 1
        else:
            p1 += 1    

print(cnt)