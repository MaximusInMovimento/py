class Figure:
    def __init__(self, title):
        self.title = title

    def move(self):
        print(f"{self.title} ходит")


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
p.move()

k = Knight()
k.move()
