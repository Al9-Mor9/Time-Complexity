n, m = map(int, input().split())
arr = list(map(int, input().split()))
start = 0
end = max(arr)              # 제일 큰놈기준 중간부터 이진탐색

while start <= end:
    mid = (start + end) // 2
    Sum = 0
    for i in arr:           # arr를 하나씩 넣어서 arr[i]가 중간지점보다 크면 자르고 난 위 부분을 더함
        if i > mid:
            Sum += i - mid
    if Sum >= m:            # 이 때 Sum이 m보다 크면 start 올림
        start = mid + 1
    else:                   # 반대
        end = mid - 1

print(end)