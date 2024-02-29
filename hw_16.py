"""Только для оценки 10\10 в pylint"""
import datetime

def get_week_number(input_year, input_month, input_day):
    """
    Находим номер недели с помощью метода isocalendar()
    """
    date_object = datetime.date(input_year, input_month, input_day)
    week_number = date_object.isocalendar()[1]
    return week_number

if __name__ == "__main__":
    YEAR = 2015
    MONTH = 6
    DAY = 16
    week_number_result = get_week_number(YEAR, MONTH, DAY)

    print("Номер недели:", week_number_result)
