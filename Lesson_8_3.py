def type_logger(func):
    def wrapper(*args):
        my_list = []
        for num in args:
            answer = func(*args)
            my_list.append(f'{func.__name__}({num}: {type(num)}) = {answer}')
        return '\n'.join(my_list)

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


if __name__ == '__main__':
    print(calc_cube(5))
