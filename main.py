
# Task is swap two variables

# solution 1 
print('Solution 1')
a = 5
b = 10

temp = a
a = b
b = temp
print('a,b => ',a,b)


# soluton 2
print('Solution 2')
a = 12
b = 24

a,b = b,a
print('a,b',a,b)


# Solution 3
print('Solution 3')
a = 20
b = 40 

a = a + b
b = a - b
a = a - b
print('a,b',a,b)