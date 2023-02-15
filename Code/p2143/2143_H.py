from _collections import defaultdict
T = int(input())
a = int(input())
Aarr = list(map(int, input().split()))
b = int(input())
Barr = list(map(int, input().split()))
Sum = sum(Aarr)
cnt = 0
dic = defaultdict(int)

for i in range(a):
    for j in range(i, a):
        dic[sum(Aarr[i:j+1])] += 1
print(dic)