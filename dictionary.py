x = {'key': 4}
print(x['key'])

del x['key']
print(x)
x[2] = [2,23,32,43,4]
print(x)

for key, value in x.items():
    print(key, value)