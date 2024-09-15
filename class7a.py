class Counter:
    def __init__(self):
        self.__current = 0

    def increment(self):
        self.__current += 1

    def value(self):
        return self.__current

    def reset(self):
        self.__current = 0

c1 = Counter()
c1.increment()
c1.increment()
c1.__current = -99
print(c1.value())
