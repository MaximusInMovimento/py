s = float(input("Введите сумму затрат (в рублях): "))

f = open("expenses.txt", "a")
f.write("Сумма затрат - " + str(s) + " руб.")
f.close()
