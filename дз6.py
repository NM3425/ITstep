
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("Ім'я:", self.name)
        print("Вік:", self.age)



class Dog(Animal):
    def bark(self):
        print(self.name, "каже: Гав-гав!")



class Cat(Animal):
    def meow(self):
        print(self.name, "каже: Мяу!")



dog = Dog("Бобік", 3)
cat = Cat("Мурчик", 2)


dog.info()
dog.bark()

print()

cat.info()
cat.meow()