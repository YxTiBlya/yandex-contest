gen1 = input()
gen1s = {}
for i in range(2, len(gen1)+1):
    if gen1s.get(gen1[i-2:i]) == None:
        gen1s[gen1[i-2:i]] = 0
    gen1s[gen1[i-2:i]] += 1

gen2 = input()
gen2s = set()
for i in range(2, len(gen2)+1):
    gen2s.add(gen2[i-2:i])

ans = 0
for gen in gen2s:
    if gen in gen1s:
        ans += gen1s[gen]

print(ans)