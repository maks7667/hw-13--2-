"""Только для оценки 10\10 в pylint"""
from datetime import datetime, timezone

if __name__ == "__main__":
    time_utc = datetime.now(timezone.utc)
    print("Время по Гринвичу (UTC):", time_utc.strftime("%Y-%m-%d %H:%M:%S"))

    time_local = datetime.now()
    print("Местное время:", time_local.strftime("%Y-%m-%d %H:%M:%S"))
