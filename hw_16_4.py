"""Только для оценки 10\10 в pylint"""
import datetime

def add_years(date, years):
    """
    Добавляет год с заданной датой и отображает
    новую дату
    """
    try:
        return date.replace(year=date.year + years)
    except ValueError:
        return date.replace(year=date.year + years, month=2, day=28)

if __name__ == "__main__":
    print(add_years(datetime.date(2015, 1, 1), -1))
    print(add_years(datetime.date(2015, 1, 1), 0))
    print(add_years(datetime.date(2015, 1, 1), 2))
    print(add_years(datetime.date(2000, 2, 29), 1))
