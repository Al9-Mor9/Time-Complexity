m, n = map(int, input().split())
arr = list(map(int, input().split()))
Sum = cnt = ptS = ptE = 0                 # count, pointer_Start, pointer_End

while ptS != m and ptE != m+1:                   # ptS 배열 끝까지 갔을 때 종료
    Sum = sum(arr[ptS:ptE])
    if Sum == n:      # ptS과 ptE 사이 합이 같을 때 cnt ++, ptS ++
        cnt += 1
        ptS += 1
        continue
    elif Sum < n:     # 사이 합이 n값보다 작을 때 끝점을 늘려 부분합 증가
        ptE += 1      # ptE가 끝까지 갔을 때 sum보다 작으면 ptE 추가되서 무한루프,,
        continue
    else:
        ptS += 1
        continue
print(cnt)