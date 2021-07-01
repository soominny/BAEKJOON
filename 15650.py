# N과 M(2)
from itertools import combinations
import sys

n,m=map(int,sys.stdin.readline().split())
arr=[str(i) for i in range(1,n+1)]

if m==1:
    for a in arr:
        print(a)

else:
    for a in combinations(arr,r=m):
        print(" ".join(a))