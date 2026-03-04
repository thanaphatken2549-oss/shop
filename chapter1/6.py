lst = input("Enter your input : ")
try:
    num = eval(lst)
    if not isinstance(num, list):
        print("Invalid Input")
    elif any(not isinstance(x, int) for x in num):
        print("Invalid Input")
    elif len(num) < 2:
        print("Invalid Input")
    else:
        data_sorted = sorted(num)
        max1 = data_sorted[-1] * data_sorted[-2]
        max2 = data_sorted[0] * data_sorted[1]
        print(max(max1, max2))
except:
    print("Invalid Input")