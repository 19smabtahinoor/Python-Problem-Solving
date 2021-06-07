# Problem : We take a input of any year.Then we can say it's leapyear or not.

year = int(input("Enter a year: "))

if year%4 == 0:
    is_leapyear = year," is a leap year"
else:
    is_leapyear = year," is not a leap year"

print(is_leapyear)