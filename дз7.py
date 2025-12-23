
class TransportnyZasib:
    def __init__(self, speed):
        self.speed = speed

    def peremishchennia(self):
        print("Транспорт рухається зі швидкістю", self.speed, "км/год")



class Avto(TransportnyZasib):
    def drive(self):
        print("Автомобіль їде")



class Velysyped(TransportnyZasib):
    def ride(self):
        print("Велосипед їде")



class Poizd(TransportnyZasib):
    def move(self):
        print("Поїзд рухається")



car = Avto(80)
bike = Velysyped(20)
train = Poizd(120)


car.peremishchennia()
car.drive()

bike.peremishchennia()
bike.ride()

train.peremishchennia()
train.move()