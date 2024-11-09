class Counter:
    def __init__(self, max_number):
        self.i = 0
        self.max_number = max_number

    def __iter__(self):
        self.i = self.max_number + 1
        return self

    def __next__(self):
        self.i += 1
        if self.i < 0:
            raise StopIteration
        return self.i


count = Counter(5)
for elem in count:
    print(elem)