### Aritmetic operators ###

## The basic operators are the same +, -, *
print(10 % 3) # Module: 1

print(10 // 3) # Floor Division: 3

print(5 // 10) # Floor Division: 0

print(5 ** 3) # Exponent: 125

print(2 ** 3 + 3 - (7 / 1) // 4) 
'''
	(2 ** 3) + 3 - ((7 / 1) // 4)
	8 + 3 - (7 // 4)
	8 + 3 - 1
	10
'''

print("A" + "B" + "C") # Simple string concatenation

print("A" * 5) # String repetition

## print("A" * (2 ** 3 + 3 - (7 / 1) // 4)) # String repetition, it will not work because a float value was provided as argument

print("A" * int(2 ** 3 + 3 - (7 / 1) // 4)) # String repetition, you need to provide an int value

### Comparative operators ###

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)

# Dictionary/alpabetic order
print("AA" > "F")
print("AbCa" >= "AbcA")

### Logical operators ###
# True, False, and, or, not
