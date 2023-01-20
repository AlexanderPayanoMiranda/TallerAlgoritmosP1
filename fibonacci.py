from functools import cache


# Basic implementation of fibonacci series
def fibA(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibA(n-1) + fibA(n-2)


# Another implementation of fibonacci series that returns a list with the serie
def fibB(n):
    fibs = [0, 1]
    for i in range(2, n+1):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


# Another implementation of fibonacci series
def fibC(n, computed={0: 0, 1: 1}):
    if n not in computed:
        computed[n] = fibC(n-1, computed) + fibC(n-2, computed)
    return computed[n]


# Another implementation of fibonacci series
@cache
def fibD(n):
    if n <= 1:
        return n
    return fibD(n-1) + fibD(n-2)


# Another implementation of fibonacci series
def fibE(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a


print(fibA(10))
print(fibB(10))
print(fibC(10))
print(fibD(10))
print(fibE(10))
