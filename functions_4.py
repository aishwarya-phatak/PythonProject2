
def add1(num1, num2):
    return num1 + num2

def subtract1(num1, num2):
    return num1 - num2
#positional arguments - order/sequence of the arguments is important
numberOne = 10
numberTwo = 13

resultAdd = add1(numberOne, numberTwo)
print(resultAdd)

resultSub = subtract1(numberOne,numberTwo)
print(resultSub)

resultSub1 = subtract1(numberTwo,numberOne)
print(resultSub1)

#keyword arguments
def batchDetails(batchId,batchName,batchCount):
    print("batchId : {} batchName : {} batchCount : {}".format(batchId,batchName,batchCount))

batchDetails(batchId=23451,batchName="AI_Jan_26",batchCount=5)
batchDetails(batchName="iOS_Dec_25",batchCount=5,batchId=67453)


#default arguments
def add2(num1, num2 = 23, num3 = 56):
    return num1 + num2 + num3

res1 = add2(11,27,34)
print(res1)
res2 = add2(19,24)
print(res2)
res3 = add2(100)
print(res3)

#variable number of positional arguments
def sumOfNumbers(*numbers):
    return sum(numbers)

print(sumOfNumbers(1,2,3,4,5))
print(sumOfNumbers(10,34,89))

#variable number of keyword arguments
def trainerDetails(**details):
    print(details)

trainerDetails(name = "Aishwarya",
               age = 34,
               specialization = "AI/Mobile Application Dev",
               yearsOfExp = 12,
               city = "Pune",
               country = "India")

#local variable
def calculateAreaOfCircle():
    radius = 10.0           #local variable
    print("radius : {}".format(radius))
    print("area of circle : {}".format(3.14 * radius * radius))

calculateAreaOfCircle()
#globally declaration pf variables
length = 12.0
breadth = 45.0

def calculateAreaOfRect():
    print("length : {}".format(length))
    return length * breadth

calculateAreaOfRect()
print(length)

n = 5
# 5 * 4 * 3 * 2 * 1 * 0!

#n! = n * (n-1)!
#recursive functions - function calling itself
def factorialCalculation(number):
    if number == 1:
        return 1
    else:
        return number * factorialCalculation(number - 1)

print("Factorial is : {}".format(factorialCalculation(5)))