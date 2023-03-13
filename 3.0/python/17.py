first = list(map(int, input().split()))
second = list(map(int, input().split()))
lenf = len(first)
lens = len(second)
i = 0

while i <= 1000000:
    if min(first[i], second[i]) == 0 and max(first[i], second[i]) == 9:
        if first[i] == 0:
            first.append(first[i])
            first.append(second[i])
            lenf += 2
        else:
            second.append(first[i])
            second.append(second[i])
            lens += 2
        
    else:
        if first[i] > second[i]:
            first.append(first[i])
            first.append(second[i])
            lenf += 2
        else:
            second.append(first[i])
            second.append(second[i])
            lens += 2

    i += 1
    if i > min(lenf, lens)-1:
        break

if i == lenf:
    print("second", i)
elif i == lens:
    print("first", i)
else:
    print("botva")