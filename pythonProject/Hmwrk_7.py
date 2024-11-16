class Counter:
    def __init__(self, max_number):
        self.i = 0
        self.max_number = max_number

    def __iter__(self):
        self.i = 0
        return self.generator()

    def generator(self):
        for i in range(self.max_number + 1):
            for number in range(1, self.max_number + 1):
                yield number ** i

count = Counter(5)

for value in count:
    print(value)