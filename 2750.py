# 수 정렬하기

n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))

# 삽입정렬
for i in range(1,len(arr)):
    for j in range(i,0,-1):
        if arr[j]<arr[j-1]:
            arr[j],arr[j-1]=arr[j-1],arr[j]
        else:
            break

for i in arr:
    print(i)




