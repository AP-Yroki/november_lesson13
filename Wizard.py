
class Wizard:

    def __init__(self, name, rating, age):
        self.name = name
        self.rating = rating
        self.age = age

    def change_rating(self, value):
        if value > 0:
            self.rating = min(100, value)
            self.age -= max(18, abs(value) // 10)
        elif value < 0:
            self.rating = max(1, self.rating + value)
            self.age += max(18, abs(value) // 10)

    def __add__(self, other):
        length = len(other)
        self.rating += length
        self.age -= length // 10
        return self

    def __call__(self, other):
        return (other - self.age) * self.rating

    def __str__(self):
        return (f'Wizard {self.name} with {self.rating} rating looks {self.age} years old')

    def __eq__(self, other):
        if not isinstance(other, Wizard):
            raise TypeError('Неверный тип данных')

        return (self.rating, self.age, self.name) == (other.rating, other.age, other.name)

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if not isinstance(other, Wizard):
            raise TypeError('Неверный тип данных')

        return (self.rating, self.age, self.name) < (other.rating, other.age, other.name)

    def __gt__(self, other):
        if not isinstance(other, Wizard):
            raise TypeError('Неверный тип данных')

        return (self.rating, self.age, self.name) > (other.rating, other.age, other.name)

    def __le__(self, other):
        return self < other or self == other

    def __ge__(self, other):
        return self > other or self == other

wiz = Wizard('Bobfild', 90, 50)
print(wiz)
wiz.change_rating(10)
print(wiz)
wiz.change_rating(-30)
print(wiz)
result = wiz(60)
print(result)