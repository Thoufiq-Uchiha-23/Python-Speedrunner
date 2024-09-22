for i in range(10):
    print(i)

# range has 3 parameters start, stop, step
#  start from 1 then till 10 and step it by 2 values 
for i in range(1,10, 2):
    print(i)

# List looping

x = [3, 4,4,225,33,562,115]

for i in range(len(x)):
    print(x[i])
    
# enumerate gives index and elements
for i, element in enumerate(x):
    print(i , element)