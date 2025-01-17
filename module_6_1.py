class Animal: # Родитель, дочи Mammal и Predator
    alive = True # живой
    fed = False # накормленный

    def __init__(self, name): # Иниц животных
        self.name = name

    def eat(self, food):  # Метод eat в родительском классе
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Plant: # Родитель, дочи Flower и Fruit
    edible = False # Съедобность
    def __init__(self, name): # Иниц раст
        self.name = name

class Mammal(Animal): # Млекопитающие Дочь Animal
    pass # Наследуем eat

class Predator(Animal): # Хищник Тоже дочь Animal
    pass # Тоже наследуем

class Flower(Plant): # Дочь Plant
    pass

class Fruit(Plant): # Тоже дочь Plant
    edible = True

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

