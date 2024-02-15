# Variables

my_variable = 'My String Variable'
print(my_variable)

# Concatenate strings
print("foo", "bar", my_variable)

# NoneType
print(type(print("some")))

print(len(my_variable))

# Define variables in a single line
name, surname, alias, age = "John", "Doe", "Johnny", 35

print('My name is:', name, surname, ', my nickname is:', alias, ' and I am',age, 'old.')

# Inputs
first_name = 'Rick'
'''
first_name = input('What is your name? ')
age = input('How old are you? ')
'''

print('My name is:', first_name, 'and I am', age, 'years old.')

# Type definition, it does not work, it is only to help us to understand the intention of the code/variable
address: str = 'Foo Bar'
address = 123
print(address)
