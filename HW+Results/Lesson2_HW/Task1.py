"""Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно,
 в программе."""

task_list = [6, 3.14, True, "String text", [], {}, ()]

for item in task_list:
    print(item, ' >>> this is ', type(item))
