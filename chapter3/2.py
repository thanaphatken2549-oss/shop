def is_leap(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

def day_in_year(year):
    return 366 if is_leap(year) else 365

def validate_date(day, month, year):
    if year <= 0:
        return False
    if month < 1 or month > 12:
        return False
    days_in_month = [31, 28, 31, 30, 31, 30,
                     31, 31, 30, 31, 30, 31]
    if is_leap(year):
        days_in_month[1] = 29
    if day < 1 or day > days_in_month[month -1]:
        return False
    return True

def day_of_year(day, month, year):
    days_in_month = [31, 28, 31, 30, 31, 30,
                     31, 31, 30, 31, 30, 31]
    if is_leap(year):
        days_in_month[1] = 29
    return sum(days_in_month[:month-1]) + day

def date_diff(date1, date2):
    d1, m1, y1 = (date1.split('-'))
    d2, m2, y2 = (date2.split('-'))
    d1=int(d1)
    m1=int(m1)
    y1=int(y1)
    d2=int(d2)
    m2=int(m2)
    y2=int(y2)
    if not validate_date(d1, m1, y1):
        print("Invalid")
        exit()
    if not validate_date(d2, m2, y2):
        print("Invalid")
        exit()
    if y1 == y2:
        return day_of_year(d2, m2, y2) - day_of_year(d1, m1, y1) + 1
    days = 0
    days += day_in_year(y1) - day_of_year(d1, m1, y1) + 1
    days += day_of_year(d2, m2, y2)
    for year in range(y1 + 1, y2):
        days += day_in_year(year)
    return days

dates = input("Enter Input: ")
date1, date2 = [d.strip() for d in dates.split(',')]
result = date_diff(date1, date2)

print(result)