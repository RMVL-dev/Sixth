class Animal:

    alive = True
    fed = False

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if isinstance(food, Plant) and food.editable:
            self.fed = True
            print(f"{self.name} съел {food.name}")
        elif isinstance(food, Plant) and not food.editable:
            self.alive = False
            print(f"{self.name} не стал есть {food.name}")
        else:
            print(f"{food} не растение")


class Plant:

    editable = False

    def __init__(self, name):
        self.name = name


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Flower(Plant):
    pass


class Fruit(Plant):

    def __init__(self, name):
        super().__init__(name)
        self.editable = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

