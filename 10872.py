# 팩토리얼
N = int(input())


def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n - 1)


print(fac(N))