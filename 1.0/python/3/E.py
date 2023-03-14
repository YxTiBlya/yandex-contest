corr = input().split()
ans = set()
for i in input():
    if i not in corr:
        ans.add(i)

print(len(ans))