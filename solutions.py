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

# Найти первый неповторяющийся символ в строке
# def get_first_uniq_symbol(string: str):
#     for symbol in string:
#         if string.index(symbol) == string.rindex(symbol):
#             print(symbol)
#             break

# get_first_uniq_symbol('123214')

# Перевести в верхний регистр первую и последнюю букву каждого слова
# def change_case_first_and_last_symbol_of_every_word(sentence: str):
#     splitted_sentence = sentence.split(' ')
#     new_sentence = []
#     for word in splitted_sentence:
#         new_word = word[0].upper() + word[1:-1] + word[-1].upper()
#         new_sentence.append(new_word)
#     return ' '.join(new_sentence)

# print(change_case_first_and_last_symbol_of_every_word('один два три'))

# Подсчитайте количество символов в заданной строке без пробелов
# def get_count_of_symbols_without_spaces(sentence: str) -> int:
#     return len(sentence.replace(' ', ''))

# print(get_count_of_symbols_without_spaces('три два1 1'))

# Получить расширение файла
# def get_extension(path: str) -> str:
#     extension = path.split('\\')[-1].split('.')[1]
#     return extension

# print(get_extension('C:\Folder\Subfolder\12sw\filename.txt'))

# Получить самое короткое слово предложения
# def get_shortest_word_in_sentence(sentence: str) -> str:
#     splitted_sentence = sentence.split()
#     nums_arr = []

#     for word in splitted_sentence:
#         nums_arr.append(len(word))

#     min_length_word_index = nums_arr.index(min(nums_arr))

#     return splitted_sentence[min_length_word_index]

# print("Наименьшая строка в предложении:", get_shortest_word_in_sentence('один два тричетыре'))
    
# Перевернуть порядок слов в строке
# def get_reverse_sentence(sentence: str) -> str:
#     strings_arr = sentence.replace(';', ' ').split()
#     strings_arr.reverse()
#     return ' '.join(strings_arr)

# print(get_reverse_sentence("три;;;два;один"))

# Вывести строку, содержащую символы строки S, между которыми вставлено по N символов "#".
# def update_string(string: str, n: int) -> str:
#     insert_n_string = '#' * n
#     symbols_arr = []

#     for symbol in string:
#         if symbol != ' ':
#             symbols_arr.append(symbol)

#     return insert_n_string.join(symbols_arr)

# print(update_string('123 dmk2l', 2))

# Зашифровать строку, состяющую из английских слов, разделенных запятыми
# def encrypt_string(string: str) -> str:
#     encrypted_string = ''

#     for index, symbol in enumerate(string):
#         if index % 2 != 0:
#             encrypted_string = encrypted_string + symbol
        
#     for index, symbol in enumerate(string[::-1]):
#         if index % 2 == 0:
#             encrypted_string = encrypted_string + symbol
    
#     return encrypted_string

# print(encrypt_string('одиннадцать'))

# Заменить все вхождения заданного слова в строке на другое заданное слово
# def replace_all_occurrences(string: str, target: str, replaceable: str) -> str:
#     strings_arr = string.split(' ')
#     for index, word in enumerate(strings_arr):
#         if word == target:
#             strings_arr[index] = replaceable
#     result = ' '.join(strings_arr)
#     return result

# print(replace_all_occurrences('один два три один', 'один', 'четыре'))


# Получить строку с перевернутыми словами
# def reverse_words_in_sentece(sentence: str) -> str:
#     splited_sentence = sentence.split()
#     reversed_strings_arr = []

#     for word in splited_sentence:
#         reversed_word = ''
#         for char in word:
#             reversed_word = char + reversed_word

#         reversed_strings_arr.append(reversed_word)

#     result = ' '.join(reversed_strings_arr)
#     return result


# print(reverse_words_in_sentece('один два три'))

# Подсчитать количество слов в заданной строке, которые состоят из заглавных букв
# def get_uppercase_words_count(sentence: str) -> int:
#     splitted_string = sentence.split()
#     count = 0
#     for word in splitted_string:
#         if word.swapcase() == word.lower():
#             count += 1
#     return count

# print(get_uppercase_words_count('один ОДИН один ОДИН '))

# Удалить символы, которые имеют нечетные значения индексов
# def delete_odd_symbols(sentence: str) -> str:
#     result = ""
#     for index, symbol in enumerate(sentence):
#         if index % 2 == 0:
#             result = result + symbol
#     return result

# print(delete_odd_symbols("один два"))

# Добавить ing в конце строки
# def add_ing(sentence: str):

#     if len(sentence) < 3:
#         return sentence
    
#     if len(sentence.split("ing")) == 2:
#         return sentence + "ly"
    
# print(add_ing("22"))

# Получить строку, в которой все вхождения ее первого символа были заменаны на $, кроме первого
# def replace_occurrence_character_in_string(string: str) -> str:
#     replace_to = string[0]
#     result = ''
    
#     for index, symbol in enumerate(string):
#         if symbol == replace_to and index != 0:
#             result = result + "$"
#         else: 
#             result = result + symbol
    
#     return result

# print(replace_occurrence_character_in_string("привет как дела папа"))

# Вывести самое длинное слово в предложении
# def get_longest_word(sentence: str) -> str:
#     splitted_sentence = sentence.split()
#     max_length_word = max(splitted_sentence, key=len)
#     return max_length_word

# print(get_longest_word("привет как дела хорошо семьсем"))

# Преобразовать заданную строку так, чтобы каждое слово состояло из заглавных букв
# def get_uppercase_string(string: int) -> int:
#     splitted_uppercase_string = string.upper().split()
#     return " ".join(splitted_uppercase_string)

# print(get_uppercase_string("Привет   как дела     "))

# Получить строку, в которой все буквы замененына след букву алфавита
# def get_next_letter(string: str) -> str:
#     result = ""
#     for char in string:
#         if char == 'z' or char == 'Z':
#             result += 'a'
#         elif char.isalpha():
#             next_char_code = ord(char) + 1
#             if char.isupper():
#                 next_char = chr(next_char_code).upper()
#             else:
#                 next_char = chr(next_char_code)
#             result += next_char
#         else:
#             result += char
#     return result

# print(get_next_letter("abcdz"))

# Заменить все буквы на порядковые номера в алфавите
# def switch_to_numbers(string: str) -> str:
#     result = ""

#     for char in string:
#         result = result + str(ord(char) - ord('a') + 1)
    
#     return result

# print(switch_to_numbers('ac'))

# Получить палиндром
# def get_palindrom(string: str) -> str:
#     result = ''
#     for char in string:
#         result = char + result
    
#     print(result)
#     if result == string:
#         return 'Palindrom!'
#     else:
#         return 'Not palindrom'
    
# print(get_palindrom('abba abba1'))

# Поменять местами минимальный и максимальный элементы массива
# def switch_max_and_min_nums(arr: list[int]) -> list[int]:
#     min_num = min(arr)
#     max_num = max(arr)
#     min_index = arr.index(min_num)
#     max_index = arr.index(max_num)

#     arr[min_index] = max_num
#     arr[max_index] = min_num
#     return arr

# print(switch_max_and_min_nums([1, 2, 3]))

# Найти два соседних элемента, которые дают максимальную сумму
# def get_max_neighboring_elements(arr: list[int]) -> list[int]:
    
#     sum_of_neighboring_elements = []

#     for index, num in enumerate(arr):
#         if index + 1 != len(arr):
#             sum_of_neighboring_elements.append(
#                 arr[index] + arr[index + 1])
    
#     max_num_index = sum_of_neighboring_elements.index(max(sum_of_neighboring_elements))
#     return [arr[max_num_index], arr[max_num_index + 1]]
    
# print(get_max_neighboring_elements([10, 21, 3, 4, 52, 21]))

# Найти произведение всех элементов списка, расположенных српава от максимального элемента
# def get_multiplying_numbers(arr: list[int]) -> int:
#     index_max_num = arr.index(max(arr))
#     result = 1 

#     for num in arr[index_max_num + 1 :]:
#         result *= num

#     return result

# print(get_multiplying_numbers([1, 2, 11, 2, 2, 2, 10]))

# Найти количество взаимо противоположных пар
# def get_mutually_opposed_count(arr: list[int]) -> int:
#     count = 0

#     for num in arr:
#         if -num in arr:
#             arr.pop(arr.index(-num))
#             count += 1
    
#     return count

# print(get_mutually_opposed_count([1, -1, 2, -2, 3, -3, 33]))

# Обнулить элементы между максимальным и минимальным элементом
# def reset_elements(arr: list[int]) -> list[int]:
#     max_num_index = arr.index(max(arr))
#     min_num_index = arr.index(min(arr))
#     for index, num in enumerate(arr):
#         if index > min_num_index and index < max_num_index:
#             arr[index] = 0
#     return arr

# print(reset_elements([10, 1, 2, 3, 11, 100, 1, 20]))

# Сформировать список длинной N, первый элемент которого = A, каждый последующий больше предыдущего на B
# def generate_list(n: int, a: int, b:int):
#     arr = []

#     for num in range(n):
#         if num == 0:
#             arr.append(a)
#         else:
#             incremented_num = arr[-1] + b
#             arr.append(incremented_num)
    
#     return arr

# print(generate_list(10, 1, 2))

# Получить все положительные числа по возрастанию
# def get_sorted_positive_nums(arr: list[int]) -> list[int]:
#     positive_arr = []

#     for num in arr:
#         if num >= 0:
#             positive_arr.append(num)
#     return sorted(positive_arr)

# print(get_sorted_positive_nums([-1, 5, 2, 0, 10, -10, 1000, -1000]))

# Получить все положительные числа по убыванию
# def get_reverse_sorted_positive_nums(arr: list[int]) -> list[int]:
#     positive_arr = []

#     for num in arr:
#         if num >= 0:
#             positive_arr.append(num)
#     return sorted(positive_arr, reverse=True)

# print(get_reverse_sorted_positive_nums([-1, 5, 2, 0, 10, -10, 1000, -1000]))

# Выбрать нечетные числа на нечетных позициях по убыванию
# def get_odd_reverse_nums(arr: list[int]) -> list[int]:
#     odd_nums = []

#     for index, num in enumerate(arr):
#         if index % 2 == 0:
#             odd_nums.append(num)

#     return sorted(odd_nums, reverse=True)

# print(get_odd_reverse_nums([-1, 5, 2, 500, 200, 400, 0, 10, -10, 1000, -1000]))

# Отсортировать список по длине строк от самой короткой к самой длинной
# def get_sorted_list(arr: list[str]) -> list[str]:
#     sorted_list = sorted(arr, key=len)
#     return sorted_list
    
# print(get_sorted_list(["три", "четыре", "пять", "шесть", "восемь", "десять"]))

# Отсортировать все двузначные числа массива
# def sort_double_digits(arr: list[int]) -> list[int]:
#     result = []

#     for num in arr:
#         if num > 9 and num < 100:
#             result.append(num)
    
#     return sorted(result)

# print(sort_double_digits([1, 2, 80, 10, 70, 10, 99, 100]))

# Отсортировать все двузначные числа по возрастнию последней цифры
# def sort_double_digits_by_last_char(arr: list[int]) -> list[int]:
#     double_digits = []

#     for num in arr:
#         if num > 9 and num < 100:
#             double_digits.append(num)

#     def last_digit(number: int) -> int:
#         return number % 10
    
#     sorted_nums = sorted(double_digits, key=last_digit)
#     return sorted_nums

# print(sort_double_digits_by_last_char([1, 2, 81, 12, 73, 16, 99, 100]))

# Отсортировать двузначные числа по убыванию первой цифры
# def sort_double_digits_by_first_char(arr: list[int]) -> list[int]:
#     double_digits = []

#     for num in arr:
#         if num > 9 and num < 100:
#             double_digits.append(num)
        
#     def first_digit(number: int) -> int:
#         return number // 10
    
#     sorted_nums = sorted(double_digits, key=first_digit)
#     return sorted_nums

# print(sort_double_digits_by_first_char([21, 22, 1, 2, 81, 12, 73, 16, 99, 100]))

# Отсортировать список по перевернутому алфавиту
# def get_sorted_list(arr: list[int]) -> list[int]:
#     sorted_arr = sorted(arr, key=str.lower, reverse=True)
#     return sorted_arr

# print(get_sorted_list(['б', 'а', 'ф', 'ы', 'я', 'ч']))

# Получить все двузначные числа и отсортировать их по возрастанию суммы цифр
# def get_sorted_list(arr: list[int]) -> list[int]:
#     double_digits = []
#     sum_of_nums = []
#     result = []

#     for num in arr:
#         if num > 9 and num < 100:
#             double_digits.append(num)

#             first_digit = num // 10
#             second_digit = num % 10
#             sum_of_nums.append(first_digit + second_digit)
    
#     for sum in sorted(sum_of_nums):
#         for double_digit_num in double_digits:
#             first_digit = double_digit_num // 10
#             second_digit = double_digit_num % 10

#             if sum == first_digit + second_digit:
#                 result.append(double_digit_num)

#     return result

# print(get_sorted_list([100, 50, 20, 21, 54, 89, 1, 4, 76]))

# Получить два максимальных числа и два минимальных из массива
# def max_and_min_nums(arr: list[int]) -> list[int]:
#     list = arr[:]

#     max_values_index = []
#     min_values_index = []

#     max_values_index.append(list.index(max(list)))
#     min_values_index.append(list.index(min(list)))
#     list.pop(max_values_index[0])
#     list.pop(min_values_index[0])
#     max_values_index.append(list.index(max(list)))
#     min_values_index.append(list.index(min(list)))

#     sorted_max = sorted(max_values_index, reverse=True)
#     sorted_min = sorted(min_values_index, reverse=True)

#     return [arr[sorted_max[0]], arr[sorted_max[1]], arr[sorted_min[0]], arr[sorted_min[1]]]

# print(max_and_min_nums([100, 50, 20, 21, 54, 89, 1, 4, 76]))