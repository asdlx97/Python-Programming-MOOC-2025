"""
Please write a function named list_years(dates: list) which takes
a list of date type objects as its argument. The function should
return a new list, which contains the years in the original list
in chronological order, from earliest to latest.

An example of the function in action:

date1 = date(2019, 2, 3)
date2 = date(2006, 10, 10)
date3 = date(1993, 5, 9)

years = list_years([date1, date2, date3])
print(years)

Sample output
[1993, 2006, 2019]
"""

# Write your solution here
# Remember the import statement
from datetime import date


def list_years(dates: list):
    dates_sorted = sorted(dates[:])
    sorted_years = []
    for date in dates_sorted:
        sorted_years.append(date.year)
    return sorted_years


if __name__ == "__main__":
    date1 = date(2019, 2, 3)
    date2 = date(2006, 10, 10)
    date3 = date(1993, 5, 9)

    years = list_years([date1, date2, date3])
    print(years)

"""
# Suggested solution

from datetime import date
 
def list_years(dates: list):
    years = []
    for dt in dates:
        years.append(dt.year)
 
    years.sort()
    return years

#Review
My solution results in the same output, suggested one is a bit more concise.
"""
