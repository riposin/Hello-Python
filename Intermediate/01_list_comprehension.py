### List comprehension ###

c = 1

my_original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_original_list)

my_range = range(15)
print(list(my_range))

my_list = [i for i in range(12)]
print(my_list)

my_list = [i + 1 for i in range(12)]
print(my_list)

def sum_five(number):
	return number + 5

my_list = [sum_five(i) for i in range(12)]
print(my_list)