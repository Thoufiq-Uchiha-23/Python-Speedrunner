def func(x):
    def func2():
        print(x)
    
    return func2

print(func(3)())

def func(*args, **kwargs):
    pass

x = [1, 23, 236363, 2727]
print(x)
print(*x)