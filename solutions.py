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

# Получить склонение валюты
# def get_the_declination_of_number(amount: int):
#     if amount % 10 == 1 and amount % 100 != 11:
#         return print(amount, "рубль")
#     elif 2 <= amount % 10 <= 4 and (amount % 100 < 10
#                                     or amount % 100 >= 20):
#         return print(amount, "рубля")
#     else:
#         return print(amount, "рублей")

# get_the_declination_of_number(173)

# Рассчитать размер зп с учетом опыта работы
# def get_wage(age: int, base_salary: int):
#     wage = base_salary
#     if age < 10 and age > 5:
#         wage = wage * 1.1
#     if age >= 10 and age <= 15:
#         wage = wage * 1.15
#     if age > 15:
#         wage = wage * 1.2
#     print("Wage: ", int(wage))

# get_wage(16, 10000)

# Получить цвет радуги по первому слову
# def get_color_of_rainbow(word: str):
#     first_symbol_of_word = word[0].lower()
#     rainbow_colors = ["красный", "оранжевый", "желтый", "зеленый", "голубой", "синий", "фиолетовый"]
#     for color in rainbow_colors:
#         if color[0] == first_symbol_of_word:
#             print(color)

# get_color_of_rainbow('Золотой')

# Является ли число числом Армстронга
# def is_armstrong_number(number: int):
#     string_number = str(number)
#     sum_of_cubs_num = int(string_number[0])**3 + int(string_number[1])**3 + int(string_number[2])**3
#     if number ==sum_of_cubs_num:
#         print(True)
#     else:
#         print(False)

# is_armstrong_number(370)

# Подсчитать сумму для заданного натурального n
# def get_sum(n: int):
#     sum = 0
#     for number in range(1, n + 1):
#         sum = sum + (1 / number)
#     print(sum)

# get_sum(10)

# Подсчитать количество членов для суммы < 0 (арифметическая прогрессия)
# def get_count_of_iterations():
#     start_num = 7.1
#     diff = 1.8
#     result = []

#     while start_num >= -diff:
#         result.append(start_num)
#         start_num -= diff
#     print(f"Нужно {len(result)}")

# get_count_of_iterations()


# Для заданного натурального n подсчитать сумму
# def get_sum(n: int) -> int:
#     if n == 0:
#         return 1
    
#     result = 0
#     for num in range(1, n + 1):

#         buff = 1
#         for num1 in range(1, num + 1):
#             buff *= num1

#         result += buff

#     return result

# print('Сумма равна:', get_sum(5))

# Посчитать стоимость конфет
# def get_cost_for_candies(price: int):
#     inital_weight = 1.2

#     while inital_weight <= 2:
#         print(f'Стоимость для {inital_weight} кг:', round(price * inital_weight))
#         inital_weight = round(inital_weight + 0.2, 1)
    
# get_cost_for_candies(10)

# Получить среднее арифметическое отрезка от K до L
# def get_average(arr: list[int], k: int, l: int) -> float:
#     index_k = arr.index(k)
#     index_l = arr.index(l)
#     arr_segment = arr[index_k:index_l + 1]
#     sum_segment = sum(arr_segment)
#     result = sum_segment / len(arr_segment)
#     print("Среднее арифметечское отрезка", result)
#     return result

# get_average([1, 2, 3, 4, 5, 6, 7, 8], 2, 6)

# Получить сумму чисел на отрезках до K и от L
# def get_sum_by_segments(arr: list[int], k: int, l: int) -> int:
#     index_k = arr.index(k)
#     index_l = arr.index(l) + 1
#     segment_k = arr[0:index_k]
#     segment_l = arr[index_l:len(arr)]
#     result = sum(segment_l) + sum(segment_k)
#     print(f"Сумма отрезков до {k} и от {l}:", result)
#     return result

# get_sum_by_segments([1, 2, 3, 4, 5, 6, 7, 8], 5, 6)

# Увеличить все четные числа на заданное число
# def update_even_nums(arr: list[int], increase_num: int):
#     result = []
#     for index, num in enumerate(arr):
#         if index % 2 == 0:
#             num += increase_num
#         result.append(num)
#     print(result)

# update_even_nums([1, 2, 3, 4, 5, 6, 7, 8], 4)

# Найти минимальный элемент из элементов с четными номерами
# def get_min_even_index(arr: list[int]):
#     even_indices = []
#     for index, num in enumerate(arr):
#          if index % 2 == 0:
#              even_indices.append(num)
#     print(even_indices)
#     print("Минимальное число из элементов с четным индексом:", min(even_indices))

# get_min_even_index([10, 2, 11, 4, 5, 6, 7, 8, 9])

# Получить список с уникальными элементами
# def get_uniq_nums_arr(arr: list[int]):
#     uniq_arr = []
#     for num in arr:
#         if not num in uniq_arr:
#             uniq_arr.append(num)
#     print(uniq_arr)

# get_uniq_nums_arr([1, 1, 2, 2, 2, 3, 4, 5])

# Получить список с уникальными элементами
# def get_uniq_nums_set(arr: list[int]):
#     uniq_set = set()

#     for num in arr:
#         uniq_set.add(num)
    
#     print(uniq_set)

# get_uniq_nums_set([1, 1, 2, 2, 2, 3, 4, 5])

# Выбрать из списка все нечетные элементы и упорядочить их по убыванию
# def get_sorted_odd_nums(arr: list[int]) -> list[int]:
#     odd_nums = []

#     for num in arr:
#         if num % 2 != 0:
#             odd_nums.append(num)
#     print(odd_nums)
#     return sorted(odd_nums, reverse=True)

# print("Упорядоченный список нечетных элементо:", get_sorted_odd_nums([1, 4, 2, 13, 6, 9, 0, 10, 8, 11]))

# Вывести таблицу для товаров (от 1 до 10)
# def get_cost_table():
#     for num in range(1, 11):
#         print(f"{num}: {round(num * 20.4, 1)}")

# get_cost_table()

# Напечатать квадраты всех целых чисел от A до B с шагом N
# def get_squares_of_numbers(A: int, B: int, N: int):
#     for num in range(A, B + 1, N):
#         print(f"{num}: {num**2}")

# get_squares_of_numbers(0, 10, 2)

# Составить программу, которая находит и выводит на печать все четрыхзначные числа
# abcd, для которых выполняются след. условия: a, b, c, d - разные числа
# и ab - cd = a + b + c + d
# def get_solution():
#     for num in range(1000, 10000):
#         a, b, c, d = map(int, str(num))
#         nums_arr = [a, b, c, d]
        
#         set_of_uniq_nums = set(nums_arr)

#         if len(nums_arr) == len(set_of_uniq_nums):
#             if int(str(f"{nums_arr[0]}{nums_arr[1]}")) - int(str(f"{nums_arr[2]}{nums_arr[3]}")) == sum(nums_arr):
#                 print(num)

# get_solution()

# Подсчитать количество двузначных чисел, кратных трем
# def get_count_nums_multiplies_three():
#     count = 0
#     for num in range(10, 100):
#         if num % 3 == 0:
#             count += 1
#     print('Количество двузначных чисел кратных 3:', count)

# get_count_nums_multiplies_three()

# Дано натуральное число n. Найти сумму s = 2/5 + 2/9...
# def get_sum(n: int) -> float:
#     sum = 0
#     cur_divider = 5

#     for num in range(n):
#         sum += 2 / cur_divider
#         cur_divider += 4
    
#     print(sum)
#     return sum

# get_sum(3)

# Найти число Фибоначи и посчитать сумму первых n чисел
# def get_fibonacci_number(n: int) -> list[int]:
#     nums_arr = []

#     for index, num in enumerate(range(n)):
#         if len(nums_arr) == 0 or len(nums_arr) == 1:
#             nums_arr.append(num)
#         else:
#             new_num = nums_arr[index - 1] + nums_arr[index - 2]
#             nums_arr.append(new_num)
    
#     print(f"Числа фибоначи до {n}", nums_arr)
#     print(f"Сумма чисел до {n}:", sum(nums_arr))

#     return nums_arr

# get_fibonacci_number(10)

# Посчитать сложный процент при вкладе в банк
# def get_sum(s: int, p: int):
#     cur_sum = s
#     percent = p / 100 + 1
#     for num in range(1, 100):
#         print(num, round(cur_sum))
#         cur_sum = cur_sum * percent
#         if s * 3 < cur_sum:
#             print("Сумма утроится к", num, "году")
#             break

# get_sum(5000, 20)