# collections - it's a unordered or ordered group of elements
#  Mainly used are List and Tuples
# Lists - []
x = [4, True, 'hi']
y = 'hi'

# print(len(x), len(y))
# we can also add in new elements in the list
# append adds elements at the last pos of the list
x.append("hello")
# extend adds the set or collection of elements at the end of the list
x.extend([4, 5,5,5,5,])
print(x)
# pop removes the one element of the list either from the last pos or from the index pos which we specify
# x.pop()
x.pop(1)
print(x)