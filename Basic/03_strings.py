### Strings ###

# Special characters: \n, \t, \\ <-- \ is an escape character

# Formating of strings

name, surname, age = 'Ricardo', 'Pool', 35

print("1) Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print('2) Mi nombre es %s %s y mi edad es %d' %(name, surname, age))
print(f"3) Mi nombre es {name} {surname} y mi edad es {age}")
print("4) Mi nombre es {1} {0} y mi edad es {2}".format(name, surname, age))

# Unpacking characters
language = 'PY'
f, g = language
a, b = 'xy'
print('5)', a)
print('6)', b)
print('7)', f)
print('8)', g)

# Division
foo = 'ABCDEF'

sliced = foo[1:3] # Char start position, before char end position BC
print('9)', sliced)

sliced = foo[1:]
print('10)', sliced)

sliced = foo[-2]
print('11)', sliced)

sliced = foo[0:6:2] # ??
print('12)', sliced)

# Reverse
print('13)', foo[::-1])

# Methods
print('14)', foo.count("C"))
print('15)', foo.lower())
print('16)', foo.isnumeric()) # False
print('17)', '55'.isnumeric()) # True
print('18)', foo.lower().islower()) # True
print('19)', foo.islower()) # True
print('20)', foo.startswith("A")) # True
print('21)', foo.startswith("a")) # False