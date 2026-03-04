def is_leap(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


def day_of_year(day, month, year):
    days = [31, 28, 31, 30, 31, 30,
            31, 31, 30, 31, 30, 31]

    if is_leap(year):
        days[1] = 29

    return sum(days[:month - 1]) + day


# -----------------------------
date_str = input("Enter a date : ")

# แยกส่วน
parts = date_str.split("-")

# ต้องมี 3 ส่วนเท่านั้น
if len(parts) != 3:
    print("day of year: Invalid ,is_leap: False")
    exit()

d, m, y = parts

# ถ้ามีตัวอักษรให้ invalid ทันที
if not (d.isdigit() and m.isdigit() and y.isdigit()):
    print("day of year: Invalid ,is_leap: False")
    exit()

# แปลงเป็นตัวเลข
d = int(d)
m = int(m)
y = int(y)

# ตรวจ leap
leap = is_leap(y)

# ตรวจเดือนผิด
if m < 1 or m > 12:
    print(f"day of year: Invalid ,is_leap: {leap}")
    exit()

# ตรวจวันผิด
days = [31, 28, 31, 30, 31, 30,
        31, 31, 30, 31, 30, 31]

if leap:
    days[1] = 29

if d < 1 or d > days[m - 1]:
    print(f"day of year: Invalid ,is_leap: {leap}")
    exit()

# ถ้าถูกต้องทั้งหมด
print(f"day of year: {day_of_year(d, m, y)} ,is_leap: {leap}")