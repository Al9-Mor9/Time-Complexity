import sys
sys.stdin = open("input.txt", "r")


n = int(input())
s = 1

maxmin = [[0 for _ in range(6)] for _ in range(n+1)]

for i in range(n):
    a, b, c = map(int, input().split())
    
    maxmin[i+1] = [a + max(maxmin[i][0:2]),
                    b + max(maxmin[i][:3]),
                    c + max(maxmin[i][1:3]),
                    a + min(maxmin[i][3:5]),
                    b + min(maxmin[i][3:]),
                    c + min(maxmin[i][4:])] 

print(max(maxmin[-1][:3]), min(maxmin[-1][3:]))

