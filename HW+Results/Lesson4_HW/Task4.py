"""
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.

Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""

numbers = [1, 2, 5, 15, 5, 7, 151, 9, 101, 7, 4, 44, 10, 66, 131, 5, 151, 795, 89, 89, 4]
items = [x for x in numbers if numbers.count(x) == 1]

print(items)

