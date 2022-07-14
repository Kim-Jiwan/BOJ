N = int(input())
users = []

for _ in range(N):
    user = list(input().split())
    user[0] = int(user[0])
    users.append(user)
    
users = sorted(users, reverse = False, key = lambda x : x[0])

for user in users:
    print(f"{user[0]} {user[1]}")