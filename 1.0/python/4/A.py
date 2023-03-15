dt = {}
for _ in range(int(input())):
    word1, word2 = map(str, input().split())
    dt[word1] = word2
    dt[word2] = word1
print(dt[input()])