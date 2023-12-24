class More50Exception(Exception):
    pass


def request_name():
    my_fav = int(input("Введите ваше любимое число: "))
    if my_fav > 50:
        raise More50Exception
    return my_fav


def request_age():
    my_age = int(input("Введите возраст: "))
    if my_age > 50:
        raise More50Exception
    return my_age


print(f"Любимое число {request_name()}: ")
print(f"Возраст {request_age()}: ")
