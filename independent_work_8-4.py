from datetime import datetime


class Figure:
    def __init__(self, title):
        self.title = title
        self.__created_at = datetime.now()

    def move(self):
        print(f"{self.title} ходит")

    def history(self):
        print(f"Фигура создана " + str(self.__created_at))


class King(Figure):
    def __init__(self):
        super().__init__("Король")


class Queen(Figure):
    def __init__(self):
        super().__init__("Ферзь")


class Pawn(Figure):
    def __init__(self):
        super().__init__("Пешка")


class Bishop(Figure):
    def __init__(self):
        super().__init__("Слон")


class Knight(Figure):
    def __init__(self):
        super().__init__("Конь")


p = Pawn()
p.history()
print(p.__created_at)