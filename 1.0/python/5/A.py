n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

left, right = 0, 0
ansA, ansB = 0, 0
mn = abs(a[0] - b[0])
while left < n and right < m:
    if abs(a[left] - b[right]) == 0:
        ansA, ansB = left, right
        break
    elif abs(a[left] - b[right]) < mn:
        mn, ansA, ansB = abs(a[left] - b[right]), left, right

    if a[left] < b[right]:
        left += 1
    else:
        right += 1

print(a[ansA], b[ansB])