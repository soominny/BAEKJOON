# 신나는 함수 실행


L=dict()

def w(a,b,c):
    if (a,b,c) in L.keys():
        return L[a,b,c]
    else:
        if a>20 or b>20 or c>20:
            L[(a,b,c)]=w(20,20,20)
            return w(20,20,20)
        if a<=0 or b<=0 or c<=0:
            L[(a,b,c)]=1
            return 1
        if a<b<c:
            L[(a,b,c)]=w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
            return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        else:
            L[(a,b,c)]=w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
            return w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

import sys
L={}
while True:
    a,b,c=map(int,sys.stdin.readline().split())
    if a==b==c==-1:
        break

    print(f'w({a}, {b}, {c}) = {w(a,b,c)}')