n = int(input())
st = set(range(1, n + 1))

while True:
    inp = input()

    if inp != "HELP":
        nums = list(map(int, inp.split()))
        ans = input()

        if ans == "YES":
            st.intersection_update(nums)
        else:
            st.difference_update(nums)

    else:
        break

print(*sorted(list(st)))