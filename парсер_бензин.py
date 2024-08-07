import requests
from bs4 import BeautifulSoup
import fake_useragent
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = 'https://mimobaka.ru/novosibirskaya-oblast/?key=&price=&fuel_type8=1' # бензин


ua = fake_useragent.UserAgent()

headers = {
    "User-Agent": ua.random,
    'Accept': '*/*'
}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'lxml')

list = []
table = soup.find('table')
for row in table.find_all('tr'):
    for cell in row.find_all('td'):
        list.append(cell.text.strip().replace('\n', ' '))
df = pd.DataFrame({'Price': list})
df.to_csv('prices.csv', index=False)

# Импортируем данные из Csv и визуализируем их
df = pd.read_csv('prices.csv')
plt.figure(figsize=(18, 4))
sns.histplot(data=df, x='Price', kde=True, shrink=3)
plt.title('Распределение цен на бензин')
plt.xlabel('Цена')
plt.ylabel('Количество')
plt.show()