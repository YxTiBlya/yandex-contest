a = int(input())
b = int(input())
c = int(input())

sum = 2*a + 3*b + 4*c
cnt = a + b + c
l, r = 0, cnt
while l < r:
    m = (l + r) // 2

    if (sum + 5*m) * 2 >= (cnt + m) * 7:
        r = m
    else:
        l = m + 1

print(l)