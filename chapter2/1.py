n = input("Input : ")
if not n.isdigit() or int(n) < 0:
    print("Invalid Input")
else:
    n = int(n)
    line = ""
    for i in range(n):
        line += "#"
        spaces = " " * (n - len(line)+1)
        print(spaces + line)