from functools import lru_cache

@lru_cache(None)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == '__main__':
    print(fibonacci(100))

def check(input_func):
    def output_func(*args):
        name, age = args[0], args[1]

        if age < 0 or age > 130:
            age = 'Недопустимый возраст'
        input_func(name,age)

    return output_func

@check
def personal_info(name,age):
    print(f"Name: {name} Age: {age}")

if __name__ == '__main__':
    personal_info('Владимир',38)
    personal_info('Александр',-5)
    personal_info('Петр',138,15,48,2)

def data(*args):
    try:
        for i in range(len(*args)):
            try:
                result = (args[0][i] * 15) // 10
                print(result)
            except Exception as ex:
                print(ex)
    except Exception as ex:
        print(ex)
    finally:
        print('Вся информация обработана')

if __name__ == '__main__':
    data([1,15,'Hello','i','try','to','crash','your','site',38,45])

class NegativeValueException(Exception):
    pass

def check_name(name):
    if len(name > 10):
        raise NegativeValueException('Длинна более 10 символов')
    else:
        print('Успешная регистрация')

if __name__ == '__main__':
    name = '1234567810'
    check_name(name)

class SiteChecker:
    def __init__(self,func):
        print('> Класс SiteChecker метод __init__ успешный запуск')
        self.func = func

    def __call__(self):
        print('Ю Проверка перед запуском', self.func.__name__)
        self.func()
        print('> Проверка безопасного выключения')

@SiteChecker
def site():
    print('Усердная работа сайта')

if __name__ == '__main__':
    print('>> Сайт запущен')
    site()
    print('>> Сайт выключен')

import time
def fibonacci(function):
    def wrapped(*args):
        fib1 = fib2 = 1

        start_time = time.perf_counter_ns()
        for i in range(2,200):
            fib1, fib2 = fib2, fib1 + fib2
            print(fib2, end='')

        res = function(*args)
        print(time.perf_counter_ns() - start_time)
        return res
    return wrapped

@fibonacci
def func(first, second):
    return bin(int(first, 2) + int(second, 2))

class NegativeValueException(Exception):
    pass

def check_name():
    f = open('text.txt', 'r')
    if f.read() == '':
        raise NegativeValueException('Файл пустой')
    else:
        print(f)

if __name__ == '__main__':
    check_name()

def data(args):
    try:
        result = args + 2
        print(result)
    except Exception as ex:
        print('Неподходящий тип данных. Ожидалось число')

if __name__ == '__main__':
    data(20)

def a_decorator_passing_arguments(function_to_decorate):
    def a_wrapper_accepting_arguments(arg1, arg2):
        print
        "Смотри, что я получил:", arg1, arg2
        function_to_decorate(arg1, arg2)

    return a_wrapper_accepting_arguments

@a_decorator_passing_arguments
def print_full_name(first_name, last_name):
    print
    "Меня зовут", first_name, last_name


print_full_name("Питер", "Венкман")

class MyCustomException(Exception):
    def __init__(self, message, extra_info):
        super().__init__(message)
        self.extra_info = extra_info

def divide_numbers(a, b):
    if b == 0:
        raise MyCustomException("Деление на ноль невозможно", {"a": a, "b": b})
    return a / b

try:
    result = divide_numbers(10, 0)
except MyCustomException as e:
    print(f"Сообщение об ошибке: {e}")
    print(f"Дополнительная информация: {e.extra_info}")
