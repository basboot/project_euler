# https://www.geeksforgeeks.org/python-program-to-find-day-of-the-week-for-a-given-date/


import datetime
import calendar


def is_sunday(d, m, y):
    try:
        # Convert the input date string to a datetime object
        given_date = datetime.datetime.strptime(f"{d} {m} {y}", '%d %m %Y')

        # Use isoweekday() to get the weekday (Monday is 1 and Sunday is 7)
        return given_date.weekday() == 6

    except ValueError as e:
        print(f"Error: {e}")



n_sundays = 0

for y in range(1901, 2001):
    for m in range(1, 13):

        if is_sunday(1, m, y):
            n_sundays += 1

print(n_sundays)