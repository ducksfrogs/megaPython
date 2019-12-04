def test_funk(x, l=None):
    if l is None:
        l = []
    l.append(x)

y = [1,2,3]
r = test_funk(100,y)
print(r)
