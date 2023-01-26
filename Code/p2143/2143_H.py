from _collections import defaultdict
T = int(input())

a = int(input())
Aarr = list(map(int, input().split()))
b = int(input())
Barr = list(map(int, input().split()))

dicA = defaultdict(int)     # 이거 안쓰면 못푸네여ㅠ

cnt = 0
#for i in range(sum(Aarr)):
#    dicA[i + 1] = 0                # 키 값 정의(1 ~ sum(Aarr) 까지)
for i in range(a):
    for j in range(i, a):
        dicA[sum(Aarr[i:j + 1])] += 1   # i부터 j까지 합을 key값으로 하고 해당 value + 1

for i in range(b):
    for j in range(i, b):
        #if (T - sum(Barr[i:j+1])) >= 1:        # Barr[i:j+1] = i부터 j까지 합
        cnt += dicA[T - sum(Barr[i:j+1])]       # 그 합을 T에서 뺐을 때의 값을 key로 하고 dicA의 해당 val 만큼 카운트 추가
print(cnt)