from bs4 import BeautifulSoup
import requests

url = "https://bank.gov.ua/ua/markets/exchangerates"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')
    row_count = 0
    for row in table.find_all('tr'):
        row_count += 1
        if row_count == 9:
            cells = row.find_all('td')
            if cells:
                currency_name = cells[1].text.strip()
                currency_price = float(cells[4].text.strip().replace(',', '.'))
                print(f"1 {currency_name} Коштує {currency_price} Грн")
                amount_to_buy = float(input(f"Скілкьи Грн ви хочете перевести в {currency_name}? "))
                total_cost = amount_to_buy  / currency_price
                print(f"{amount_to_buy} Грн це {total_cost} {currency_name}.")