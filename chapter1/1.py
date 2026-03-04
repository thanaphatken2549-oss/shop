num = input("Input : ")
if num.isdigit() and len(num) == 1:
    x = int(num)
    x1 = x
    x2 = int(str(x)*2)
    x3 = int(str(x)*3)
    x4 = int(str(x)*4)
    total = x1+x2+x3+x4
    print("Output : ",end='')
    print(total)
else:
    print("Output : ",end='')
    print("Invalid Input")