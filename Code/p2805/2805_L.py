import sys
sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
tree = list(map(int, input().split()))

l = 1 
r = max(tree)

while l <= r:
    
    mid = (l + r)//2
    s = [x for x in tree if x > mid]
    v = sum(s) - len(s) * mid

    if v > m:
        l = mid + 1
    elif v < m :
        r = mid - 1
    else:
        break

if v < m:
    print(mid-1)
else:
    print(mid)

