import sys

n, q = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
prefix = [0 for _ in range(n+1)]

for i in range(1, n+1):
    prefix[i] = prefix[i-1] + lst[i-1]

for _ in range(q):
    s, e = map(int, sys.stdin.readline().split())
    print(prefix[e] - prefix[s-1])