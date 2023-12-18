def fix(lst):
    bads = set()
    for i, ball in enumerate(lst):
        if ball == 3:
            lst[i] = 4
        if ball == 2:
            bads.add(i)

    while len(bads) > 0:
        rm = max(bads)
        lst.pop(rm)
        bads.remove(rm)
    return lst


list_1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
list_2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
list_3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

print(list_1)
fix(list_1)
print(list_1)

print(list_2)
fix(list_2)
print(list_2)

print(list_3)
fix(list_3)
print(list_3)
