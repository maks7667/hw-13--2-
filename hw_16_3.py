"""Только для оценки 10\10 в pylint"""
import datetime

def find_sundays(year):
    """
    Выводит все воскресенья определенного года
    """
    sundays_list = []
    current_date = datetime.date(year, 1, 1)
    while current_date.year == year:
        if current_date.weekday() == 6:
            sundays_list.append(current_date)
        current_date += datetime.timedelta(days=1)
    return sundays_list

if __name__ == "__main__":
    input_year = int(input("Введите год: "))
    sundays_result = find_sundays(input_year)
    if sundays_result:
        print("Все воскресенья в", input_year, "году:")
        for sunday_date in sundays_result:
            print(sunday_date.strftime("%d %B %Y"))
    else:
        print("В", input_year, "году нет воскресений.")
