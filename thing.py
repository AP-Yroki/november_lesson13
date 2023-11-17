from dataclasses import dataclass, field, InitVar, make_dataclass
from typing import Any
from random import randrange

@dataclass
class Goods:
    current_uid = 0

    uid: int = field(init=False)
    price: Any
    weight: Any

    def __post_init__(self):
        print('Goods')
        Goods.current_uid += 1
        self.uid = Goods.current_uid


class GoodMeassureFactory:

    @staticmethod
    def get_init_meassure():
        return [0, 0, 0]


@dataclass
class Book(Goods):
    title: str
    author: str
    price: int
    weight: float
    meassure: list = field(default_factory=GoodMeassureFactory.get_init_meassure)

g = Goods(1200, 2.3)
print(g)
g1 = Goods(1200, 2.3)
print(g1)
b = Book(12253523, 2000, 2.5, 'Jokons', 'Bob')
print(b)


print(b)