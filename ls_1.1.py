"""
1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
до минуты: <s> сек;
* до часа: <m> мин <s> сек;
* до суток: <h> час <m> мин <s> сек;
* *до месяца, до года, больше года: по аналогии.
"""
seconds_in_day = 86400 # Секунд в дне
seconds_in_hour = 3600 # секунд в часе
seconds_in_minute = 60 # секунд в минуте

seconds = int(input("Введите число в секундах: "))

days = seconds // seconds_in_day # оператор div == // делит число нацело. Всегда возвращает целое число
seconds = seconds - (days * seconds_in_day)

hours = seconds // seconds_in_hour
seconds = seconds - (hours * seconds_in_hour)

minutes = seconds // seconds_in_minute
seconds = seconds - (minutes * seconds_in_minute)

print(f"{days} дн, {hours} час, {minutes} мин, {seconds} сек.") # Использовал f-строки. Гибче и читабельней метода format()
