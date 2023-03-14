N = int(input())
lst = input().split()

for i in range(N):
    if lst[i:] == lst[i:][::-1]:
        print(i)
        print(*lst[:i][::-1])
        break