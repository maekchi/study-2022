import requests
from bs4 import BeautifulSoup

from openpyxl import Workbook

url = 'https://finance.naver.com/sise/sise_market_sum.naver'

response = requests.get(url)
response.raise_for_status()
html = response.text
soup = BeautifulSoup(html, 'html.parser')
body = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody')
tds = body.select('tr:nth-child(2)')
datas = []
for td in tds:
    name = td.select_one('td > a').get_text()
    price = td.select_one('tr:nth-child(2) > td:nth-child(3)').get_text()
    datas.append([name, price])

write_wb = Workbook()
write_ws = write_wb.create_sheet('결과')
for data in datas:
    write_ws.append(data)

write_wb.save("C:/Users/hyeji/study-2022/크롤링.xlsx")

