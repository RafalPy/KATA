class Fib:
    def __init__(self, limit):
        self.limit = limit
        self.generator = self._generator()

    def _generator(self):
        counter = 0
        a = 0
        b = 1
        for i in range(self.limit + 1):
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

    @staticmethod
    def run_many_times(x):
        fib.generate()
        counter2 = 1
        while counter2 <= x:
            if counter2 == fib.limit:
                break
            fib.generate()
            counter2 += 1
    def overwrite_limit (self, new_limit):
        self.limit = new_limit

    def clear_memory(self):
        self.generator = self._generator()


fib = Fib(12)
print(fib.limit)
fib.run_many_times(13)

fib.clear_memory()
fib.overwrite_limit(13)
print(fib.limit)
fib.run_many_times(13)