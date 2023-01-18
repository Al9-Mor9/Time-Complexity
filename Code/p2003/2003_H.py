m, n = map(int, input().split())
arr = list(map(int, input().split()))
cnt = ptS = ptE = 0                 # count, pointer_Start, pointer_End

while ptS <= m-1:                   # ptS 배열 끝까지 갔을 때 종료
    if sum(arr[ptS:ptE]) == n:      # ptS과 ptE 사이 합이 같을 때 cnt ++, ptS ++
        cnt += 1
        ptS += 1
    elif sum(arr[ptS:ptE]) < n:     # 사이 합이 n값보다 작을 때 끝점을 늘려 부분합 증가
        ptE += 1                    # ptE가 끝까지 갔을 때 sum보다 작으면 ptE 추가되서 무한루프,,

    elif sum(arr[ptS:ptE]) > n:     # 사이 합이 n값보다 클 때 ptS 추가
        ptS += 1                    # 이건 문제 없었음 while 조건식 때매

    if ptE >= m:                    # 그래서 조건 추가했슴다
        ptS += 1

print(cnt)