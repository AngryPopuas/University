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
...
numbers = [0,1,2,3,4,5]
for item in numbers:
    print(item)
...


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
...

a = [i ** 2 for i in range(1,5)]

print('a - ', a)
for i in a:
    print(i)

print('iter(a) - ', iter(a))

for i in a:
    print(i)

...
b = [i ** 2 for i in range(1,5)]

print(b)
print('first')
for i in b:
    print(i)
print('second')

for i in b:
    print(i)

###
def countdown(count):
    while count >= 0:
        yield count
        count -= 1

if __name__ == '__main__':
    counter = countdown(5)
    for i in counter:
        print(i)
