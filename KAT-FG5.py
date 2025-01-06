def fib(x = 100):
    a = 0
    b = 1
    counter = 0
    for i in range(x):
        if a == 0:
            counter += 1
            yield a
        if a == 1 and counter < 2:
            counter += 1
            yield a
        yield a + b
        a, b = b, a + b


def print_fibonacci(how_many=10):
    fib_gen = fib()
    for i in range(how_many):
        print(next(fib_gen))
        i += 1

print_fibonacci()
