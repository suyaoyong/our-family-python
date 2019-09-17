from itertools import islice
from itertools import cycle
class fib:
    def __init__(self):
        self.prev = 0
        self.curr = 1

    def __iter__(self):
        return self

    def __next__(self):
        value = self.curr
        self.curr += self.prev
        self.prev = value
        return value

f = fib()
list1 = list(islice(f, 0, 10))
print(list1)