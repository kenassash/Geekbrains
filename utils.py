from requests import get
from datetime import date

response = get('http://www.cbr.ru/scripts/XML_daily.asp')
content = response.content.decode(encoding='UTF-8', errors='ignore').split('<Valute ID=')
d, m, y = content[0].split()[3].split('Date=')[1][1:-1].split('.')


def currency_rates(code):
    for i in content:
        if code.upper() in i:
            print(date(year=int(y), month=int(m), day=int(d)), end=', ')
            return float(i.replace('/', '').split('<Value>')[-2].replace(',', '.'))


if __name__ == '__main__':
    print(currency_rates('eur'))
    print(currency_rates('Usd'))
    print(currency_rates('RuB'))
