import winsound # Windows Sounds -> Beep when done scraping
import time
import pandas as pd
import httplib2
import numpy as np
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def return_index(feature):
    return columns.index(feature)


# url of interest
url = "https://lalafo.kg/kyrgyzstan/kompyutery/noutbuki-i-netbuki"
base = "https://lalafo.kg"

#  all available features on lalago.kg for Laptops
columns = ['Состояние', 'Бренд', 'Модель', 'Процессор',
           'Оперативная память (ГБ)', 'Частота процессора',
           'Количество ядер', 'Диагональ (дюйм)',
           'Разрешение экрана', 'Тип матрицы',
           'Видеокарта', 'Тип', 'Назначение',
           'Накопитель', 'Объем накопителя',
           'ОС', 'Цвет',  'Емкость батареи', 'Доставка', 'Title', 'Link', 'Price']
df = pd.DataFrame(columns = columns)

# opens Chrome 
service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service=service)
# open the link 
driver.get(url)
# wait 5 seconds - so the pages fully loads 
time.sleep(5)

storage = np.empty(10000, dtype = 'object')
FROM = 0
TO = 2235 

try:
    for i in range(10000):
        #scroll down
        driver.execute_script(f"window.scrollTo({FROM}, {TO})")
        # fetch te HTML code
        html = driver.page_source
        # initialize the bs4 obejct 
        soup = BeautifulSoup(html, 'html.parser')

        main_container = soup.find('div', class_='virtual-scroll__container')
        c = 0
        for i in main_container.children:
            arr = np.empty(len(columns), dtype='object')
            http = httplib2.Http()
            outer = i.find('div', class_ = 'AdTileHorizontal')
            try:
                inner = outer.find('a', class_ = 'AdTileHorizontalTitle business')
                title = inner.contents[0]

                if title in storage or 'Скупка' in title:
                    continue
                else:
                    storage[c] = title
                    c += 1
                    
                    link = urljoin(base, inner['href'])
                    status, response = http.request(link)
                    bs = BeautifulSoup(response, 'lxml')
                    try:
                        for item in bs.findAll('ul')[1]:
                            feature = item.contents[0].contents[0].strip(':')
                            value = item.contents[1].contents[0]
                            arr[return_index(feature)] = value
                            
                        arr[return_index('Link')] = link
                        arr[return_index('Title')] = title
                        try:
                            arr[return_index('Price')] = outer.find('p', class_= 'AdTileHorizontalPrice').find('span').contents[0]
                        except AttributeError:
                            arr[return_index('Price')] = outer.find('p', class_= 'AdTileHorizontalPrice').contents[0]
                        
                        idx = len(df)
                        df.loc[idx] = arr
                    except:
                        continue
                    

            except AttributeError as e:
                inner = outer.find('a', class_ = 'AdTileHorizontalTitle')
                title = inner.contents[0]
                if title in storage:
                    continue
                else:
                    storage[c] = title
                    c += 1
                    
                    link = urljoin(base, inner['href'])
                    status, response = http.request(link)
                    bs = BeautifulSoup(response, 'lxml')

                    try:
                        for item in bs.findAll('ul')[1]:
                            feature = item.contents[0].contents[0].strip(':')
                            value = item.contents[1].contents[0]
                            arr[return_index(feature)] = value
                            
                        arr[return_index('Link')] = link
                        arr[return_index('Title')] = title
                        try:
                            arr[return_index('Price')] = outer.find('p', class_= 'AdTileHorizontalPrice').find('span').contents[0]
                        except AttributeError:
                            arr[return_index('Price')] = outer.find('p', class_= 'AdTileHorizontalPrice').contents[0]
                            
                        
                        idx = len(df)
                        df.loc[idx] = arr
                    except:
                        continue
        FROM  += 1000
        TO += 1000
except:
    pass
finally:
    df.to_csv('hope.csv', sep=',', index=False, encoding='utf-8-sig')
##    winsound.Beep(1000, 10000)
