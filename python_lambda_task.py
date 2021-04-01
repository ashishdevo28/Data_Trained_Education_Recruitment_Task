# Wrtie two codes that will return the factorial of a number
# using user defined funtion and lambda function.


# Codes that will return the factorial of a number using user defined funtion
import sys

num = int(sys.argv[1])
factorial = lambda x: x and x * factorial(x - 1) or 1
print(factorial(num))
