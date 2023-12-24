from datetime import datetime


class Figure:
    def __init__(self, title):
        self.title = title
        self.__created_at = datetime.now()

    def move(self):
        print(f"{self.title} ходит")

    def history(self):
        print(f"Фигура создана " + str(self.__created_at))

    def can_move(self):
        pass


class King(Figure):
    def __init__(self):
        super().__init__("Король")

    def can_move(self):
        print("Король может хотить на одну клетку в любую сторону")


class Queen(Figure):
    def __init__(self):
        super().__init__("Ферзь")

    def can_move(self):
        print("Ферзь может хотить на сколько угодно клеток по вертикали, диагонали или горизонтали")


class Pawn(Figure):
    def __init__(self):
        super().__init__("Пешка")

    def can_move(self):
        print("Пешка может хотить одно или два поля вперед. Пешка рубит по диагонали")


class Bishop(Figure):
    def __init__(self):
        super().__init__("Слон")

    print("Слон может хотить по диагонали")


class Knight(Figure):
    def __init__(self):
        super().__init__("Конь")

    print("Конь может хотить буквой Г")


white = [Pawn(), King(), Queen(), Bishop(), Knight()]

for figure in white:
    figure.can_move()