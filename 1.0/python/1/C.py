ncode, nnumber = "", ""
 
for i in range(4):
    number = input()
    number = number.replace("(", "")
    number = number.replace(")", "")
    number = number.replace("-", "")
    number = number.replace("+", "")

    if len(number) > 10:
        code, number = number[1:4], number[4:]
    elif len(number) > 7:
        code, number = number[:3], number[3:]
    else:
        code, number = "495", number
    
    if i == 0:
        ncode, nnumber = [code, number]
    else:
        if code == ncode and number == nnumber:
            print("YES")
        else:
            print("NO")