def magic(tpl, num):

    if tpl.count(num) == 0:
        return ()
    lst = list(tpl)

    fst = lst.index(num)
    lst.pop(fst)

    if lst.count(num) == 0:
        scd = len(tpl) - 2
    else:
        scd = lst.index(num)

    return tpl[fst:scd+2]


print(magic ((1, 2, 3), 8))
print(magic((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(magic ((1, 2, 8, 5, 1, 2, 9), 8))
