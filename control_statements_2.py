#break statement
import array as a

#break - exists once condition is matched
arr = a.array('i', [33,24,56,72,94])
findValue = 72
for i in arr:
    if findValue == i:
        print("value {} found".format(findValue))
        break
else:                           #else suite statement
    print("value {} not found".format(findValue))
print("===================")
#continue statement - skips the iteration for which condition match
#skips basically one iteration
for i in range(1,10):
    if i == 3:
        continue
    print(10 // (i - 3))

print("===================")

#pass statement
i = -10
while i > 10:
    pass
    print(i)

#assert statement
#using eval
number = eval(input("Enter a number: "))
assert 5.0 < number < 10.0, "number does not lie in the range of 5 to 10"
print(" {} lies in the range of 5.0 to 10.0".format(number))

#type casting the input
number = input("Enter a number: ")
assert 5 < int(number) < 10
print(" {} lies in the range of 5 to 10".format(number))