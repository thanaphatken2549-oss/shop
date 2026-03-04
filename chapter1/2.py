n = input("Enter digits : ").strip()
if not n.isdigit() or int(n) <= 1:
    print("Invalid Input")
else:
    n = int(n)
    start = 10**(n - 1)
    end = 10**n - 1
    max_palindrome = -1
    for i in range(end, start - 1, -1):
        for j in range(i, start - 1, -1):
            product = i * j
            if product <= max_palindrome:
                break
            if str(product) == str(product)[0:][::-1]:
                max_palindrome = product
    print(max_palindrome)