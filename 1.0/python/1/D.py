a = int(input())
b = int(input())
c = int(input())

if c < 0:
    print("NO SOLUTION")
elif (a + b) == c ** 2 and (2 * a + b) == c ** 2:
    print("MANY SOLUTIONS")
else:
    if a != 0 and (c ** 2 - b) / a == (c ** 2 - b) // a:
        print((c ** 2 - b) // a)
    else:
        print("NO SOLUTION")