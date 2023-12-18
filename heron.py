from math import sqrt


def square(a, b, c):
    # формула площади Герона: S = √(p * (p — a) * (p — b) * (p — c)).
    p = (a + b + c) / 2
    s = sqrt(p * (p - a) * (p - b) * (p - c))
    return s
