N, M = map(int, input().split())
num = list(map(int, input().split()))
closest = 0

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            if M >= num[i] + num[j] + num[k]:
                if M - (num[i] + num[j] + num[k]) < M - closest:
                    closest = num[i] + num[j] + num[k]

print(closest)