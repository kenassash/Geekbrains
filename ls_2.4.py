my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for el in my_list:
    name = el.split()[-1].title()
    print(f'Привет, {name}!')