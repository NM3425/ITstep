class Car:
    def __init__(self, brand):
        self.brand = brand
        self.speed = 0

    def accelerate(self, amount):
        self.speed = self.speed + amount
        print("Швидкість збільшилась на", amount)

    def brake(self, amount):
        self.speed = self.speed - amount
        if self.speed < 0:
            self.speed = 0
        print("Швидкість зменшилась на", amount)

    def show_speed(self):
        print("Поточна швидкість:", self.speed)



car1 = Car("BMW")
car2 = Car("Audi")


car1.show_speed()
car1.accelerate(30)
car1.show_speed()
car1.brake(10)
car1.show_speed()

print("------")

car2.accelerate(50)
car2.brake(20)
car2.show_speed()