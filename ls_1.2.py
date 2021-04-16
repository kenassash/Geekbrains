

# Создать список, состоящий из кубов нечётных чисел от 1 до 1000:

number = []
for i in range(1,1001, 2):
    number.append(i**3)
print('Список из кубов нечетных чисел \n', number)
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
sum_div_7 = 0
i = 0   # счетчик
for element in number:
    sum_dig = 0
    while element > 0:  #перебираем каждый элемент из созданного списка и находим его сумму цифр
        sum_dig += element % 10
        element = element // 10
    if sum_dig % 7 ==0:     # если сумма цифр каждого элемента делится нацело на 7
        sum_div_7 += number[i] # вычисление суммы
    i += 1

print('Сумма цифр которые делятся нацело на 7: ', sum_div_7, '\n')

#Список из кубов нечетных чисел +17

i = 0
for element in number:
    number[i] = element + 17
    i += 1
print('Список из кубов нечетных чисел +17\n',number)

sum_div_17 = 0
i = 0   # счетчик
for element in number:
    sum_dig = 0
    while element > 0:
        sum_dig += element % 10
        element = element // 10
    if sum_dig % 7 ==0:
        sum_div_17 += number[i]
    i += 1
print('Cумма из кубов нечетных чисел +17 ',sum_div_17, '\n')

#Решить задачу под пунктом b, не создавая новый список.

sum = 0
for number in range(1, 1000, 2):
    number = number**3 +17
    sum_dig = 0
    element = number
    while element > 0:
        sum_dig += element % 10
        element //= 10
    if sum_dig % 7 ==0:
        sum += number

print(sum)