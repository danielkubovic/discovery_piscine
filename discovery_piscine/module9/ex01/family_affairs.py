#!/usr/bin/python3

class Person:
	def find_the_redheads(self, dict):
		return list(filter(lambda color: dict[color] == "red", dict))

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

person = Person()
print(person.find_the_redheads(dupont_family))
