#anonymous functions

sqrOfNumber = lambda num : num * num
print("sqrOfNumber is {}".format(sqrOfNumber(10)))

maximumOfThree = lambda n1,n2,n3 : max(n1,n2,n3)
print("maximumOfThree is {}".format(maximumOfThree(13,87,66)))

max1 = lambda x,y : x if x > y else y
print("max1 is {}".format(max1(10,20)))

res = lambda n : n % 2 == 0
print("res is {}".format(res(103)))