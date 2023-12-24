class Figure:
    def __init__(self, title):
        self.title = title

    def move(self):
        print(f"{self.title} ходит")


f = Figure("Король")
f.move()
