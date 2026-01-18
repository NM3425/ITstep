import requests
from bs4 import BeautifulSoup as bs


class MinfinCurrency:
    def __init__(self, url):
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        }
        self.soup = None

    def auditSite(self):
        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 200:
            self.soup = bs(response.text, 'html.parser')
            return True
        else:
            print("Не вдалося підключитися до сайту")
            return False

    def getinfo(self):
        currencies = []
        blocks = self.soup.find_all("div", class_="currency-rate")[:5]

        for block in blocks:
            name = block.find("a").text.strip()
            print(name)
            buy = block.find("span", class_="buy").text.strip()
            sell = block.find("span", class_="sell").text.strip()

            buy = float(buy.replace(",", "."))
            sell = float(sell.replace(",", "."))

            currencies.append({
                "name": name,
                "buy": buy,
                "sell": sell
            })

        return currencies

    def showinfo(self, currencies):
        print("\nКурси 5 найпопулярніших валют:\n")
        for i, cur in enumerate(currencies, 1):
            print(f"{i}. {cur['name']}")
            print(f"   Купити: {cur['buy']} грн")
            print(f"   Продати: {cur['sell']} грн")
            print("-" * 30)



url = "https://minfin.com.ua/ua/currency/"
obj = MinfinCurrency(url)

obj.auditSite()
currencies = obj.getinfo()

if not currencies:
    print("Немає даних")
    exit()

obj.showinfo(currencies)


print("\nЩо ви хочете зробити?")
print("1 - Купити валюту")
print("2 - Продати валюту")
action = input("> ")


print("\nВиберіть валюту (1-5):")
choice = int(input("> ")) - 1
currency = currencies[choice]


amount = float(input("\nВведіть суму (1000 - 10000 грн):\n> "))

if amount < 1000 or amount > 10000:
    print("Сума має бути від 1000 до 10000 грн")
    exit()


if action == "1":
    result = amount / currency["sell"]
    print(f"\nВи хочете КУПИТИ {currency['name']}")
    print(f"Сума: {amount} грн")
    print(f"Ви отримаєте: {result:.2f} {currency['name']}")
elif action == "2":
    result = amount / currency["buy"]
    print(f"\nВи хочете ПРОДАТИ {currency['name']}")
    print(f"Сума: {amount} грн")
    print(f"Ви отримаєте: {result:.2f} {currency['name']}")
else:
    print("Невірний вибір")
    exit()


confirm = input("\nПідтвердити операцію? (так / ні): ").lower()

if confirm == "так":
    print("✅ Операцію виконано успішно")
else:
    print("❌ Операцію скасовано")
