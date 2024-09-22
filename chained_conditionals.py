""" chained conditionals - combining multiple conditions together to create one large condition """
x = 7
y = 8
z = 0

result1 = x == y
result2 = y > x
result3 = z < x + 2

result4 = result1 or result2
print(result4)

# Evaluation order of logical operators are not --> and --> or