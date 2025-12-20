class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_salary_info(self):
        print("Ім'я:", self.name)
        print("Посада:", self.position)
        print("Заробітна плата:", self.salary)


employee = Employee("Олена", "Менеджер", 20000)
employee.get_salary_info()