price = [57.8, 46.51, 97, 101,5, 23, 1.32, 87, 65.65, 66, 35, 345.54, 554.35]
price.sort()
print(f'price ID: {id(price)}') # Задание "А". Сортирую сразу что бы потом не усложнять

price_list = []
for i in price:
    number = str(i).split('.')
    rub = number[0]

    if len(number) == 2:
        cent = number[1]
    else:
        cent = '00'

    if len(cent) == 1:
        cent = f'{cent}0'

    price_list.append(f'{rub} руб {cent} коп')

print(', '.join(price_list)) # Сотрировка по возрастанию
print(', '.join(price_list[::-1])) # Сортировка по убыванию
print(', '.join(price_list[-5:])) # Цены пяти самых дорогих товаров