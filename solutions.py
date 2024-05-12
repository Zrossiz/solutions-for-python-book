import math
import datetime
import random
from typing import List

# Найти объем и площадь поверхности прямоугольного параллелепипеда 
# def get_v(a, b, c):
#     print('Объем равен: ', a * b * c)

# def get_s(a, b, c):
#     s = 2 * (a * b + b * c + a * c)
#     print('Площадь равна: ', s)

# def get_info(a, b, c):
#     get_s(a, b, c)
#     get_v(a, b, c)

# get_info(2, 2, 2)


# Найти длину окружности и площадь круга по радиусу
# def get_l(r: int):
#     l = 2 * math.pi * r
#     print('Длина окружности равна: ', l)

# def get_s(r: int):
#     s = math.pi * r ** 2
#     print('Площадь окружности равна: ', s)

# def get_info(r: int):
#     get_l(r)
#     get_s(r)

# get_info(5)

# Найти гипотенузу и периметр
# def get_hypotenuse(a: int, b: int) -> int:
#     hypotenuse = math.sqrt(a**2 + b**2)
#     print("Гипотенуза равна: ", hypotenuse)
#     return hypotenuse

# def get_perimeter(a: int, b: int, c: int):
#     perimeter = a + b + c
#     print("Периметр равен: ", perimeter)

# def get_info(a, b):
#     hypotenuse = get_hypotenuse(a, b)
#     get_perimeter(a, b, hypotenuse)

# get_info(3, 4)

# Получить количество слов в строке
# def get_words_in_string(string: str):
#     arr_of_strings = string.split(' ')
#     print(len(arr_of_strings))

# get_words_in_string('Тут должно быть 5 слов')

# Получить количество слов, которые начинаются с одной буквы
# def get_count_words_with_same_symbol(sentence: str):
#     sentence_arr = sentence.lower().split(' ')
#     first_symbol_of_every_word = {}
#     for word in sentence_arr:
#         first_symbol_of_every_word[word[0]] = 0
#     for word in sentence_arr:
#         if word[0] in first_symbol_of_every_word:
#             first_symbol_of_every_word[word[0]] = first_symbol_of_every_word[word[0]] + 1
#     print(max(first_symbol_of_every_word.values()))

# get_count_words_with_same_symbol('Тестовое предложение один два три дд дд дд')

# Решить уравнение
# def solution(x: int):
#     y = 3 * x**3 + math.cos(x + 1)
#     print('Решение: ', y)

# solution(1)

# Решить уравнение
# def solution(x: int, a: int, b: int):
#     y = 2 * a * math.sqrt(x + 2) + b * (x + 1)
#     print('Решение: ', y)

# solution(4, 2, 1)

# Решить уравнение
# def solution(x: int, a: int) -> int:
#     y = (1 / (x**2 + 1)) - a
#     print('Решение: ', y)
#     return y

# solution(3, 4)

# Решить уравнение
# def solution(x: int) -> int:
#     y = (x - 2 * math.sin(x) / abs(8 * x - 5 * math.atan(3 * x + 1)))
#     print('Решение: ', y)
#     return y

# Решить уравнение
# def solution(x: int, b: int) -> float:
#     y = (2 * math.sqrt(x**3 + 1)) - (2 * b)
#     print('Решение: ', y)
#     return y
# solution(3, 4)

# Перевести из F в градусы Цельсия
# def from_f_to_c(f: int) -> float:
#     c = (f - 32) * 5/9
#     print('Температура в цельсиях: ', c)
#     return c

# from_f_to_c(572)

# Конвертор валют из доллара в рубль
# def exchange(rate: float, count: int) -> List[str]:
#     rub = str(rate * count).split('.')
#     print(f"{rub[0]} руб. {rub[1]} коп.")
#     return rub

# exchange(90.20, 4)

# Решить уравнение
# def solution(x: int, a: int) -> float:
#     y = ((3 - a) / (x**2 + 1)) + math.sin(2 * x + 1)
#     print("Решение: ", y)
#     return y

# solution(1, 1)

# Решить уравнение
# def solution(x: int, a: int) -> float:
#     y = (a * x**3) + math.cos(3 * x + 1)
#     print("Решение: ", y)
#     return y

# solution(1, 2)

# Написать программу для вычисления стоимости поездки на дачу
# def get_cost(distance: int, fuel: int, cost_per_liter: int):
#     total_distance = distance * 2
#     total_fuel = total_distance / fuel
#     total_price = total_fuel * cost_per_liter
#     return print(total_price)

# get_cost(50, 10, 100)

# Написать программау для получения строки с обратной последовательностью слов
# def get_reverse_string(sentence: str):
#     arr_str = sentence.split()
#     reverse_string = ' '.join(reversed(arr_str))
#     return print(reverse_string)

# get_reverse_string('Эта строка должна быть перевернута')

# Перед каждым вхождением символа C в строку S вставить строку S0
# def solution(c: str, S: str, S0: str):
#     result_string = ''
#     for index, item in enumerate(S):
#         if item == c:
#             result_string += S0
#         result_string += item
#     print(result_string)

# solution('а', 'ваб ва бв а', 'ТЕСТ')

# По числу текущего месяца определить день недели
# def get_day_of_week():
#     cur_month = datetime.date.today().month
#     if cur_month > 7:
#         cur_month -= 7
#     days_of_week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"] 
#     print(days_of_week[cur_month - 1])

# get_day_of_week()

# Проверка на знание таблицы умножения
# def check_multiplication_table_knowledge():
#     print("Программа генерирует числа...")
#     first_num = random.randint(1, 9)
#     second_num = random.randint(1, 9)
#     multiply = first_num * second_num

#     print(f"Что будет результатом операции {first_num} * {second_num} ?")

#     user_num = int(input("Введите ответ: "))

#     if multiply == user_num:
#         print("Правильно")
#     else:
#         print("Неправильно")

# check_multiplication_table_knowledge()