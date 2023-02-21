import sys
from collections import deque
sys.stdin = open("input.txt", "r")

# bfs가 맞긴 맞는데, 까다로운 조건이 붙어있다.
# 
# 방문한 노드들의 최소와 최대의 차이 중 최소값을 찾아야 한다.
# 필수 방문 노드가 있다.
# 1. 모든 경로 중 최대 최소 높이 차이의 최소값을 찾는다.
#               모든 경로를 탐색하면 거의 지수시간만큼 소요된다.

# 구하고자 하는 피로도가 높이에 의해 범위가 한정된다는 것이 힌트이다.
# 예를 들면 피로도는 마을의 최대 높이 지점과 최소 높이 지점 차이보단 작거나 같다.
#
# 높이는 총 n^2 개 여서 2 가지를 고르는 경우가 거의 n^4이지만, 
# 정렬 했을 경우, 리스트 내 두 값의 차이 = 최소값이 되는 해를 찾는 투 포인터 문제로 볼 수 있다.
# 
# 두 포인터가 가리키는 높이의 높이차로 커버가 안될 경우, right를 높여 피로도를 높여보고, 
# 커버 될 경우, left를 높여서 피로도를 줄여본다. 그리고 커버했으니, 저장된 최소값과 비교한다.

# stamina 기준으로 bfs로 탐색.
def bfs(r, c, l, h):
    q = deque()
    q.append((r, c))
    visited = [[0] * (n + 1) for _ in range(n + 1)]
    visited[r][c] = 1
    tmp = 0
    
    while q:
        r, c = q.popleft()
        if arr[r][c] == 'K': tmp += 1
        for i in range(8):
            r_ = r + dx[i]
            c_ = c + dy[i]
            if 0 <= r_ < n and 0 <= c_ < n:
                if not visited[r_][c_]:
                    if l <= h_arr[r_][c_] <= h:
                        visited[r_][c_] = 1
                        q.append((r_, c_))
    print("l, h, tmp: -----", l, h,tmp)
    if tmp == k:
        return True
    else:
        False
    
# 초기 인풋을 받아줌.
n = int(sys.stdin.readline())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
h_arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in arr:
    print(i)
for i in h_arr:
    print(i)
# bfs시 필요한 시작점과 방문해야하는 집을 저장해주자. 
k = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] =='P':
            r, c = i, j
        elif arr[i][j] == 'K':
            k += 1
h_post = h_arr[r][c]

# 투 포인터로 돌 구간: 모든 지점의 높이를 정렬, 중복제거
h_lst = sum(h_arr, [])
h_lst.sort()
h_lst = list(set(h_lst))
print("-------")
print(h_lst)

hi = h_lst.index(h_post)

# 8곳 탐색
dx = [-1, -1, -1, 0, 0, 1, 1 ,1]
dy = [1, 0, -1, 1, -1, 1, 0, -1]

li, ri = 0, hi
ans = h_lst[-1] - h_lst[0]
while li <= hi and ri <= len(h_lst) - 1:
    lh = h_lst[li]
    rh = h_lst[ri]
    if bfs(r, c, lh, rh):
        ans = min(ans, rh - lh)
        li += 1
    else:
        ri += 1
print(ans)