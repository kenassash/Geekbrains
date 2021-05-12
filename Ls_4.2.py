from requests import get

response = get('http://www.cbr.ru/scripts/XML_daily.asp')
content = response.content.decode(encoding='UTF-8', errors='ignore').split('<Valute ID=')


def currency_rates(code):
    for i in content:
        if code.upper() in i:
            return float(i.replace('/', '').split('<Value>')[-2].replace(',', '.'))


if __name__ == '__main__':
    print(currency_rates('eur'))
    print(currency_rates('Usd'))
    print(currency_rates('RuB'))
