# **ТЕМА 11. Итераторы и генераторы**

Отчёт по теме #11 выполнил

Цыганков Денис Николаевич ПИЭ-21-2


| Задание | Лаб_раб | Сам_раб |
|----------|----------|----------|
| 1    | +   | +  |
| 2   | +   | +   |
| 3    | +   | +   |
| 4    | +   | +   |
| 5    | +   | +   |

знак "+" - задание выполнено; знак "-" - задание не выполнено;
Работу проверили:  к.э.н., доцент Панов М.А.

# Лабораторная работа №1

Простой итератор, но у него нет гибкой настройки, например его нельзя развернуть. Он работает просто как next(), но нет prev()

```
numbers = [0,1,2,3,4,5]
for item in numbers:
    print(item)
```

![Desktop Screenshot 2023 12 08 - 02 39 14 23](https://github.com/AngryPopuas/University/assets/121407501/d9fccc51-fd78-4ef2-8459-29319051e9ed)

# Лабораторная работа №2

Класс итератор с гибкой настройкой и удобными применением

```
class CountDown:
    def __init__(self,start):
        self.count = start + 1
        
    def __iter__(self):
        return self

    def __next__(self):
        self.count -= 1
        if self.count < 0:
            raise  StopIteration
        return self.count

if __name__ == '__main__':
    counter = CountDown(5)
    for i in counter:
        print(i)
```

![Desktop Screenshot 2023 12 08 - 02 40 57 47](https://github.com/AngryPopuas/University/assets/121407501/ff3706f3-ddc1-4cdb-b0fe-ae202bf7745d)

# Лабораторная работа №3

Генератор списка

```
a = [i ** 2 for i in range(1,5)]

print('a - ', a)
for i in a:
    print(i)

print('iter(a) - ', iter(a))

for i in a:
    print(i)
```

![Desktop Screenshot 2023 12 08 - 02 41 54 75](https://github.com/AngryPopuas/University/assets/121407501/100f3cbc-ee7a-4029-9518-17cef2865321)

# Лабораторная работа №4

Выражения генераторы

```
b = [i ** 2 for i in range(1,5)]

print(b)
print('first')
for i in b:
    print(i)
print('second')

for i in b:
    print(i)
```

![Desktop Screenshot 2023 12 08 - 02 42 51 52](https://github.com/AngryPopuas/University/assets/121407501/7c06711a-9061-463b-bb31-1404b101b52a)
 
# Лабораторная работа №5

Такой же счетчик, как и в первом задании, только это генератор и использует yield

```
def countdown(count):
    while count >= 0:
        yield count
        count -= 1

if __name__ == '__main__':
    counter = countdown(5)
    for i in counter:
        print(i)
```


![Desktop Screenshot 2023 12 08 - 02 45 35 45](https://github.com/AngryPopuas/University/assets/121407501/de10d9a9-4e3a-476a-8fd9-1f120654b74b)



# Самостоятельная работа №1

Вас никак не могут оставить числа Фибоначчи, очень уж они вас заинтересовали. Изучив новые возможности Python вы решили реализовать программу, которая считает числа Фибоначчи при помощи итераторов. Расчет начинается с чисел 1 и 1. Создайте функцию fib(n), генерирующую n чисел Фибоначчи с минимальными затратами ресурсов. Для реализации этой функции потребуется обратиться к инструкции yield (Она не сохраняет в оперативной памяти огромную последовательность, а дает возможность “доставать” промежуточные результаты по одному). Результатом решения задачи будет листинг кода и вывод в консоль с числом Фибоначчи от 200

```
def fib(n):
    a, b = 1, 1
    for __ in range(n - 1):
        yield a
        a, b = b, a + b
print(list(fib(200)))
```

![Desktop Screenshot 2023 12 08 - 02 26 12 98](https://github.com/AngryPopuas/University/assets/121407501/c83f7102-27c3-4b0c-96ab-6f7c31547403)

# Вывод:

```def fib(n):``` - Создаем функцию

Итерируемся n раз  ```for __ in range(n)```

Сохраняем состояния ее локальных переменных  ```yield a```

Выводим резултьтат в консоль  ```print(list(fib(200)))```

# Самостоятельная работа №2

К коду предыдущей задачи добавьте запоминание каждого числа Фибоначчи в файл “fib.txt”, при этом каждое число должно находиться на отдельной строчке. Результатом выполнения задачи будет листинг кода и скриншот получившегося файла

```
def fib(n):
    a, b = 1, 1
    for i in range(n - 1):
        yield a
        a, b = b, a + b

def rem_fib():
    f = open('text.txt', 'w')
    fibResult = list(fib(200))
    for i in range(len(fibResult)):
        f.write(f"\n {fibResult[i]}")
rem_fib()
```

![Desktop Screenshot 2023 12 08 - 02 33 08 52](https://github.com/AngryPopuas/University/assets/121407501/d7c812de-05c5-4956-8df3-d552e71cbd32)

![Desktop Screenshot 2023 12 08 - 02 33 10 72](https://github.com/AngryPopuas/University/assets/121407501/c871b177-690c-476b-b39a-844d31d43f8e)

# Вывод:

```f = open('text.txt', 'w')``` - Открытваем файл для записи

Запоминаем результат функции fib(n) в fibResult ```fibResult = list(fib(200))```

Дальше проходимся циклом по всему массиву  ```for i in range(len(fibResult)):```

На каждой итерации с новой строки, записываем новое значение ```f.write(f"\n {fibResult[i]}")```



