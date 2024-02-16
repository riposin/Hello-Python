### Sets ###

c = 1

my_set = set()
my_other_set = {}

#1
print(str(c),'-')
print('\t', type(my_set))
print('\t', type(my_other_set)) # At the beginning its type is dictionary
my_other_set = {"Ricardo", "Pool", 35}
print('\t', type(my_other_set)) # Now its type is set, that is because the way to define/initialize a dict and set is the sameñ
c += 1

#2 Add elements
print(str(c),'-')
my_other_set.add("riposin")
print('\t', my_other_set) # A set is an unordered collection of elements, like a hash table
my_other_set.add("riposin")
print('\t', my_other_set) # A set does not allow duplicated elements
c += 1

#3 Search for elements
print(str(c),'-', "rip" in my_other_set)
c += 1

#4 Remove elements
#str(c),'-', 
my_other_set.remove("riposin")
print(str(c),'-', my_other_set)
c += 1

#5 Sum
my_new_set = {1, 2, 3}
print(str(c),'-', my_new_set.union(my_other_set))
c += 1

#6 Difference
print(str(c),'-', my_new_set.difference({2}))
c += 1