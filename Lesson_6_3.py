import json
from itertools import zip_longest

with open('users.csv', encoding='utf-8') as users:
    with open('hobby.csv', encoding='utf-8') as hobby:
        with open('result.json', 'w', encoding='utf-8') as result:
            lines = zip_longest(users, hobby)
            dict_line = {}
            for i in lines:
                dict_line.setdefault(str(i[0]).strip().replace(',', ' '), str(i[1]).strip())
            if 'None' in dict_line:
                exit(1)
            else:
                json.dump(dict_line, result, indent=1, ensure_ascii=False)
