'''
Outdated

In the United States, dates are typically formatted in month-day-year order (MM/DD/YYYY),
otherwise known as middle-endian order, which is arguably bad design. Dates in that format can’t be easily sorted because the date’s year comes last instead of first.
Try sorting, for instance, 2/2/1800, 3/3/1900, and 1/1/2000 chronologically in any program (e.g., a spreadsheet).
Dates in that format are also ambiguous. Harvard was founded on September 8, 1636, but 9/8/1636 could also be interpreted as August 9, 1636!

Fortunately, computers tend to use ISO 8601, an international standard that prescribes that dates should be formatted in year-month-day (YYYY-MM-DD) order,
no matter the country, formatting years with four digits, months with two digits, and days with two digits, “padding” each with leading zeroes as needed.

In a file called outdated.py, implement a program that prompts the user for a date, anno Domini,
in month-day-year order, formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list below:

Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, prompt the user again.
Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.
'''

def main():
    months_lst = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
        ]

    while True:
        date = input("Date: ")
        #For this format MM/DD/YYYY
        try:
            month_num, day, year = date.split("/")
            day = int(day)
            year = int(year)
            month_num = int(month_num)

            if year < 0 or year > 9999: 
                raise ValueError("This year doesn't exist")
            elif month_num > 12 or month_num < 1:
                raise ValueError("This month doesn't exist")
            elif day < 1 or day > 31:
                raise ValueError("This day doesn't exist")
            else:
                print(f"{year}-{month_num:02}-{day:02}")
        except Exception as e:
            pass
        
        #For this format Month Day, Year
        try:
            month, day, year = date.split(" ")
            day = int(day.replace(",", ""))
            year = int(year)
            month = month.title()
            month_num = 0

            if month in months_lst:
                month_num = months_lst.index(month) + 1
                
            if year < 0 or year > 9999: 
                raise ValueError("This year doesn't exist")
            elif month_num > 12 or month_num < 1:
                raise ValueError("This month doesn't exist")
            elif day < 1 or day > 31:
                raise ValueError("This day doesn't exist")
            else:
                print(f"{year}-{month_num:02}-{day:02}")
                
        except Exception as e:
            pass
main()