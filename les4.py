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



import requests #запит по HTTP

from bs4 import BeautifulSoup as bs #робота з HTML

class AutoRia:
    def __init__(self, url):
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
         }
        self.soup = None
    def AuditSite(self): #завантаження сайту на спробу парсенга
        response = requests.get(self.url, headers=self.headers)#видправка GET запыту
        if response.status_code == 200:
          self.soup = bs(response.text, 'html.parser')
        else:
           print("Не вдалося падключится на сайт " )

    def getinfo(self):#отвечает за парсинг даных(зчитание нужной инф)
        soup = self.AuditSite()#палучаем HTML сторинку
        if not soup:return #если страница не открылась
        teg=soup.find_all("section", class_="proposition")
        for k in teg:
            name = k.find("h3", class_="proposition_name")
            link = k.find("a", class_="proposition_url")
            priceUSD = k.find("span", class_="size20 tooltip-price")
            priceGRN =k.find("span", class_="size16")
            city = k.find("span", class_="region")
            if priceUSD:
                num=int(''. join(i for i in priceUSD.get_text() if i.digit()))#з рядка берем только 🔥 77 666 $
            else:
                num=0# если цена не указана
            self.car.append({
                "Название":name.get_text() if name else "Названия нету ",
                "Сылка":link.get_text() if link else "Сылки нету",
                "Сколько стоит в гривнах":priceGRN.get_text() if priceGRN else "Цена в $",
                "Сколько стоит в доларах":priceUSD.get_text() if priceGRN else "Цена в ₴",
                "город":city.get_text() if city else "Не указан горад ",
                "число":num


            })

    def sortPrice(self,limit=5):
        self.car.sort(key=lambda x:x["число"],reverse=True)
        self.car=self.car[:limit]#сразки с списка от 0 до 5


    def showinfo(self):
        if not self.car:
            print("Даные по афто не найдины")
            return
        print("Топ 5 най дороших джыпав в Украини\n")
        for ind,i in enumerate(self.car,start=1):

            print(ind,i["Название"])
            print("Город", i['Город'])
            print("Цена $", i['Цена $'])
            print("Цена ₴", i['Город ₴'])
            print("Сылка", i['Сылка'])
            print('='*30)



url = 'https://auto.ria.com/uk/newauto/marka-jeep/'
obj = AutoRia(url)
obj.AuditSite()   # ← правильний виклик методу
AuditSite = obj.getinfo()

if AuditSite == True:
    obj.sortPrice(5)
    obj.showinfo()
else:
    print("Ніякої інформації немає з сайту")
