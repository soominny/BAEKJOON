# 블랙잭

n,m=map(int,input().split())
L=list(map(int,input().split()))
answer=0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(i+2,n):
            if L[i]+L[j]+L[k] > m:
                continue
            else:
                answer = max(answer,L[i]+L[j]+L[k])

print(answer)