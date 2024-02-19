### Lists ###

c = 1

my_list = list()
my_other_list = []

#1
print(str(c),'-',len(my_list))
c += 1

#2
my_list = [35, 24, 62, 52, 30, 30, 17]
print(str(c),'-',my_list)
c += 1

#3
print(str(c),'-',len(my_list))
c += 1

#4
my_other_list = [35, 1.77, 'Ricardo', 'Pool']
print(str(c),'-',type(my_other_list))
c += 1

#5
print(str(c),'-', my_other_list[0])
c += 1

#6
print(str(c),'-')
print("\t", my_other_list[-1])
print("\t", my_other_list[-3])
print("\t", my_other_list[-4])
#print(str(c),'-', my_other_list[-5]) # Error, the -4 is the equivalent to 0
c += 1

#7 Unpack
age, tall, name, surname = my_other_list
print(str(c),'-', tall)
c += 1

#8 Sum
print(str(c),'-', my_list + my_other_list)
c += 1

#9 Add/Remove elements
print(str(c),'-')

my_other_list.append("T&M")
print("\t", my_other_list)

my_other_list.insert(len(my_other_list) - 1, "Venbenetta")
print("\t", my_other_list)

my_other_list.append("T&M")
print("\t", my_other_list)
my_other_list.remove("T&M") # It only removes the first occurrence of an known value
print("\t", my_other_list)

print("\t", my_other_list.pop(len(my_other_list) - 1))# Remove an element by index and keep the value removed
print("\t", my_other_list)

del my_other_list[len(my_other_list) - 1] # Remove an element by index
print("\t", my_other_list)
# Notice: del word is used to "delete" variables, like dispose of objects

c += 1

#10 Copy lists
print(str(c),'-')

my_new_list1 = my_other_list.copy()
my_new_list2 = my_new_list1 # It keeps the same reference
my_new_list1.clear()
print('\t', my_new_list2)
my_new_list1 = my_other_list.copy() 
my_new_list2 = my_new_list1.copy() # Creates a new list
my_new_list1.clear()
print('\t', my_new_list2)
c += 1

#11 Reverse list
my_other_list.reverse()
print(str(c),'-', my_other_list)
my_other_list.reverse()
c += 1

#12 Slices
print(str(c),'-')
slice = my_other_list[1:3]
print('\t', my_other_list)
print('\t', slice)
c += 1
