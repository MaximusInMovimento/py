class MyException(Exception):
    pass


def my_check(fn):
    f = open(fn, 'r')
    lines = f.readlines()
    if len(lines) == 0:
        raise MyException()


file_list = ['empty-file-1.txt', 'empty-file-2.txt', 'empty-file-3.txt',
             'no-empty-file-1.txt', 'no-empty-file-2.txt', 'no-empty-file-3.txt']

for file_name in file_list:
    try:
        my_check(file_name)
    except MyException as ex:
        print(f"Файл {file_name} пустой!")
    finally:
        print(f"Файл {file_name} проверен!")
