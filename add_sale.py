from sys import argv

if len(argv) == 2:
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        f.writelines(f'{argv[1]}\n')
else:
    print('Неверно')
