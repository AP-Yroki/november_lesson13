class GoodIfrit:
    def __init__(self, height, name, goodness):
        self.height = height
        self.name = name
        self.goodness = goodness

    def change_goodness(self, value):
        if value >= 0:
            self.goodness += value
        else:
            self.goodness = 0

    def __add__(self, other):
        if other < 0:
            raise ValueError('Число отрицательное')

        new_ifrit = GoodIfrit(self.height + other, self.name, self.goodness)
        return new_ifrit

    def __call__(self, argument):
        return argument * self.goodness // self.height

    def __str__(self):
        return f'Good Ifrit {self.name}, height {self.height}, goodness {self.goodness}'

    def __eq__(self, other):
        if not isinstance(other, GoodIfrit):
            raise TypeError('Неверный тип данных')

        return (self.goodness, self.height, self.name) == (other.goodness, other.height, other.name)

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if not isinstance(other, GoodIfrit):
            raise TypeError('Неверный тип данных')

        return (self.goodness, self.height, self.name) < (other.goodness, other.height, other.name)

    def __gt__(self, other):
        if not isinstance(other, GoodIfrit):
            raise TypeError('Неверный тип данных')

        return (self.goodness, self.height, self.name) > (other.goodness, other.height, other.name)

    def __le__(self, other):
        return self < other or self == other

    def __ge__(self, other):
        return self > other or self == other



gi = GoodIfrit(80, "Hazrul", 3)
gi.change_goodness(4)
print(gi)
gi1 = gi + 15
print(gi1)
print(gi(31))

gi = GoodIfrit(80, "Hazrul", 3)
gi1 = GoodIfrit(80, "Dalziel", 1)
print(gi < gi1)
gi1.change_goodness(2)
print(gi > gi1)
print(gi, gi1, sep='\n')

