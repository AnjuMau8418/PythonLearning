# Declare number of days in any month of year
def Is_leap(year):
    if year % 4 == 0 or year % 400 == 0 and year % 100 == 0:
        return "a leap year"
    else:
        return "not a leap year"


def days_in_month(year, month):
    if month > 12 or month < 1:
        return "Invalid Input"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if Is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]


year = int(input("Enter the year:"))
month = int(input("Enter the month :"))
Days = days_in_month(year, month)
leap_or_not = Is_leap(year)
print(f"The {year} is {leap_or_not} and it's {month}th month has {Days} days.")
