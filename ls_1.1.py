"""
1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
до минуты: <s> сек;
* до часа: <m> мин <s> сек;
* до суток: <h> час <m> мин <s> сек;
* *до месяца, до года, больше года: по аналогии.
"""
seconds_in_year = 31556926
seconds_in_month = 2629743
seconds_in_week = 604800
seconds_in_day = 86400 # Секунд в дне
seconds_in_hour = 3600 # секунд в часе
seconds_in_minute = 60 # секунд в минуте

seconds = int(input("Введите число в секундах: "))

year = seconds // seconds_in_year
seconds = seconds - (year * seconds_in_year)

month = seconds // seconds_in_month
seconds = seconds - (month * seconds_in_month)

week = seconds // seconds_in_week
seconds = seconds - (week * seconds_in_week)

days = seconds // seconds_in_day # оператор div == // делит число нацело. Всегда возвращает целое число
seconds = seconds - (days * seconds_in_day)

hours = seconds // seconds_in_hour
seconds = seconds - (hours * seconds_in_hour)

minutes = seconds // seconds_in_minute
seconds = seconds - (minutes * seconds_in_minute)

print(f"{year} лет,{month} мес,{week} нед,{days} дн, {hours} час, {minutes} мин, {seconds} сек.") # Использовал f-строки. Гибче и читабельней метода format()
