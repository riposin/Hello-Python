### Classes ###

if 1 == 1:
	pass # Null operation/statement

class MyEmptyPerson:
	pass

person = MyEmptyPerson()
person = MyEmptyPerson

class Person:
	def __init__(self, name, surname, alias):
		self.name = name
		self.surname = surname
		self.__alias = alias # Private attribute

	def get_alias(self):
		return self.__alias

	def walk (self):
		print("I am walking")

person = Person("Ricardo", "Pool", 'Riposin')

print(person.name)
print(person.surname)