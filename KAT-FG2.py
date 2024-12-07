class Fib:
    def __init__(self, limit):
        self.limit = limit
        self.generator = self._generator()

    def _generator(self):
        counter = 0
        a = 0
        b = 1
        for i in range(self.limit):
            if counter == 0:
                counter += 1
                yield 0
            if counter == 1:
                counter += 1
                yield 1
            else:
                a, b = b, a + b
                yield a + b


    def generate(self):
        print(next(self.generator))

fib = Fib(10)

def run_many_times(x):
    counter = 1
    while counter <= x:
        if counter == fib.limit:
            break
        fib.generate()
        counter +=1

run_many_times(14)