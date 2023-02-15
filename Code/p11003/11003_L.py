import sys
sys.stdin = open("input.txt","r")
#----------------------------------
from collections import deque
n, l = map(int, input().split())
arr = list(map(int, input().split()))

q = deque()
ans = []
for idx in range(n):
    #q에 있고, 가장 최근에 넣은 값보다 다음값이 더 작으면 가장 최근 넣은 값을 계속 제거
    #사실상 새로들어온 값과 q에 들어있는 모든 값을 비교하는 것. 
    while q and q[-1][1] > arr[idx]:
        q.pop()     #LIFO
    #q에 값이 있고, 가장 마지막 넣은 값이 범위 내 존재하지 않으면 해당 값 제거 
    if q and q[0][0] < idx - l + 1:
        q.popleft() #FIFO
    
    q.append([idx, arr[idx]])
    print(q[0][1], end = ' ')
