#loops
import array as a
#1 for loop
arr = a.array('i', [12, 2, 43, 47, 5, 60, 71, 8, 19,10])
sumOfAllElements = 0
for eachElement in arr:
    sumOfAllElements = sumOfAllElements + eachElement
print(sumOfAllElements)

#2 find sum of all even elements from an array
sumOfEvenElements = 0
sumOfOddElements = 0
for eachElement in arr:
    if eachElement % 2 == 0:
        sumOfEvenElements = sumOfEvenElements + eachElement
    else:
        sumOfOddElements = sumOfOddElements + eachElement
print(sumOfEvenElements)
print(sumOfOddElements)

#3 else suite example with for loop
sumOfElementsAtEvenIndices = 0
sumOfElementsAtOddIndices = 0
for index in range(len(arr)):
    if index % 2 == 0:
        sumOfElementsAtEvenIndices = sumOfElementsAtEvenIndices + arr[index]
    else :
        sumOfElementsAtOddIndices = sumOfElementsAtOddIndices + arr[index]
else:
    print("else suite after execution of for loop")

print("Sum of Elements At even indices : {}".format(sumOfElementsAtEvenIndices))
print("Sum of Elements At odd indices : {}".format(sumOfElementsAtOddIndices))