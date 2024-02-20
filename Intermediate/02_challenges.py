### Challenges ###

'''
FizzBuzz
3 => Fiz
5 => Buzz
3 & 5 => FizBuzz
'''

def fizzBuzz(n):
	for i in range(1, n + 1):
		if i % 3 == 0 and i % 5 == 0:
			print("FizzBuzz")
		elif i % 3 == 0:
			print("Fizz")
		elif i % 5 == 0:
			print("Buzz")
		else:
			print(i)

fizzBuzz(100)

def palindromo(s):
	normal = list(s.lower())
	reverse = list(s.lower())
	reverse.reverse()
	if normal == reverse:
		print(s, "it is a palindromo")
	else:
		print(s, "it is not a palindromo")

palindromo("Ricardo")
palindromo("anitalavalatina")

def anagram(word_one, word_two):
	word_one = word_one.lower()
	word_two = word_two.lower()
	list_word_one = list(word_one)
	list_word_two = list(word_two)
	list_word_one.sort()
	list_word_two.sort()
	
	# sorted(list_word_one) # order and return a list
	# sorted(list_word_two) # order and return a list

	if word_one == word_two:
		print(word_one, 'it is not an anagram of', word_two)
	elif list_word_one == list_word_two:
		print(word_one, 'it is an anagram of', word_two)
	else:
		print(word_one, 'it is not an anagram of', word_two, 'they are equal')
	
anagram('zAbr','rbzA')
anagram('zAbr','rbzAa')
anagram('zAbr','zAbr')

def fibonacci():
	previous = 0
	current = 1
	print(0)
	print(1)
	for i in range(2, 50):
		fib = previous + current
		previous = current
		current = fib
		print(i, previous, current)
fibonacci()

def prime():
	for i in range(1, 101):
		esprimo = False
		for j in range(2, i):
			if i % j == 0:
				break
		else:
			esprimo = True
		
		if esprimo and i > 1:
			print(i, 'es primo')
		'''
		if i == 1:
			print(i, 'no es primo')
		elif esprimo:
			print(i, 'es primo')
		else:
			print(i, 'no es primo')
		'''
prime()


def reverse(string):
	reversed = ''
	'''
	reversecounter = len(string) - 1
	for i in string:
		reversed += string[reversecounter]
		reversecounter -= 1
	'''
	for i in range(len(string) - 1, -1, -1):
		reversed += string[i]
	
	print(reversed)

reverse("abcde")