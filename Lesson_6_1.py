with open('nginx_logs.txt', 'r', encoding='UTF-8') as file:
    data_line = []
    for line in file:
        item = line.split()
        data_line.append((item[0], item[5][1:], item[6]))
    print(*data_line[:20], sep='\n')
