# **Тема 9. Концепции и принципы ООП**

Отчёт по теме #9 выполнил

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

  Допустим, что вы решили оригинально и немного странно познакомится с человеком. Для этого у вас должен быть написан свой класс на Python, который будет проверять угадал ваше имя человек или нет. Для этого создайте класс, указав в свойствах только имя. Дальше создайте функцию __init__(), а в ней сделайте проверку на то угадал человек ваше имя или нет. Также можете проверить что будет, если в этой функции указав атрибут, который не указан в вашем классе, например, попробуйте вызвать фамилию.
  ```
class Ivan:
    __slots__ = ['name']

    def __init__(self,name):
        if name == 'Иван':
            self.name = f"Да я {name}"
        else:
            self.name = f"Я не {name}, а Иван"
```
  ![Desktop Screenshot 2023 12 02 - 01 04 47 29](https://github.com/AngryPopuas/University/assets/121407501/0efbcbb4-eb7b-4348-8335-45584daa3b28)


# Лабораторная работа №2

  2) Вам дали важное задание, написать продавцу мороженого программу, которая будет писать добавили ли топпинг в мороженое и цену после возможного изменения. Для этого вам нужно написать класс, в котором Михаил А. Панов будет определяться изменили ли состав мороженого или нет. В этом классе реализуйте метод, выводящий на печать «Мороженое с {ТОППИНГ}» в случае наличия добавки, а иначе отобразится следующая фраза: «Обычное мороженое». При этом программа должна воспринимать как топпинг только атрибуты типа string.

```
  class Icecream:
    def __init__(self,ingredient=None):
        if isinstance(ingredient,str):
            self.ingredient = ingredient
        else:
            self.ingredient = None

    def composition(self):
        if self.ingredient:
            print(f"Мороженное с {self.ingredient}")
        else:
            print("Обычное мороженное")

icecream = Icecream()
icecream.composition()
icecream = Icecream('Шоколадное')
icecream.composition()
icecream = Icecream(5)
icecream.composition()
```
![Desktop Screenshot 2023 12 02 - 01 12 13 96](https://github.com/AngryPopuas/University/assets/121407501/45a9b0ec-9be1-4a5b-9128-8ba99eccbbd8)


# Лабораторная работа №3

  Петя – начинающий программист и на занятиях ему сказали реализовать икапсу…что-то. А вы хороший друг Пети и ко всему прочему прекрасно знаете, что икапсу…что-то – это инкапсуляция, поэтому решаете помочь вашему другу с написанием класса с инкапсуляцией. Ваш класс будет не просто инкапсуляцией, а классом с сеттером, геттером и деструктором. После написания класса вам необходимо продемонстрировать что все написанные вами функции работают. Также вас необходимо объяснить Пете почему на скриншоте ниже в консоли выводится ошибка
  ```
class MyClass:
    def __init__(self,value):
        self._value = value

    def set_value(self,value):
        self._value = value

    def get_value(self):
        return self._value

    def del_value(self):
        del self._value

    value = property(get_value,set_value,del_value)

obj = MyClass(42)
print(obj.get_value())
obj.set_value(45)
print(obj.get_value())
obj.set_value(100)
print(obj.get_value())
obj.del_value()
print(obj.get_value())
```
![Desktop Screenshot 2023 12 02 - 01 16 27 72](https://github.com/AngryPopuas/University/assets/121407501/9754657d-418e-46e6-8db2-03cfbd721815)


# Лабораторная работа №4

Вам прекрасно известно, что кошки и собаки являются млекопитающими, но компьютер этого не понимает, поэтому вам нужно написать три класса: Кошки, Собаки, Млекопитающие. И при помощи Михаил А. Панов “наследования” объяснить компьютеру что кошки и собаки – это млекопитающие. Также добавьте какой-нибудь свой атрибут для кошек и собак, чтобы показать, что они чем-то отличаются друг от друга.

```
class Mammal:
    className = 'Mammal'

class Dog(Mammal):
    species = 'canine'
    sounds = 'wow'

class Cat(Mammal):
    species = 'feline'
    sounds = 'meow'

dog = Dog()
print(f"Dog is {dog.className} but they say {dog.sounds}")
cat = Cat()
print(f"Cat is {cat.className},but they say {cat.sounds}")
```
![Desktop Screenshot 2023 12 02 - 01 20 05 31](https://github.com/AngryPopuas/University/assets/121407501/b5f2f93d-cd13-4d8e-9963-924e600e67a1)


# Лабораторная работа №5

  На разных языках здороваются по-разному, но суть остается одинаковой, люди друг с другом здороваются. Давайте вместе с вами реализуем программу с полиморфизмом, которая будет описывать всю суть первого предложения задачи. Для этого мы можем выбрать два языка, например, русский и английский и написать для них отдельные классы, в которых будет в виде атрибута слово, которым здороваются на этих языках. А также напишем функцию, которая будет выводить информацию о том, как на этих языках здороваются. Заметьте, что для решения поставленной задачи мы использовали декоратор @staticmethod, поскольку нам не нужны обязательные параметры-ссылки вроде self
  ```
class Russian:

    @staticmethod
    def greeting():
        print("Метод")

class English:

    @staticmethod
    def greeting():
        print("Hello")

def greet(language):
    language.greeting()

ivan = Russian()
greet(ivan)
john = English()
greet(john)
```
![Desktop Screenshot 2023 12 02 - 01 21 55 12](https://github.com/AngryPopuas/University/assets/121407501/e0eaa0b3-196f-4f98-8876-5aede3cd6bbb)


# Самостоятельная работа №1

Класс Tomato: 1) Создайте класс Tomato 2) Создайте статическое свойство states, которое будет содержать все стадии созревания помидора 3) Создайте метод __init__(), внутри которого будут определены два динамических свойства: _index (передается параметром) и _state
(принимает первое значение из словаря states). После написания этого блока кода в комментарии к нему укажите какими являются эти два свойства 4) Создайте метод grow(), который будет переводить томат на следующую стадию созревания 5) Создайте метод is_ripe(), который будет проверять, что томат созрел

```
`class Tomato:`
    `states = {'Отсутствует': 0, 'Цветение': 1, 'Зеленый': 2, 'Красный': 3}`

    def __init__(self, index):
        self._index = index
        self._state = self.states['Отсутствует']

    def grow(self):
        if self._state < 3:
            self._state += 1

    def is_ripe(self):
        return True if self._state == 3 else False
```


![Desktop Screenshot 2023 12 02 - 00 37 32 37](https://github.com/AngryPopuas/University/assets/121407501/d4664edf-4ac7-4abf-b76b-6d54485f69c3)

# Вывод:

В данном коде создается класс Tomato 

 `states = {'Отсутствует': 0, 'Цветение': 1, 'Зеленый': 2, 'Красный': 3}` states хранит в себе статистические свойства созревания


 ` def __init__(self, index):` - Метод класса Tomato который принимает index как параметр

  `def grow(self):` - Метод класса Tomato, прибавляет к state единицу, тем самым, переводит томат не след. стадию созревания

`def is_ripe(self):` - Метод класса Tomato, который возвращает True если state равно 3 иначе False

# Самостоятельная работа №2

Класс TomatoBush: 1) Создайте класс TomatoBush 2) Определите метод __init__(), который будет принимать в качестве параметра количество томатов и на его основе будет создавать список объектов класса Tomato. Данный список будет храниться внутри динамического свойства tomatoes 3) Создайте метод grow_all(), который будет переводить все объекты из списка томатов на следующий этап созревания 4) Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из списка стали спелыми. 5) Создайте метод give_away_all(), который будет чистить список томатов после сбора урожая


```
class TomatoBush:

    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(1, num + 1)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []
```

![Desktop Screenshot 2023 12 02 - 00 39 36 14](https://github.com/AngryPopuas/University/assets/121407501/38080743-adde-4c21-9562-8dee4ae2ac41)

# Вывод:

В данном коде создается класс TomatoBush 

`def __init__(self, num):` - Метод класса TomatoBush, принимает параметр num, который отвечает за длинну списка обьектов класса Tomato, создающихся в данном методе

`    def grow_all(self):` - Метод класса TomatoBush, который вызывает grow у всех Tomato

`def all_are_ripe(self):` - Метод класса TomatoBush, который проверяет если у всех Tomato 
state имеет значение 3 и возращает True иначе False

`    def give_away_all(self):` - Метод класса TomatoBush который очищает список tomatoes

# Самостоятельная работа №3

Класс Gardener: 1) Создайте класс Gardener 2) Создайте метод __init__(), внутри которого будут определены два динамических свойства: name (передается параметром, является публичным) и _plant (принимает объект класса TomatoBush). После написания этого блока кода в комментарии к нему укажите какими являются эти два свойства 3) Создайте метод work(), который заставляет садовника работать, что позволяет растению становиться более зрелым 4) Создайте метод harvest(), который проверяет, все ли плоды созрели. Если все, то садовник собирает урожай. Если нет, то метод печатает предупреждение 5) Создайте статический метод knowledge_base(), который выведет в консоль справку по садоводству

```
`class Gardener:`

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            print('Урожай собран!')
            self._plant.give_away_all()
        else:
            print('Томаты еще не дозрели')

    @staticmethod
    def knowledge_base():
        print('Справка по садоводству:')
        print('1. Не забывайте регулярно поливать и подкармливать растения')
        print('2. Определите правильное расстояние между растениями, чтобы они не мешали друг другу в росте')
        print('3. Удалите поврежденные листья и плоды, чтобы предотвратить распространение болезней')
```

        
![Desktop Screenshot 2023 12 02 - 00 41 42 89](https://github.com/AngryPopuas/University/assets/121407501/2486206f-83b6-4c39-ac3a-cfbd73d75985)

# Вывод:
В данном коде создается класс Gardener

`def __init__(self, name, plant):` - Это метод обьекта Gardener, который определяет 2 динамических свойства.

`def work(self):` - Это метод обьекта Gardener, который вызывает plant.grow_all()

`def harvest(self):` - Это метод обьекта Gardener, в котром if else statement проверяет, являеться ли результат self._plant.all_are_ripe() true or false, если true то вызывается self._plant.give_away_all(), если false, то просто print()

` def knowledge_base():` - Это метод обьекта Gardener, который выводит текст в консоль, используя функцию print()

# Самостоятельная работа №5

Тесты: 1) Вызовите справку по садоводству 2) Создайте объекты классов TomatoBush и Gardener 3) Используя объект класса Gardener, поухаживайте за кустом с помидорами 4) Попробуйте собрать урожай, когда томаты еще не дозрели. Продолжайте ухаживать за ними 5) Соберите урожай

```
# Вызов справки по садоводству
Gardener.knowledge_base()

# Создание объектов классов TomatoBush и Gardener
bush = TomatoBush(5)
gardener = Gardener('John', bush)

# Уход за кустом с помидорами
gardener.work()
gardener.work()
gardener.work()

# Сбор урожая
gardener.harvest()

# Продолжение ухода за кустом, пока томаты не дозреют
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()
# Сбор урожая после дозревания всех томатов
gardener.work()
gardener.harvest()
```

![Desktop Screenshot 2023 12 02 - 00 44 01 25](https://github.com/AngryPopuas/University/assets/121407501/c83c7bd5-1225-4f63-b36f-9c7be7a3792d)

# Вывод:

В данном коде создаются обьекты классов TomatoBush и Gardener

`Gardener.knowledge_base()` - Вызов справки по руководству

`gardener.work()` - Вызов метода work у обьекта gardener (Уход за кустами)

`gardener.harvest()` - Вызываем методы у того же обьекта, пока томаты не созреют

`gardener.work()
gardener.harvest()` - Вызываем методы и получаем собранные томаты





