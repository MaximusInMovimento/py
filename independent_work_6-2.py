def cutter(tpl, num):
    if tpl.count(num) == 0:
        return tpl
    lst = list(tpl)
    i = lst.index(num)
    lst.pop(i)
    return tuple(lst)


print(cutter((1, 2, 3), 1))
print(cutter((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3))
print(cutter((2, 4, 6, 6, 4, 2), 9))
