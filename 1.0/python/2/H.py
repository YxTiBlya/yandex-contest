lst = sorted(list(map(int, input().split())))
print(lst[0], lst[1], lst[-1]) if lst[0] * lst[1] * lst[-1] > lst[-3] * lst[-2] * lst[-1] else print(lst[-3], lst[-2], lst[-1])