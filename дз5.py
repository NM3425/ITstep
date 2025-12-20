
class Product:
    def __init__(self, name, price, quantity):
        self.name = name       # назва товару
        self.price = price     # ціна товару
        self.quantity = quantity  # кількість на складі

    def __str__(self):
        return self.name + " - " + str(self.price) + " грн, в наявності: " + str(self.quantity)



class Cart:
    def __init__(self):
        self.items = []  # список товарів у кошику


    def add_product(self, product, amount):
        if product.quantity >= amount:
            self.items.append((product, amount))
            product.quantity -= amount
            print(product.name + " додано у кошик (" + str(amount) + " шт.)")
        else:
            print("На жаль, " + product.name + " немає в потрібній кількості.")


    def remove_product(self, product_name):
        for item in self.items:
            if item[0].name == product_name:
                item[0].quantity += item[1]  # повертаємо товар на склад
                self.items.remove(item)
                print(product_name + " видалено з кошика")
                return
        print(product_name + " не знайдено в кошику")


    def total_price(self):
        total = 0
        for item in self.items:
            total += item[0].price * item[1]
        return total


    def show_cart(self):
        if not self.items:
            print("Кошик порожній")
        else:
            print("Товари у кошику:")
            for item in self.items:
                print(item[0].name + " - " + str(item[1]) + " шт. по " + str(item[0].price) + " грн")
            print("Загальна вартість: " + str(self.total_price()) + " грн")



p1 = Product("Молоко", 30, 10)
p2 = Product("Хліб", 20, 5)

cart = Cart()
cart.add_product(p1, 2)
cart.add_product(p2, 1)
cart.show_cart()

cart.remove_product("Молоко")
cart.show_cart()