# 나이순 정렬
import sys
n=int(sys.stdin.readline())
arr=[]
for i in range(n):
    a,b=sys.stdin.readline().split()
    arr.append((int(a),i,b))
arr=sorted(arr)

for a,b,c in arr:
    print(a,c)