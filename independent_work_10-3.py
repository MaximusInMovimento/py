total_num = 2

for i in range(5):

    is_val = False
    while not is_val:
        num = input(f"Итоговый результат {total_num}. Введите число: ")
        try:
            val = int(num)
            is_val = True
            total_num += val

        except ValueError as ex:
            val = 0
            print("Неподходящий тип данных. Ожидалось число")
print(f"Итоговый результат {total_num} ")
