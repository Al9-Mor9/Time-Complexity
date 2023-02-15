import sys
sys.stdin = open("input.txt", "r")
#--------------------------------------

# 최악의 경우 n^4이다. 매우 어지러운 시간복잡도다.
# 배열이 2개인 경우를 생각해보자. -> 한 배열을 for 문을 돌리며 
#                                  값의 음수가 다른 배열에 있는지 확인하면 된다. O(n)
#
# 배열이 3개라면..? -> 2개 배열로 나올 수 있는 합을 
#                      하나의 배열로 만들고 다른 배열을 for문 돌리며 확인하자. O(n^2)
# 배열이 4개라면..? 
# 1. 3개 배열로 나올 수 있는 합을 하나의 배열로 만들고 ... O(n^3)
# 2. 2개 배열로 나올 수 있는 합을 하나의 배열로 만들고, 
#       다른 2개 배열도 하나의 배열로 만들어 확인.. O(n^2)
# 
# 이러면 이론상 n크기 배열이 m개 주어졌을 때, O(n ^ (log2(m))) 시간 복잡도가 보장된다. 맞나..?

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr = list(map(list, zip(*arr)))            #변수 선언하기 귀찮으니 전치 해주자.
cnt = 0
dic = {}

#------------------
for a in arr[0]:
    for b in arr[1]:
        if a + b in dic:
            dic[a + b] += 1
        else:
            dic[a + b] = 1
for c in arr[2]:
    for d in arr[3]:
        if -c - d in dic:
            cnt += dic[-c - d]
print(cnt)        

# 흠... 드럽게 깐깐하네
# arrab = [x + y for x in arr[0] for y in arr[1]]
# arrcd = [x + y for x in arr[2] for y in arr[3]]

# for i in arrab:
#     if i in dic:
#         dic[i] += 1
#     else:
#         dic[i] = 1

# for i in arrcd:
#     if -i in dic:
#         cnt += dic[-i]

# print(cnt)
