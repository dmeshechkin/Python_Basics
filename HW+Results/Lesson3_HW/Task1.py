"""
Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.
"""


def main(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Ошибка! На ноль делить нельзя! (Ну как бы можно, но нельзя!)"


a = int(input("Введите число a >>> "))
b = int(input("Введите число b >>> "))

print(f'Результатом деления {a} на {b} будет {main(a, b)}')
