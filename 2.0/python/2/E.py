n = int(input())
folders = sorted(list(map(int, input().split())))

ans = 0 - folders[-1]
for folder in folders:
    ans += folder

print(ans)
