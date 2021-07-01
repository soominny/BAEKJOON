# 파도반 수열
# 1 1 1 2 2 3 4 5 7 9 12 16 21 28 37

# i : 5부터
# a[i]=a[i-5]+a[i-1]
import sys
answer=[1,1,1,2,2]
for i in range(5,100):
    answer.append(answer[i-5]+answer[i-1])

n=int(sys.stdin.readline())
for _ in range(n):
    a=int(sys.stdin.readline())
    print(answer[a-1])
