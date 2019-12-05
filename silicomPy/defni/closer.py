# def outer(a, b):
#
#     def inner():
#         return a + b
#
#     return inner
#
# print(outer(1, 2))
#
# f = outer(1, 2)
# r = f()
# print(r)

def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius ** 2

    return circle_area

ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.14152)

r = ca1(10)
print(r)

r = ca2(10)
print(r)
