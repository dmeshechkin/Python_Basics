"""
Реализовать функцию int_func(), принимающую слово из маленьких
латинских букв и возвращающую его же, но с прописной первой буквой.

Например, print(int_func(‘text’))-> Text.

Продолжить работу над заданием. В программу должна попадать
строка из слов, разделенных пробелом. Каждое слово состоит
из латинских букв в нижнем регистре. Сделать вывод исходной
строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(input_word: str):
    return "".join([
        input_word[0].upper(), input_word[1:]
    ])


user_words = input(
    "Введите строку из слов разделенных пробелом >>> "
).split()

user_words = [int_func(x) for x in user_words]

print(" ".join(user_words))