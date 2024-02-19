### Loops ###

c = 1

#1 While
print("-" * 30)
print(str(c),'- While:')
print("-" * 30)

i = 0
while i < 10:
	print("Iteration A", i)
	i += 1

i = 0
while i < 10:
	print("Iteration B", i)
	i += 1

	if i == 5:
		break
else:
	print("Condition B was not met")

#2 For
print("-" * 30)
print(str(c),'- For:')
print("-" * 30)

my_list = [35, 24, 62, 52, 30, 30, 17] # tuple, set
my_dict = {"a": "1", "b": "2", "c": "3"}

print("(a) list")
for element in my_list:
	print(element)

print('\n(b) dict')
for element in my_dict:
	print(element, my_dict[element])
	#print(element, element.value) # This will not work

print('\n(c) forelse')
for element in my_dict:
	print(element, my_dict[element])
else:
	print("For bucle has ended")

print('\n(d) forelsebreak')
for element in my_dict:
	print(element, my_dict[element])
	if element == "b":
		break
else:
	print("For bucle has ended")

print('\n(e) forcontinue')
for element in my_dict:
	print(element, my_dict[element])
	if element == "b":
		continue # It stops the current iteration and continue with the next one
	print('End of FOR block')
else:
	print("For bucle has ended")

print("-" * 30)
print("Done")

