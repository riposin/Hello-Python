### Functions ###

c = 1

#1

def my_function():
	print("Hello")

my_function()

def sum(a, b):
	return a + b

print(sum(1, 2))

def default_sum(a, b = 5):
	return a + b

def multiple_sum(*args):
	a = 0
	for arg in args:
		a += arg
	return a

print(multiple_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))