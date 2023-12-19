from random import randint

s = ""
for i in range(15 + randint(0, 15)):
    s += str(randint(0, 9))

print(f"Исходная случайная строка случайной длины({len(s)}): {s}")


def give_me_dict(st):
    tpl = tuple(st)
    dct = {}
    for num in tpl:
        dct.update({int(num): tpl.count(num)})

    srtd = sorted(dct.items(), key=lambda x: x[1])
    srtd.reverse()
    srtd = srtd[:3]

    dct = dict(srtd)
    dct = dict(sorted(dct.items()))

    print(dct)


give_me_dict(s)
