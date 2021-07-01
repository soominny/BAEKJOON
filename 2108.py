# 통계학
from collections import Counter
import sys
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(sys.stdin.readline()))

arr=sorted(arr)
n=len(arr)

many= Counter(arr).most_common()
if n>1:
    if many[0][1]==many[1][1]:
        most=many[1][0]
    else:
        most=many[0][0]
else:
    most=many[0][0]

print(round(sum(arr)/n))
print(arr[n//2])
print(most)
print(arr[n-1]-arr[0])



