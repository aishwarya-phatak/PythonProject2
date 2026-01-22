
#control statements
#1
age = 34
if age >= 18:
    print('You are eligible to vote')

print("======================")
#2
number = 45
if number % 2 == 0:
    print("The number entered is even")
else:
    print("The number entered is odd")

print("======================")

#3
studentPercentage = 67.0

if (studentPercentage > 0.0) and (studentPercentage < 40.0):
    print("Student has failed")
elif (studentPercentage >= 40.0) and (studentPercentage < 55.0):
    print("Student has passed in Second class")
elif (studentPercentage >= 55.0) and (studentPercentage < 75.0):
    print("Student has passed in First class")
else:
    print("Student has passed in Distinction class")

print("======================")

#4 logical operators and , or used

num1 = 44
if (num1 % 3 == 0) and (num1 % 5 == 0):
    print("The number is divisible by 3 and 5")
elif (num1 % 3 == 0) or (num1 % 5 == 0):
    print("The number is divisible by 3 or 5")
else :
    print("The number is not divisible by 3 or 5")

#5 != operator
m = "Welcome"
if m != "Hello":
    print("m not equal to Hello")