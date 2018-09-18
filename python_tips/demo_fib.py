

class Fib():

    def __init__(self):
        self.pre = 0
        self.cur = 1

    def __iter__(self):

        return self

    def __next__(self):
        value = self.cur
        self.cur += self.pre
        self.pre = value

        return value

