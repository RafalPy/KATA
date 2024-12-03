def Fib():
    counter = 0
    a = 0
    b = 1
    for i in range(10):
        if counter == 0:
            counter += 1
            yield 0
        if counter == 1:
            counter += 1
            yield 1
        else:
            a, b = b, a + b
            yield a + b



generator = Fib()

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))