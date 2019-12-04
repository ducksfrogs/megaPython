days = ['Mon', "Tue", 'Wed']
friuts = ['apple', 'banana', 'Mango']

drinks = ['coffee', 'tea', 'beer']

# for i in range(len(days)):
#     print(days[i], friut[i], drinks[i])

for day, friut, drink in zip(days, friuts, drinks):
    print(day, friut, drink)

d = {'x':100, 'y':200}

for k, v in d.items():
    print(k,':'v)

print(d.items())
