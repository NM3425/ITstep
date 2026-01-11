from operator import index

import requests
from bs4 import BeautifulSoup as bs


class CoinMarketCap:
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
        else:
            print("Не вдалося підключитися до сайту")

    def getinfo(self):
        coins = []
        table = self.soup.find('tbody')
        if not table:
            print('Не знайдено таблицю')
            return

        rows = table.find_all('tr')[:10]

        for row in rows:
            # Назва монети
            name = row.find('p', class_='coin-item-name')
            nameCoin = name.text if name else 'Назва відсутня'

            # Ціна монети
            price = row.find('div', class_='eAphWs')
            priceCoin = price.text if price else 'Ціна відсутня'

            # Circulating Supply (ЯК ТИ ПРОСИВ)
            CirculatingSupply = row.find(
                "div", class_="circulating-supply-value"
            )
            cirs = (
                CirculatingSupply.text
                if CirculatingSupply
                else 'Відсутнє значення'
            )

            coins.append({
                'name': nameCoin,
                'price': priceCoin,
                'supply': cirs
            })

        return coins

    def showinfo(self, coins):
        print('\033[34mТоп 10 популярних криптомонет\033[0m')
        index = 1
        for coin in coins:
            print(f"#{index}")
            print("Назва:", coin['name'])
            print("Ціна:", coin['price'])
            print("Circulating Supply:", coin['supply'])
            print('-' * 40)
            index += 1


url = "https://coinmarketcap.com/"
obj = CoinMarketCap(url)
obj.auditSite()
site = obj.getinfo()

if site:
    obj.showinfo(site)
    bitcoin = site[0]['price']
    bit=float(bitcoin.replace('$', '.').replace(',', '.'))
    print('\nЦіна Bitcoin x2=',bit,'=',bit*2,'$')

else:
    print("Немає інформації")


#import requests #запит по HTTP

#from bs4 import BeautifulSoup as bs #робота з HTML




#class Name:
   # def __init__(self, url):
     #   self.url = url
      #  self.headers = {
     #       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
      #   }
      #  self.soup = None
  #  def AuditSite(self): #завантаження сайту на спробу парсенга
       # response = requests.get(self.url, headers=self.headers)#видправка GET запыту
 #       if response.status_code == 200:
  #          self.soup = bs(response.text, 'html.parser')
  #      else:
  #          print("Не вдалося падключится на сайт " )

  #  def getinfo(self):#отвечает за парсинг даных(зчитание нужной инф)
   #     pass

    #def showinfo(self):
       #pass

#url = "Сылка на сайт"
#obj = Name(url)
#obj.auditSite()
#site= obj.getinfo()
#if site==True :obj.showinfo()

#else:print("Не какой информацыи нету с сайта")
