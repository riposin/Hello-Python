### Higher order functions ###

from functools import reduce

def sum_one(value):
	return value + 1

def sum_two_values_and_one(a, b, func):
	return func(a + b)

print(sum_two_values_and_one(1, 2, sum_one))

### Closures ###

def sum_ten():
	def add(value):
		return value + 10
	return add

add_closure = sum_ten()
print(add_closure(6))

def sum_ten_param(value_original):
	def add(value):
		return value + 10 + value_original
	return add

add_closure = sum_ten_param(4)
print(add_closure(6))

print(sum_ten_param(3)(2))

### Built-in higher order functions ###
# Map

def mutiply_by_two(value):
	return value * 2

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(map(mutiply_by_two, my_list)))

print(list(map(lambda number: number * 3, my_list)))

# Filter

def filter_greater_than_five(value):
	return value > 5

print(list(filter(filter_greater_than_five, my_list)))

# Reduce

def sum_two_numbers(number_one, number_two):
	return number_one + number_two

print(reduce(sum_two_numbers, my_list))