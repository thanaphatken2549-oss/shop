import sys

def is_leap(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


def day_of_year(day, month, year):
    days = [31, 28, 31, 30, 31, 30,
            31, 31, 30, 31, 30, 31]

    if is_leap(year):
        days[1] = 29

    return sum(days[:month - 1]) + day


# -------------------------------------

date_str = input("Enter a date : ")

try:
    d, m, y = map(int, date_str.split("-"))
    leap = is_leap(y)

    # ตรวจเดือนผิด
    if m < 1 or m > 12:
        print(f"day of year: Invalid ,is_leap: {leap}")
        sys.exit()

    # ตรวจวันในเดือน
    days = [31, 28, 31, 30, 31, 30,
            31, 31, 30, 31, 30, 31]

    if leap:
        days[1] = 29

    if d < 1 or d > days[m - 1]:
        print(f"day of year: Invalid ,is_leap: {leap}")
        sys.exit()

    print(f"day of year: {day_of_year(d, m, y)} ,is_leap: {leap}")

except:
    print("day of year: Invalid ,is_leap: False")
    sys.exit()
