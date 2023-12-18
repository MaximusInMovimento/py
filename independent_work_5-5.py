def func(lst):
    s = set()
    for i, num in enumerate(lst):
        if num in s:
            st = str(num)
            for z in range(lst[:i].count(num)):
                st += str(num)
            s.add(st)
        else:
            s.add(num)
    return s


list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

print(list_1)
print(func(list_1))

print(list_2)
print(func(list_2))

print(list_3)
print(func(list_3))
