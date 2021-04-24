def thesaurus(*args):
    result = dict()
    for name in args:
        key = name[0].capitalize()
        if key not in result:
            result[key] = []
        result[key].append(name)
    return result


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
