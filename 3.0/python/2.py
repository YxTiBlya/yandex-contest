k = int(input())
S = input()
lns = len(S)
alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ans = 0

for letter in alp:
    right = 0
    t = k
    for left in range(lns - k):
        while right < lns and t >= 0:
            if S[right] != letter:
                t -= 1
            right += 1

        tmp = right - left - 1

        if S[left] != letter:
            t += 1
            
        if tmp > ans:
            ans = tmp

print(ans)