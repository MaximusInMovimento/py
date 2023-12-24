from datetime import datetime


class MyDecorator:

    def __init__(self, func):
        self.func = func

    def __call__(self):
        start = datetime.now()
        print('\nВремя старта: ' + str(start))

        self.func()

        # фиксируем и выводим время окончания работы кода
        finish = datetime.now()
        print('\nВремя окончания: ' + str(finish))


@MyDecorator
def fibonacci():
    fib1 = fib2 = 1

    for i in range(2, 200):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end=' ')


if __name__ == '__main__':
    fibonacci()
