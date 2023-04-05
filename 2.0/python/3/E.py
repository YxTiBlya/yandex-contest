m = int(input())
wits = []
for _ in range(m):
    wits.append(set(input()))

n = int(input())
numbers = []
mx = 0
for _ in range(n):
    number = input()
    nst = set(number)
    c = 0
    for wit in wits:
        if wit <= nst:
            c += 1
    numbers.append((number, c))
    mx = max(mx, c)

for number in numbers:
    if number[1] == mx:
        print(number[0])