class AirCastle:

    def __init__(self, height, count, color):
        self.height = height
        self.count = count
        self.color = color

    def change_height(self, value):
        if value >= 0:
            self.height = value

    def add_count(self, n):
        self.count += n
        self.height += n // 5

    def show_castle(self, value):
        result = self.height // value * self.count
        print(result)

    def __str__(self):
        print(f'The AirCastle at an altitude of {self.height} meters is {self.color} with {self.count} clouds')

    def __eq__(self, other):
        if not isinstance(other, AirCastle):
            raise TypeError('Неверный тип данных')

        return (self.count, self.height, self.color) == (other.count, other.height, other.color)

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if not isinstance(other, AirCastle):
            raise TypeError('Неверный тип данных')

        return (self.count, self.height, self.color) < (other.count, other.height, other.color)

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        if not isinstance(other, AirCastle):
            raise TypeError('Неверный тип данных')

        return (self.count, self.height, self.color) > (other.count, other.height, other.color)

    def __ge__(self, other):
        return self > other or self == other

cst1 = AirCastle(100, 20, 'Green')
cst2 = AirCastle(150, 5, 'Red')

cst1.change_height(80)
print(cst1.height)

cst2.add_count(10)
print(cst2.count)
print(cst2.height)

cst1.show_castle(10)

cst1.__str__()

print(cst1 > cst2)
print(cst1 < cst2)
print(cst1 == cst2)
print(cst1 != cst2)