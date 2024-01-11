from bs4 import BeautifulSoup
from selenium import webdriver

url = 'https://bossa.pl/notowania/indeksy-swiatowe'

driver = webdriver.Chrome()
driver.get(url)

html_text = driver.page_source

driver.quit()
soup = BeautifulSoup(html_text, 'lxml')
all_index = soup.find_all('tr', class_='b30-quotations--single-instrument')

for index in all_index:
    name = index.find('td', class_='b30fx-quotations--symbol').text.split(' ')[0].strip().replace('.', '')
    low_price = index.find('td', class_='d-none d-sm-table-cell text-right b30-quotations--low').text
    high_price = index.find('td', class_='d-none d-sm-table-cell text-right b30-quotations--high').text
    print(f'{name} low price: {low_price} high_price: {high_price}')
