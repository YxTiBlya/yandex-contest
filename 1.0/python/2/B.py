statements = {
    "CONSTANT": False,
    "ASCENDING": False,
    "DESCENDING": False,
}
prev = int(input())
while True:
    num = int(input())
    if num == -2*10**9:
        break
    
    if prev == num:
        statements["CONSTANT"] = True
    elif prev < num:
        statements["ASCENDING"] = True
    elif prev > num:
        statements["DESCENDING"] = True

    prev = num

if statements["CONSTANT"] and statements["ASCENDING"] and statements["DESCENDING"] == False:
    print("WEAKLY ASCENDING")
elif statements["CONSTANT"] and statements["DESCENDING"] and statements["ASCENDING"] == False:
    print("WEAKLY DESCENDING")
elif statements["ASCENDING"] and statements["CONSTANT"] == False and statements["DESCENDING"] == False:
    print("ASCENDING")
elif statements["DESCENDING"] and statements["CONSTANT"] == False and statements["ASCENDING"] == False:
    print("DESCENDING")
elif statements["CONSTANT"] and statements["ASCENDING"] == False and statements["DESCENDING"] == False:
    print("CONSTANT")
else:
    print("RANDOM")