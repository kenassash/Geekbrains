def type_logger(func):
    def wrapper(*args):
        my_list = []
        for num in args:
            if num > 0:
                answer = func(num)
                my_list.append(f'{func.__name__}({num}: {type(num)}) = {answer}')
            else:
                raise ValueError(f'wrong val {num}')
        return '\n'.join(my_list)

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


if __name__ == '__main__':

    print(calc_cube(3, 5, 7))
    print(calc_cube(-5))
