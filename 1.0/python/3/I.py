n = int(input())
allLang = set()
st = {}
for i in range(n):
    m = int(input())
    st[i] = set()
    for _ in range(m):
        lang = input()
        st[i].add(lang)
        allLang.add(lang)

inter = st[0]
for i in range(1, n):
    inter = inter.intersection(st[i])

print(len(inter))
for lang in inter:
    print(lang)
print(len(allLang))
for lang in allLang:
    print(lang)