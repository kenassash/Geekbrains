my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for index, el in enumerate(my_list):
    if el.isnumeric():
        number = f'{int(el):02}'
        my_list.remove(el)
        my_list.insert(index, f'"{int(el):02}"')
    elif ('+' or '-') in el:
         number = f'{el[0]}{int(el[-1]):02}'
         my_list.remove(el)
         my_list.insert(index, f'"{el[0]}{int(el[-1]):02}"')

print(my_list)
print(' '.join(my_list))