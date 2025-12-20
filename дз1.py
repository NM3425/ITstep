
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


    def get_info(self):
        print(self.year, self.make, self.model)



car1 = Car("Toyota", "Corolla", 2020)


car1.get_info()
