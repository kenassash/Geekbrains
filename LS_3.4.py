def thesaurus(*args):
    result = dict()
    for name in args:
        key = name[0].capitalize()
        if key not in result:
            result[key] = []
        result[key].append(name)
    return result


def thesaurus_adv(*args):
    result = dict()
    for name in args:
        result.setdefault(name.split()[1][:1], []).append(name)
    for key, values in result.items():
        result[key] = thesaurus(*values)
    return result


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
