N, M = map(int, input().split())
n, m = N, M

while m != 0:
    n = n % m
    n, m = m, n

print(n)

print(N * M // n)