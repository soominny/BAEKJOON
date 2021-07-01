# 피보나치 함수
def count(n): #0,1,3
    if len(zero)<=n:
        for i in range(len(zero),n+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print(zero[n],one[n])


zero=[1,0,1]
one=[0,1,1]

import sys
n=int(sys.stdin.readline())
arr=[]
for _ in range(n):
    a=int(sys.stdin.readline())
    count(a)

