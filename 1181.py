# 단어정렬

import sys
n=int(sys.stdin.readline())
arr=[]
for _ in range(n):
    word=input()
    word_len=len(word)
    arr.append((word_len,word))

arr=list(set(arr))
arr=sorted(arr)

for a,b in arr:
    print(b)
