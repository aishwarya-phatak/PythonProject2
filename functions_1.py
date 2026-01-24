#function definition
def welcomeMessage():
    print("Welcome to Bitcode!")

welcomeMessage()    #function call

def addition():
    num1 = 10
    num2 = 20
    print(num1 + num2)

addition()

def checkEvenOdd(num):
    if num % 2 == 0:
        print("{} is even".format(num))
        return num + 10
    else:
        print("{} is odd".format(num))
        return num - 10

number = checkEvenOdd(18)
print(number)

checkEvenOdd(45)

#recursive function
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)

print(factorial(3))

#multiple values can be returned from a function
def mathsOperations(num1, num2):
    add2 = num1 + num2
    subtract = num1 - num2
    multiply = num1 * num2
    division = num1 / num2
    return add2, subtract, multiply, division

print(mathsOperations(11, 28))
addResult,subResult,mulResult,divResult = mathsOperations(92, 31)
print(addResult)
print(subResult)
print(mulResult)
print(divResult)
print("--------------------")
#return statement without returning a value is allowed
#Functions are first class objects
def printHello():
    print("Hello World!")
    return

#1 -- assign variable to the function
print1 = printHello
print1()
printHello()
print("--------------------")

#2 -- function inside another function
def printMessage():
    def printBatchDetails(batchId):
        print("{} batchId batch will launch soon".format(batchId))

    printBatchDetails(13425)
    printBatchDetails(29876)
    printBatchDetails(34107)

printMessage()
print("--------------------")

#3 -- function as an argument
def mathematicalOperations(num1,num2,operation):
    return operation(num1, num2)

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
   return num1 - num2

add1 = mathematicalOperations(32,19,add)
print("add1 is {}".format(add1))
sub1 = mathematicalOperations(354,10,sub)
print("sub1 is {}".format(sub1))

#4 -- function as return type
def selectOperation(choiceValue):
    if choiceValue == 1:
        return add
    else:
        return sub

choice = int(input("Please enter a choice 1 for add and 2 for sub : "))
addRes1 = mathematicalOperations(14,56,selectOperation(choice))
print("addRes1 is {}".format(addRes1))