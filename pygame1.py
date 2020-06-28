import math

first_date = input("Enter first date")
second_date = input("Enter second date")

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def date_tuple(date_str):
    lst = date_str.split("/")
    for n, i in enumerate(lst):
        lst[n] = int(i)
    return lst

date1 = date_tuple(first_date)
date2 = date_tuple(second_date)

date0 = [1, 1, 0]


def difference(date, date0 = date0):
    def leap_years(date):
        counter = 0
        for n in range(date[2]+1):
            if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
                counter += 1
        return counter


    days_from_years = date[2] * 365
    days_from_months = sum(months[:(date[1] - 1)])
    days_from_days = date[0]
    total = days_from_years + days_from_months + days_from_days + leap_years(date)
    return total

print(abs(difference(date1) - difference(date2)))










