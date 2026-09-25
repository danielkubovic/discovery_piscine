#!/usr/bin/python3

class Person:
	def array_of_names(self, dict):
		return [f"{key.capitalize()} {value.capitalize()}" for key, value in persons.items()]

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}

person = Person()
print(person.array_of_names(persons))
