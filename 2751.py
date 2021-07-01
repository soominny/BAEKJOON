# 수 정렬하기 2

n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))

arr=sorted(arr)

for i in arr:
    print(i)