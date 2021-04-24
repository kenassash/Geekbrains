def num_translate(number):
    result = {'one': 'один',
              'two': 'два',
              'three': 'три',
              'four': 'четыре',
              'five': 'пять',
              'six': 'шесть',
              'seven': 'семь',
              'eight': 'восемь',
              'nine': 'девять',
              'ten': 'десять',
              }

    for i in number:
        if not i.islower():
            return print(result.get(number.lower()).capitalize())
        else:
            return print(result.get(number))


num_translate(input('Введите число на англ. языке: '))
