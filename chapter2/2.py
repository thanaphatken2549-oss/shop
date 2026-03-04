n = input("Input : ").strip().split()
if len(n) == 0 or len(n) > 10:
    print("Invalid Input")
    exit()
for p in n:
    if not p.isdigit() or len(p) != 1:
        print("Invalid Input")
        exit()
nums = sorted(n)
if nums[0] == '0':
    for i in range(1, len(nums)):
        if nums[i] != '0':
            nums[0], nums[i] = nums[i], nums[0]
            break
result = "".join(nums)
if result == "0" or result == "00" or result == "000" or result == "0000" or result == "00000" or result == "000000" or result == "0000000" or result == "00000000" or result == "000000000" or result == "0000000000":
    print("Invalid Input")
else:
    print(result)