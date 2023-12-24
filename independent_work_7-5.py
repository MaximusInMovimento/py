val = int(input("Введите число от 10 до 20: "))

if val < 10 or val > 20:
    print("Не соответствует")
else:
    f = open("independent_work_7-5.py")
    lines = f.readlines()
    f.close()
    f = open(f"{val}.py", "a")
    f.writelines(lines)
    f.close()
