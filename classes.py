class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print("move")
    
    def draw(self):
        print("draw")

p = Point(10, 20)
print(p.x)
print(p.y)
p.draw()
p.move()

class Person:
    def __init__(self, name):
        self._name = name
    def talk(self):
        print(f"Hi, I am {self._name}")

person = Person("Abbas Mehrabi")
person.talk()

# Inharitance
class Mammal:
    def walk(self):
        print("Walk")

class Dog(Mammal):
    def bark(self):
        print("Bark")

class Cat(Mammal):
    def meow(self):
        print("meow")

dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 = Cat()
cat1.walk()
cat1.meow()