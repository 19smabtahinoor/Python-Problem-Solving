
salary = 5002 
vacation = 50

if salary > 500 and vacation > 40:
  print("I will do the job")
else:
  print("I will not to do thid job")

a = 5 
b= 7 
c = b = a + b
print(b)

x = 5
y = 7
z = (x + y) * (x -y)
print(z)


x = [3,7,5,9]
y = [2,4,8,7]
z = x[1] + y[2]
print(z)


# array index
friends = ["Batman","Catman","Fatman"]
print(friends)
print("Catman's index Number is : ",friends.index('Catman'))

# rewrite the array value
friends[2] = "PilotMan"
print("Updateed Array => ",friends)

# add to array
friends.append("Goat Men")
print("Updateed Array => ",friends)

# length
print(len(friends))

# remove from array
friends.remove("PilotMan")
print(friends)

# max operation and min operation
friends_number = [12,324,434,55,32,-6]

print("Maximum Value is:",max(friends_number))
print("Minimum Value is:",min(friends_number))

# is in the array
print("Fatman" in friends)

# pop
nums = [1,2,43,3464,757]
print(nums.pop()) #it gives last item of the array.

# =================================
# loop 

# basket = ["Apple","Orange","Strawberry","Banana"]
# for fruits in basket:
#   print(fruits)


# exploring with loop
bags = ["Apple","Orange","Strawberry","Banana","Mango"]

for bag_Fruit in bags:
  if len(bag_Fruit) > 5:
    print(bag_Fruit)

# break keyword
numbers = [12, 30, 40, -20, 34, 40,6]
for number in numbers:
  if number < 0:
    break
  print(number)


# Continue keyword
print('Continue KEyword ==================')
for number in numbers:
  if number < 0:
    continue
  print(number)

# while loop
print('While loop ==================')

count = 1 
while count <= 5:
  print(count)
  count = count + 1


# total fo 1 - 10
i = 1
sum = 0 
while i <= 10:
  sum = sum + i 
  i = i + 1
print(sum)

# namta
count = 1
num = int(input("Write a Number "))
while count < 10:
  product = num * count
  print(num , " X " ,count , " = " ,product)
  count = count + 1
  

# even number total
i = 1
sum =0 
while i <= 10:
  if i%2 == 0:
    sum = sum + i
  i = i + 1

print("The toal of the even numbers ",sum)

# odd numbers total
i = 1
sum = 0
while i <= 50:
  if i%2 !=0:
    sum = sum + i
  i = i + 1

print("The odd numbers total ",sum)



# get odd numbers
i = 0
while i < 10:
  i = i + 1
  if i%2 == 0:
      continue
  print(i)
      


# function with parameters

def number(a ,b ):
  res = a * b
  print("The multiplication is ",res)

number(7,9)


# return 
def get_expense(tution,rent):
  total = tution + rent
  return total

print("The total expense is ",get_expense(100,4400))

