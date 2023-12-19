from random import randint


def give_me_dict():
    dct = {}
    for i in range(5):
        dct.update({randint(1, 1000): randint(1, 1000)})
    return dct


print(give_me_dict())
print(give_me_dict())
print(give_me_dict())
