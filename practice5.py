class Person:
	def __init__(x, name, age, origin, residence):
		x.name = name
		x.age = age
		x.origin = origin
		x.residence = residence
listperson = []
num = int(input('How many people would you like to record?'))
for x in range(num):
	name = input('What is their name?')
	age = input('What is their age?')
	origin = input("what is their country of origin?")
	residence = input('what is their country of residence?')
	listperson.append(Person(name,age,origin,residence))
	
for x in range(num):
	print(listperson[x].name)
	print(listperson[x].age)
	print(listperson[x].origin)
	print(listperson[x].residence)
	
    