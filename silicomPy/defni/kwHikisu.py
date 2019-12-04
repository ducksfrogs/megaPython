# def menu(**kwargs):
#     print(kwargs)
#     for k, v in kwargs.items():
#         print(k, v)

# d = {
#     'entree': 'beef',
#     'drinl': 'ice coffee',
#
# }

def memu(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)

memu('banana', 'apple', 'orange', entree='beef', drinl='beer')
