class Student:
    def __init__(self, name):
        self.name = name
        self.knowledge = 50
        self.health = 50
        self.money = 50

    def study(self):
        print("Студент вчиться")
        self.knowledge += 5
        self.health -= 2

    def work(self):
        print("Студент працює")
        self.money += 20
        self.health -= 5

    def rest(self):
        print("Студент відпочиває")
        self.health += 5
        self.money -= 10

    def day(self):
        if self.money < 20:
            self.work()
        elif self.knowledge < 40:
            self.study()
        else:
            self.rest()

        print("Знання:", self.knowledge)
        print("Здоров'я:", self.health)
        print("Гроші:", self.money)
        print("------")


student = Student("Андрій")

for d in range(1, 366):
    print("День", d)
    student.day()

print("Студент прожив рік!")