def func(n):
    res = {1: 2, 2: 4, 3: 7}
    if n in res:
        return res[n]
    for i in range(4, n + 1):
        res[i] = res[i - 1] + res[i - 2] + res[i - 3]
        #print(res)
    return res[n]


print(func(int(input())))