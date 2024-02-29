"""Только для оценки 10\10 в pylint"""
from datetime import datetime, timedelta

def find_first_monday(year, week):
    """
    Находит дату первого понедельника данной недели
    """
    first_day = datetime(year, 1, 1)
    first_monday = first_day + timedelta(days=(0 - first_day.weekday() + 7) % 7)
    target_date = first_monday + timedelta(weeks=week - 1)
    return target_date

if __name__ == "__main__":
    YEAR = 2024
    WEEK = 9
    first_monday_date = find_first_monday(YEAR, WEEK)
    print(first_monday_date.strftime("%a %d %B %H:%M:%S %Y"))
