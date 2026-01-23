#while loop
#1

#increment and decrement operators are not supported in Python
i = 1
addAllElements = 0
while i <= 10:
    addAllElements = addAllElements + i
    i = i + 1
print("Addition of All elements : {}".format(addAllElements))

print("=================")

number = 984
rem = 0
while number > 0:
    rem = rem + number % 10
    number = number // 10           #integeral division -- floor the value
print(rem)

#printing all numbers between 1 - 10
#else suite example with while loop
print("=================")
num = 1
while num <= 10:
   print(num)
   num += 1
else:
    print("else suite part executed")

print("=================")

#printing eve numbers from the range 0 - 10
num = 0
while num <= 10:
   if num % 2 == 0:
       print( num , end = ' ')
   num += 1

print("-----------------")
#while ex
number = int(input("Enter a number: "))
i = 1
while i <= 10:
    print( i * number)
    i = i + 1