class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"My name is {self.name} and I am  {self.age} years old.")

    def speak(self):
        print("I don't know what I say.")

class Cat(Pet):
    def __init__(self,name, age, color):
        super().__init__(name, age)
        self.color = color
    def speak(self):
        print("Meow")
    def show(self):
        print(f"My name is {self.name} and I am  {self.age} years old and I am {self.color}")

class Dog(Pet):
    def speak(self):
        print("Woof!")

pet = Pet("Tim", 18)
pet.show()
pet.speak()
cat = Cat("Bill", 17, "Brown")
cat.show()
cat.speak()
dog = Dog("Jill", 25)
dog.show()
dog.speak()