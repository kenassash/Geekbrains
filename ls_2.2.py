my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

new_list = []
for el in my_list:
    if el.isnumeric(): # Находит в списке числа isnumeric()
        number = f'{int(el):02}' # Записываем ноль перед целым числом типа
        new_list.extend(['"', number, '"']) # Добавляем в список измененные объекты оптом
    elif ('+' or '-') in el:
        number = f'{el[0]}{int(el[-1]):02}'
        new_list.extend(['"', number, '"'])
    else:
        new_list.append(el)

print(new_list)
print(' '.join(new_list)) # Решение № 1

second_list = []
for el in my_list:
    if el.isnumeric():
        number = f'{int(el):02}'
        second_list.append(f'"{number}"')
    elif ('+' or '-') in el:
        number = f'{el[0]}{int(el[-1]):02}'
        second_list.extend(['"', number, '"'])
    else:
        second_list.append(el)

print(' '.join(second_list)) # Решение № 2