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
        table = self.soup.find_all('tr', class_="sc-1x32wa2-4 dKDsVV")

        if not table:
            print("Не вдалося знайти таблицю валют")
            return currencies

        def clean_number(text):
            text = text.replace(',', '.').strip()
            text = text.split()[0]
            result = ""
            dot_used = False

            for ch in text:
                if ch.isdigit():
                    result += ch
                elif ch == '.' and not dot_used:
                    result += ch
                    dot_used = True
                else:
                    break

            return round(float(result), 2) if result else 0.0

        for row in table[1:6]:
            name_tag = row.find("a", class_="sc-1x32wa2-7 ciClTw")
            name = name_tag.text.strip() if name_tag else "?"

            tds = row.find_all("td")
            if len(tds) < 3:
                continue

            buy = clean_number(tds[1].text)
            sell = clean_number(tds[2].text)

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

if not obj.auditSite():
    exit()

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
