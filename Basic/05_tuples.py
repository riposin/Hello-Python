### Tuples ###

c = 1

# Constructors
my_tuple = tuple()
my_other_tuple = ()

my_tuple = (32, 1.77, "Ricardo", "Pool")

#1
print(str(c),'-', my_tuple)
c += 1

#2
print(str(c),'-', type(my_tuple))
c += 1

#3 Try to change a tuple
print(str(c),'-', my_tuple[2])
#my_tuple[2] = "Jesus" # 'tuple' object does not support item assignment, it is inmutable at level definition
c += 1

#4 Convert Tuple to List and vice versa
print(str(c),'-')

my_tuple = list(my_tuple)
print('\t', type(my_tuple))

my_tuple.insert(1, "Pool")
my_tuple = tuple(my_tuple)
print('\t', type(my_tuple))


