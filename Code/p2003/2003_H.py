m, n = map(int, input().split())
arr = list(map(int, input().split()))
Sum = cnt = ptS = ptE = 0

while ptS != m and ptE != m+1:
    Sum = sum(arr[ptS:ptE])
    if Sum == n:
        cnt += 1
        ptS += 1
    elif Sum < n:
        ptE += 1
    else:
        ptS += 1
print(cnt)