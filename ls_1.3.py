#Реализовать склонение слова «процент» для чисел до 20.
perecent = int(input("Введите колличество процентов до 20:  "))

if perecent == 1:
    print(f'{perecent} процент')
elif perecent == 2 or perecent == 3 or perecent == 4:
    print(f'{perecent} процента')
else:
    print(f'{perecent} процентов')