from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
jokes = int(input('Введите колличество шуток: '))


def get_jokes(number):
    """
    Функция печатает n шуток
    :param number: число шуток которое ввел пользователь
    :return:
    """
    joke_list = []

    for i in range(number):
        a = choice(nouns)
        b = choice(adverbs)
        c = choice(adjectives)
        element = f'{a}, {b}, {c}'
        joke_list.append(element)

    print(joke_list)
    return joke_list


get_jokes(jokes)
