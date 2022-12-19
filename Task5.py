"""5) Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
(отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен
выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра."""

class Stationery:
    title = "*Канцелярская принадлежность*"

    def draw(self):
        print("Родительский метод класса Stationery")
        print("Запуск отрисовки")
        print("\x1B[4m                                   \x1B[0m \n")


class Pen(Stationery):
    def draw(self):
        print("Родительский метод класса Pen")
        print("Запуск отрисовки ручкой")
        print("\x1B[34m\x1B[3mAa, Bb, Cc, Dd, Ff\x1B[0m \n")


class Pencil(Stationery):
    def draw(self):
        print("Родительский метод класса Pencil")
        print("Запуск отрисовки карандашом")
        print("\x1B[30m_/\__/\__/\__/\__/\__/\__/\__/\_\x1B[0m \n")


class Handle(Stationery):
    def draw(self):
        print("Родительский метод класса Handle")
        print("Запуск отрисовки маркером")
        print("\x1B[42m__________________________________\x1B[0m \n")


s = Stationery()
print(s.title)
s.draw()

p_1 = Pen()
p_1.draw()

p_2 = Pencil()
p_2.draw()

h = Handle()
h.draw()