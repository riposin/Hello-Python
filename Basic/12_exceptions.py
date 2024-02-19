### Exceptions ###

numberOne = 10
numberTwo = "1"

try:
	print(numberOne + numberTwo)
except:
	print("(A) - Error, you can only concatenate integers and strings")

try:
	pass
except:
	print("This will not be reached because the error was handled")
else:
	print("(B) - The operation was successful")


try:
	print(numberOne + numberTwo)
except TypeError:
	print("(C) - Exception Type: TypeError")

try:
	print(numberOne + numberTwo)
except TypeError as error:
	print("(D) - Exception by type details: ", error)

try:
	print(numberOne + numberTwo)
except Exception as exception:
	print("(E) - Exception generic details: ", exception)

try:
	print(numberOne + numberTwo)
except ValueError as exception:
	print('This will not be reached because the error is not the proper type')
except Exception as exception:
	print("(F) - Default exception handling: ", exception)