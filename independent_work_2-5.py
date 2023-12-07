import datetime
d, m, y = list([datetime.datetime.now().day, datetime.datetime.now().strftime("%B"), datetime.datetime.now().year])
print(f"Сегодня {d} {m} {y}. ", end="Всего хорошего!")
