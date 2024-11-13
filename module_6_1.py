class Animal:
    alive = True  # живой
    fed = False  # накормленный

    def __init__(self, name):
        self.name = name


class Plant:
    edible = False  # съедобность

    def __init__(self, name):
        self.name = name


class Mammal(Animal):
    def eat(self, food):
        if type(food) == Fruit:
            print(f'{self.name} сьел {food.name}')
            fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            alive = False


class Predator(Animal):
    def eat(self, food):
        if type(food) == Fruit:
            fed = True
            print(f'{self.name} сьел {food.name}')

        else:
            print(f'{self.name} не стал есть {food.name}')
            alive = False


class Fruit(Plant):
    edible = True


class Flower(Plant):
    pass


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
