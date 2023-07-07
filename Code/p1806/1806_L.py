import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
# --------------------------------------

# 10 <= n < 100,000
# 0 < S <= 100,000,000

n, s = map(int, input().split())
arr = list(map(int, input().split()))
ans = int(1e5 + 1)
p1, p2 = 0, 1
tmp = arr[0]


while p1 < n and p2 <= n:
    print(p1, p2, tmp)
    if tmp >= s:
        ans = min(ans, p2 - p1)
        tmp -= arr[p1]
        p1 += 1
    else:
        if p2 == n:
            break
        tmp += arr[p2]
        p2 += 1

print(0) if ans == int(1e5 + 1) else print(ans)



