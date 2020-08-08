from dataclasses import dataclass


@dataclass
class Goat:
    age: int = 0
    name: str = ''
    weight: int = .0

    def show(self):
        print(f'Коза по имени: {self.name} в возрасте {self.age} и весом {self.weight}')


# a = Goat()
# print(a.age+a.weight)

b = Goat(2, 'Зорька')

b.show()

print(b.__dict__)
print(dir(b))
