# Wrtie two codes that will return the factorial of a number
# using user defined funtion and lambda function.


# Codes that will return the factorial of a number using user defined funtion
import sys


factorial = 1
number = int(sys.argv[1])

if number < 0:
    print("No factorial for this number")
elif number == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1,number+1):
        factorial = factorial * i
    print("Factorial of",number,"is",factorial)
