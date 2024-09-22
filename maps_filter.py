x = [12,55,5,225,551,525,1,51,5,5,5,5,5,23,32,3]

mp = map(lambda i : i +2, x)
print(list(mp))

fil = filter(lambda i : i % 2 == 0, x)
print(list(fil))