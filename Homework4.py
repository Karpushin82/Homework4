# Вычислить число Пи c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001


def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = float(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Какое-то неправильное число!")
    return number


def division(num1, num2):
    return num1 / num2


num1 = InputNumbers("Введите 1 число: ")
num2 = InputNumbers("Введите 2 число: ")
n = int(InputNumbers("Введите точность (количество знаков после запятой): "))
rezult = round(division(num1, num2), n)

print(f"Результат деления: {rezult}")

""""

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Какое-то неправильное число!")
    return number


def func_search(num):
    rezult = []

    for i in range(2, num):
        while num % i == 0:
            num /= i
            rezult.append(i)
    return rezult


num = InputNumbers("Введите натуральное число N: ")


print(f"Результат деления: {func_search(num)}")

"""