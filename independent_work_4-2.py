from random import randint


def throw_dice():
    dice = randint(1, 6)
    print(f" ---\n| {dice} | \n ---")
    if dice in [3, 4]:
        return throw_dice()
    return dice


if __name__ == '__main__':
    mydice = throw_dice()
    if mydice in [1, 2]:
        print("Вы проиграли!")
    elif mydice in [5, 6]:
        print("Вы победили!")
