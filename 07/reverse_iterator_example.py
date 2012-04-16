if 1:
    class Reverse:
        """Iterator for looping over a sequence backwards."""
        def __init__(self, data):
            self.data = data
            self.index = len(data)
        def __iter__(self):
            return self
        def next(self):
            if self.index == 0:
                raise StopIteration
            self.index = self.index - 1
            return self.data[self.index]

    a = [1, 2, 3, 4, 5]
    print [i for i in Reverse(a)]
