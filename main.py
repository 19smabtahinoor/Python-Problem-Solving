
# Solution 1
num1 = input("1st number : ")
num2 = input("2nd number : ")
num3 = input("3rd number : ")

if(num1 >= num2 and num1 >= num3):
  print("Highest Value is:", num1)
elif(num2 >= num1 and num2 >= num3):
  print("Hightest Value is: ",num2)
else:
  print("Highest Value is: ",num3)


# Solution 2
num1 = input("1st number : ")
num2 = input("2nd number : ")
num3 = input("3rd number :")

print("Highest Value is: ",max(num1,num2,num3))