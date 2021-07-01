# 덩치합

n=int(input())
array=[]
for i in range(n):
    x,y=map(int,input().split())
    array.append((x,y))

for x,y in array:
    count=0
    for a,b in array:
        if x<a and y<b:
            count+=1
    print(count+1,end=' ')