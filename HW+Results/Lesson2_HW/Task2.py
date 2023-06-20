"""Для списка реализовать обмен значений соседних элементов,
т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input()."""

item = input("Введите список, разделяя значения запятой >>> ").split(",")

max_idx = len(item) - 1

for idx in range(0, max_idx, 2):
    next_idx = idx + 1
    item[idx], item[next_idx] = item[next_idx], item[idx]

print(item)
