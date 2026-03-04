def is_leap(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

def day_of_year(day, month, year):
    days_in_month = [31, 28, 31, 30, 31, 30,
                     31, 31, 30, 31, 30, 31]
    

date_input = input("Enter a date : ")
d, m, y = date_input.split("-")

try:
    d, m, y = map(int ,date_input.split("-"))
    if m < 1 or m > 12:
        print("Invalid month")
    exit()
    if is_leap(year):
        days_in_month[1] = 29
    return sum(days_in_month[:month - 1]) + day

print(f"day of year: {doy} ,is_leap: {leap}")
except:
