T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())

    num = 101
    cnt = 0

    while N > 1:
        N -= 1
        cnt += 1
        num += 100

        if cnt == H:
            num = num + 1 - H * 100
            cnt = 0

    print(num)