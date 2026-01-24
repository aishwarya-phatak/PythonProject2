numberOne = 14
print("numberOne is {}".format(numberOne))
print("id(numberOne) is {}".format(id(numberOne)))

numberTwo = numberOne
print("id(numberTwo) is {}".format(id(numberTwo)))

numberTwo = 56
print("numberOne is {}".format(numberOne))
print("id(numberOne) is {}".format(id(numberOne)))

print("numberTwo is {}".format(numberTwo))
print("id(numberTwo) is {}".format(id(numberTwo)))

print("-----------------")

#passing value to a function as an argument
def testFunction(num1):
    print("num1 is {}".format(num1))

# passing reference to a function as an argument
testFunction(id(numberOne))

print("----------------------")

#functions - formal and actual parameters in terms of reference
def testFunc2(num): #formal parameter
    num += 5
    print("num is {}".format(num))

n1 = 10
testFunc2(n1)       #actual parameter

