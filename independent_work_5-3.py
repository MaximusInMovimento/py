from heron import square

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

triangle1 = [min(one), min(two), min(three)]
triangle2 = [max(one), max(two), max(three)]

print(f"Площадь треугольника 1 со сторонами {triangle1[0]}, {triangle1[1]} и {triangle1[2]} = {square(triangle1[0],
      triangle1[1], triangle1[2])}")
print(f"Площадь треугольника 2 со сторонами {triangle2[0]}, {triangle2[1]} и {triangle2[2]} = {square(triangle2[0],
      triangle2[1], triangle2[2])}")
