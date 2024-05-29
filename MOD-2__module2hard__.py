
import random







# здесь мы получаем пароль для рандомно выбранных чисел
# выводим постррочно

# def find_pairs_for_number(target_number):
#
#     pairs = []
#
#     for i in range(1, target_number + 1):
#         for j in range(i, target_number + 1):
#             if (i != j) and ((i + j) % target_number == 0):
#                 pairs.append((f'{i}{j}'))       # Добавляем найденную пару в список
#     return pairs
#
# random_number = random.randint(3, 20)     # Генерируем случайное число от 3 до 20
# numbers = find_pairs_for_number(random_number)  # присваиваем результат функции
# result = "".join(map(str, numbers))
# print(f'{random_number}-{result}')







# это вариант вывода всех паролей всего диапазона вводимых чисел
# выводим списком

def find_pairs_for_number(target_number):
    pairs = []
    for i in range(1, target_number + 1):
        for j in range(i, target_number + 1):
            if (i != j) and ((i + j) % target_number == 0):  # исправленно здесь! я добавил сравнение что бы оставить
                                                             # только уникальные пары
                                                             # и что бы была кратность на target_number
                pairs.append(f'{i}{j}')
    return pairs

for number in range(3, 21):                    # Перебираем числа от 3 до 20 включительно
    numbers = find_pairs_for_number(number)    # Присваиваем результат функции
    result = "".join(map(str, numbers))
    print(f'{number}-{result}')







# это вариант через while

# def find_pairs_for_number(target_number):
#     pairs = []
#     i = 1
#     while i <= target_number:
#         j = i
#         while j <= target_number:
#             if (i != j) and ((i + j) % target_number == 0):
#                 pairs.append(f'{i}{j}')  # Добавляем найденную пару в список
#             j += 1
#         i += 1
#     return pairs
#
#                                          # Перебираем числа от 3 до 20 включительно с помощью цикла while
# i = 3
# while i <= 20:
#     numbers = find_pairs_for_number(i)   # Присваиваем результат функции
#     result = "".join(map(str, numbers))  # Преобразуем список пар в строку
#     print(f'{i}-{result}')
#     i += 1



