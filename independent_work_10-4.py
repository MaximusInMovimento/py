def waitint(func):
    def wrapper():
        original_result = func()

        try:
            val = int(original_result)
        except ValueError:
            val = 1
            print("Неподходящий тип данных. Ожидалось число. Число всегда будет 1")

        return val

    return wrapper


@waitint
def request_name():
    my_fav = input("Введите ваше любимое число:")
    return my_fav


@waitint
def request_age():
    my_age = input("Введите возраст:")
    return my_age


print(f"Любимое число {request_name()}")
print(f"Возраст {request_age()}")
