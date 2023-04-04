n, i, j = map(int, input().split())
d1 = abs(j - i) - 1
d2 = n - 2 - d1
print(min(d1, d2))