string = input()

j = len(string) - 1
ans = 0
for i in range(len(string)//2):
    if string[i] != string[j]:
        ans += 1
    j -= 1

print(ans)
