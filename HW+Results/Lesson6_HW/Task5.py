"""
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).

Метод выводит сообщение “Запуск отрисовки.”

Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).

В каждом из классов реализовать переопределение метода draw.

Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для
каждого экземпляра.
"""

class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f"Запуск отрисовки {self.title}"


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"Вы взяли {self.title}. {self.title} может рисовать на парте."


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"Вы взяли {self.title}. {self.title} может рисовать на листе."


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"Вы взяли {self.title}. {self.title} может рисовать на доске."


pen = Pen("Ручка")
pencil = Pencil("Карандаш")
handle = Handle("Маркер")
print(pen.draw())
print(pencil.draw())
print(handle.draw())