st = set()

with open("input.txt", "r") as f:
    for line in f.readlines():
        for word in line.split():
            st.add(word)

print(len(st))