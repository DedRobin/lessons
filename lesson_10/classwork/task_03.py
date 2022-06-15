"""
Пользователь вводит два числа N и M, рассчитать последовательность  N + NN + NNN + ... + N x M.
"""


class Progression:
    def __init__(self, symbol: str, counter: int):
        self.symbol = symbol
        self.counter = counter

    def __iter__(self):
        self.current_value = self.symbol
        return self

    def __next__(self):
        previuos_value = self.current_value
        if len(self.current_value) <= self.counter:
            self.current_value += self.symbol
            return previuos_value
        else:
            raise StopIteration


if __name__ == '__main__':
    iterator = Progression(symbol="a", counter=10)
    for item in iterator:
        print(item)