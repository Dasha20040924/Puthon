def is_leap_year(year):
    return year % 4 == 0


# Выбираем любой год для проверки
year_to_check = 2024
# Вызываем функцию и сохраняем результат в переменную
is_leap = is_leap_year(year_to_check)
# Выводим результат в консоль
print(f"год {year_to_check}: {is_leap}")
