def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
    return wrapper

@print_info
def add_num(a, b):
    return a + b

# f = print_info(add_num)


r = add_num(20, 10)
print(r)
