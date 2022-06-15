"""
Создать итератор простой геометрической прогрессии.
"""


class GeometricProgression:
    def __init__(self, power: int, limit: int):
        self.power = power
        self.limit = limit

    def __iter__(self):
        self.current_value = 1
        return self

    def __next__(self):
        previuos_value = self.current_value
        if self.current_value <= self.limit:
            self.current_value *= self.power
            return previuos_value
        else:
            raise StopIteration


if __name__ == '__main__':
    iterator = GeometricProgression(power=2, limit=16)
    for item in iterator:
        print(item)
