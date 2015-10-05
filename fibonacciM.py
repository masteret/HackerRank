import math

parsed = [int(x) for x in input().split()]
# print(parsed)

def fib(a, b, n):
    if n == 1:
        return a
    if n == 2:
        return b
    else:
        return pow(fib(a, b, n-1), 2)+fib(a, b, n-2)

print(int(fib(*parsed)))